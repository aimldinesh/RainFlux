<p align="center">
  <img src="https://img.shields.io/badge/Project-RainFlux-00acc1?style=for-the-badge&logo=rainmeter&logoColor=white" alt="RainFlux Badge"/>
  <img src="https://img.shields.io/github/workflow/status/aimldinesh/RainFlux/CI/CD%20Deployment%20to%20GKE?style=for-the-badge&label=CI/CD&logo=github-actions&color=4caf50" alt="CI/CD Status Badge"/>
  <img src="https://img.shields.io/badge/MLOps-GKE%20%7C%20Flask%20%7C%20Docker%20%7C%20Kubernetes-blue?style=for-the-badge" alt="MLOps Stack Badge"/>
  <img src="https://img.shields.io/github/last-commit/aimldinesh/RainFlux?style=for-the-badge&color=orange" alt="Last Commit Badge"/>
</p>

# ☁️ RainFlux: Rain Prediction MLOps System

RainFlux is a production-ready end-to-end MLOps project that predicts whether it will rain tomorrow in Australian cities. The pipeline is powered by Flask, Docker, Kubernetes, and GitHub Actions to ensure reproducibility, scalability, and continuous delivery.

---

## 🚀 Project Overview

- **Problem**: Predict `RainTomorrow` based on 20+ meteorological features.
- **Model**: XGBoost Classifier with Label Encoding for categorical features.
- **UI**: Simple Flask Web Interface for input and prediction.
- **Deployment**:
  - Containerized with Docker
  - Deployed to Google Kubernetes Engine (GKE)
  - Automated using GitHub Actions CI/CD pipeline

---

## 📊 Tech Stack

| Layer        | Tools                                |
|-------------|--------------------------------------|
| Frontend     | HTML, CSS, Jinja2 (Flask Templates)  |
| Backend      | Flask (Python)                       |
| Model        | XGBoost + LabelEncoder               |
| Container    | Docker                               |
| Orchestration | Kubernetes (GKE)                    |
| CI/CD        | GitHub Actions                       |
| Cloud        | Google Cloud Platform (GKE, Artifact Registry) |

---

## 🧠 Features

- Clean web UI with confidence-based color prediction
- Uses trained ML model (XGBoost)
- LabelEncoders for all categorical inputs
- Color-coded confidence output (high, medium, low)
- Production-grade Docker and K8s setup
- Fully automated CI/CD pipeline via GitHub Actions

---

## 🧪 Model Details

- **Model**: XGBoostClassifier
- **Accuracy**: ~85%
- **Features Used**: 24
- **Encoding**: LabelEncoder for 5 categorical features
- **Output**: Binary classification (YES/NO) + confidence %

---

## 📦 Project Structure
```
MLOPS_RainFlux_project/
│
├── app.py                         # Flask app for predictions
├── Dockerfile                     # Docker image setup
├── kubernates-deployment.yaml     # K8s deployment manifest
├── requirements.txt               # Python dependencies
├── setup.py                       # Packaging config
├── .gitignore
│
├── .github/
│   └── workflows/
│       └── deploy.yml             # GitHub Actions for CI/CD
│
├── artifacts/
│   ├── models/
│   │   ├── model.pkl
│   │   ├── metrics.csv
│   │   ├── confusion_matrix.png
│   │   └── roc_curve.png
│   ├── processed/
│   │   ├── X_train.pkl
│   │   ├── y_train.pkl
│   │   └── <encoders>.pkl
│   └── raw/
│       └── data.csv
│
├── logs/
│   └── log_<date>.log             # App and training logs
│
├── notebook/
│   ├── notebook_testing.ipynb     # Jupyter exploration
│   └── artifacts/                 # Local notebook outputs
│
├── pipeline/
│   ├── training_pipeline.py       # Training orchestration script
│   └── __init__.py
│
├── src/
│   ├── custom_exception.py        # Custom error handler
│   ├── data_processing.py         # Data cleaning & feature engineering
│   ├── logger.py                  # Logging utility
│   ├── model_training.py          # Model training logic
│   └── __init__.py
│
├── static/
│   └── style.css                  # Frontend styling
│
├── templates/
│   └── index.html                 # Web app UI
│
└── venv/                          # Virtual environment (optional, ignored in Git)

```

