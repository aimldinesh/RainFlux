import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import os
from src.logger import get_logger
from src.custom_exception import CustomException

# Initialize logger
logger = get_logger(__name__)


class DataProcessing:
    def __init__(self, input_path, output_path):
        # Set file paths
        self.input_path = input_path
        self.output_path = output_path
        self.df = None
        self.encoders = {}  # Dictionary to store label encoders

        # Create output directory if it doesn't exist
        os.makedirs(self.output_path, exist_ok=True)
        logger.info("✅ DataProcessing initialized")

    def load_data(self):
        # Load dataset from CSV
        try:
            self.df = pd.read_csv(self.input_path)
            logger.info("📥 Data loaded successfully")
        except Exception as e:
            logger.error(f"❌ Error while loading data: {e}")
            raise CustomException("Failed to load data", e)

    def preprocess(self):
        # Perform data cleaning and preprocessing
        try:
            # Convert Date column to datetime and extract features
            self.df["Date"] = pd.to_datetime(self.df["Date"])
            self.df["Year"] = self.df["Date"].dt.year
            self.df["Month"] = self.df["Date"].dt.month
            self.df["Day"] = self.df["Date"].dt.day
            self.df.drop("Date", axis=1, inplace=True)

            # Identify column types
            categorical = [
                col for col in self.df.columns if self.df[col].dtype == "object"
            ]
            numerical = [
                col
                for col in self.df.columns
                if col not in categorical and col != "RainTomorrow"
            ]

            # Fill missing numerical values with mean
            for col in numerical:
                self.df[col].fillna(self.df[col].mean(), inplace=True)

            # Fill missing categorical values with mode
            for col in categorical:
                self.df[col].fillna(self.df[col].mode()[0], inplace=True)

            # Drop any remaining missing values
            self.df.dropna(inplace=True)
            logger.info("🧹 Data preprocessing complete")

        except Exception as e:
            logger.error(f"❌ Error during preprocessing: {e}")
            raise CustomException("Failed to preprocess data", e)

    def label_encode(self):
        # Encode categorical variables using LabelEncoder
        try:
            categorical = [
                "Location",
                "WindGustDir",
                "WindDir9am",
                "WindDir3pm",
                "RainToday",
                "RainTomorrow",
            ]

            for col in categorical:
                encoder = LabelEncoder()
                self.df[col] = encoder.fit_transform(self.df[col])
                self.encoders[col] = encoder

                # Save encoder for future use
                joblib.dump(
                    encoder, os.path.join(self.output_path, f"{col}_encoder.pkl")
                )

                # Log label mapping
                logger.info(
                    f"🔤 Label mapping for '{col}': {dict(zip(encoder.classes_, encoder.transform(encoder.classes_)))}"
                )

            logger.info("✅ Label encoding complete")

        except Exception as e:
            logger.error(f"❌ Error during label encoding: {e}")
            raise CustomException("Failed to label encode data", e)

    def split_data(self):
        # Split data into training and testing sets and save them
        try:
            X = self.df.drop("RainTomorrow", axis=1)
            y = self.df["RainTomorrow"]

            logger.info(f"📊 Feature columns: {list(X.columns)}")

            # Perform stratified split to preserve class balance
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42, stratify=y
            )

            # Save datasets to disk
            joblib.dump(X_train, os.path.join(self.output_path, "X_train.pkl"))
            joblib.dump(X_test, os.path.join(self.output_path, "X_test.pkl"))
            joblib.dump(y_train, os.path.join(self.output_path, "y_train.pkl"))
            joblib.dump(y_test, os.path.join(self.output_path, "y_test.pkl"))

            logger.info("✅ Train-test split and saved successfully")

        except Exception as e:
            logger.error(f"❌ Error during data split: {e}")
            raise CustomException("Failed to split data", e)

    def run(self):
        # Execute the full data processing pipeline
        self.load_data()
        self.preprocess()
        self.label_encode()
        self.split_data()
        logger.info("✅ Data processing pipeline completed")


if __name__ == "__main__":
    processor = DataProcessing("artifacts/raw/data.csv", "artifacts/processed")
    processor.run()
