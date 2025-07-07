import os
import joblib
import numpy as np
from flask import Flask, render_template, request

"""
RainFlux – Flask API
--------------------
Loads the XGBoost model and the saved LabelEncoders, converts user inputs
into the numeric array expected by the model, and returns a prediction
with a confidence‑based color class (high‐, medium‑, or low‑confidence).
"""

app = Flask(__name__)

# ------------------------------------------------------------------
# Paths to artifacts
# ------------------------------------------------------------------
MODEL_PATH = "artifacts/models/model.pkl"
ENCODER_DIR = "artifacts/processed"  # *_encoder.pkl live here

# ------------------------------------------------------------------
# Load model and encoders once at startup
# ------------------------------------------------------------------
model = joblib.load(MODEL_PATH)

CATEGORICAL_COLS = ["Location", "WindGustDir", "WindDir9am", "WindDir3pm", "RainToday"]

encoders = {}
for col in CATEGORICAL_COLS:
    enc_path = os.path.join(ENCODER_DIR, f"{col}_encoder.pkl")
    if not os.path.exists(enc_path):
        raise FileNotFoundError(f"LabelEncoder file missing: {enc_path}")
    encoders[col] = joblib.load(enc_path)

# Ordered feature list expected by the model
FEATURES = [
    "Location",
    "MinTemp",
    "MaxTemp",
    "Rainfall",
    "Evaporation",
    "Sunshine",
    "WindGustDir",
    "WindGustSpeed",
    "WindDir9am",
    "WindDir3pm",
    "WindSpeed9am",
    "WindSpeed3pm",
    "Humidity9am",
    "Humidity3pm",
    "Pressure9am",
    "Pressure3pm",
    "Cloud9am",
    "Cloud3pm",
    "Temp9am",
    "Temp3pm",
    "RainToday",
    "Year",
    "Month",
    "Day",
]

LABELS = {0: "NO", 1: "YES"}

# ------------------------------------------------------------------
# Helper – preprocess user form inputs
# ------------------------------------------------------------------


def preprocess_input(form_data):
    """Convert form data dict into a 2‑D numpy array for model.predict."""
    values = []
    for feat in FEATURES:
        raw_val = form_data.get(feat)
        if feat in encoders:
            # Encode categorical feature
            values.append(encoders[feat].transform([raw_val])[0])
        else:
            # Convert to float (numeric feature)
            try:
                values.append(float(raw_val))
            except (TypeError, ValueError):
                raise ValueError(f"Invalid input for {feat}: {raw_val}")
    return np.array(values).reshape(1, -1)


# ------------------------------------------------------------------
# Main route
# ------------------------------------------------------------------


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = probability = confidence_color = None
    if request.method == "POST":
        try:
            X = preprocess_input(request.form)
            pred_class = model.predict(X)[0]
            prob_yes = model.predict_proba(X)[0, 1]  # P(class==1, YES)

            prediction = LABELS[pred_class]
            probability = f"{prob_yes * 100:.1f}%"

            # Map probability to CSS class
            confidence_color = (
                "high-confidence"
                if prob_yes >= 0.8
                else "medium-confidence"
                if prob_yes >= 0.6
                else "low-confidence"
            )
        except Exception as e:
            prediction = "Error"
            probability = str(e)
            confidence_color = "low-confidence"

    return render_template(
        "index.html",
        prediction=prediction,
        probability=probability,
        confidence_color=confidence_color,
        features=FEATURES,
        categorical_cols=CATEGORICAL_COLS,
    )


# ------------------------------------------------------------------
# Entrypoint
# ------------------------------------------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
