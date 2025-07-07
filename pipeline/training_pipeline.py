from src.data_processing import DataProcessing
from src.model_training import ModelTraining

if __name__ == "__main__":
    # Initialize and run the data processing pipeline
    processor = DataProcessing("artifacts/raw/data.csv", "artifacts/processed")
    processor.run()

    # Initialize and run the model training and evaluation pipeline
    trainer = ModelTraining("artifacts/processed", "artifacts/models")
    trainer.run()
