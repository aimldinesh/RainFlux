import os
import joblib
import xgboost as xgb
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    roc_curve,
    auc,
)
from src.logger import get_logger
from src.custom_exception import CustomException

# Initialize logger
logger = get_logger(__name__)


class ModelTraining:
    def __init__(self, input_path, output_path):
        # Define paths and model
        self.input_path = input_path
        self.output_path = output_path
        self.model = xgb.XGBClassifier()
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

        # Ensure output directory exists
        os.makedirs(self.output_path, exist_ok=True)
        logger.info("✅ ModelTraining initialized")

    def load_data(self):
        # Load train/test data from disk
        try:
            self.X_train = joblib.load(os.path.join(self.input_path, "X_train.pkl"))
            self.X_test = joblib.load(os.path.join(self.input_path, "X_test.pkl"))
            self.y_train = joblib.load(os.path.join(self.input_path, "y_train.pkl"))
            self.y_test = joblib.load(os.path.join(self.input_path, "y_test.pkl"))
            logger.info("📥 Data loaded successfully")
        except Exception as e:
            logger.error(f"❌ Error while loading data: {e}")
            raise CustomException("Failed to load data", e)

    def train_model(self):
        # Train XGBoost classifier
        try:
            self.model.fit(self.X_train, self.y_train)
            joblib.dump(self.model, os.path.join(self.output_path, "model.pkl"))
            logger.info("✅ Model trained and saved")
        except Exception as e:
            logger.error(f"❌ Error while training model: {e}")
            raise CustomException("Failed to train model", e)

    def eval_model(self):
        # Evaluate model and save metrics, plots
        try:
            training_score = self.model.score(self.X_train, self.y_train)
            logger.info(f"📈 Training model score: {training_score:.4f}")

            y_pred = self.model.predict(self.X_test)
            y_prob = self.model.predict_proba(self.X_test)[:, 1]

            # Compute evaluation metrics
            accuracy = accuracy_score(self.y_test, y_pred)
            precision = precision_score(self.y_test, y_pred, average="weighted")
            recall = recall_score(self.y_test, y_pred, average="weighted")
            f1 = f1_score(self.y_test, y_pred, average="weighted")

            # Log metrics
            logger.info(
                f"✅ Accuracy: {accuracy:.4f}, Precision: {precision:.4f}, Recall: {recall:.4f}, F1-Score: {f1:.4f}"
            )

            # Save metrics to CSV
            metrics_path = os.path.join(self.output_path, "metrics.csv")
            pd.DataFrame(
                [
                    {
                        "accuracy": accuracy,
                        "precision": precision,
                        "recall": recall,
                        "f1_score": f1,
                        "train_score": training_score,
                    }
                ]
            ).to_csv(metrics_path, index=False)
            logger.info(f"📄 Metrics saved to {metrics_path}")

            # Save confusion matrix plot
            cm = confusion_matrix(self.y_test, y_pred)
            disp = ConfusionMatrixDisplay(confusion_matrix=cm)
            disp.plot(cmap="Blues")
            plt.title("Confusion Matrix")
            plt.savefig(os.path.join(self.output_path, "confusion_matrix.png"))
            plt.close()

            # Save ROC curve plot
            fpr, tpr, _ = roc_curve(self.y_test, y_prob)
            roc_auc = auc(fpr, tpr)
            plt.figure()
            plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {roc_auc:.2f})")
            plt.plot([0, 1], [0, 1], linestyle="--", color="gray")
            plt.xlabel("False Positive Rate")
            plt.ylabel("True Positive Rate")
            plt.title("ROC Curve")
            plt.legend()
            plt.savefig(os.path.join(self.output_path, "roc_curve.png"))
            plt.close()

            logger.info("📉 Confusion matrix and ROC curve saved")

        except Exception as e:
            logger.error(f"❌ Error while evaluating model: {e}")
            raise CustomException("Failed to evaluate model", e)

    def run(self):
        # Full pipeline execution
        self.load_data()
        self.train_model()
        self.eval_model()
        logger.info("🏁 Model training and evaluation pipeline completed")


if __name__ == "__main__":
    trainer = ModelTraining("artifacts/processed", "artifacts/models")
    trainer.run()
