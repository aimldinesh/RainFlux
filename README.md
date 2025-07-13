<p align="center">
  <img src="https://img.shields.io/badge/Project-RainFlux-00acc1?style=for-the-badge&logo=rainmeter&logoColor=white" alt="RainFlux Badge"/>
  <img src="https://img.shields.io/github/actions/workflow/status/aimldinesh/RainFlux/deploy.yml?style=for-the-badge&label=CI/CD&logo=github-actions&color=4caf50" alt="CI/CD Status Badge"/>
  <img src="https://img.shields.io/badge/MLOps-GKE%20%7C%20Flask%20%7C%20Docker%20%7C%20Kubernetes-blue?style=for-the-badge" alt="MLOps Stack Badge"/>
  <img src="https://img.shields.io/github/last-commit/aimldinesh/RainFlux?style=for-the-badge&color=orange" alt="Last Commit Badge"/>
</p>

# ☁️ RainFlux: Rain Prediction MLOps System

RainFlux is a production-ready end-to-end MLOps project that predicts whether it will rain tomorrow in Australian cities. The pipeline is powered by Flask, Docker, Kubernetes, and GitHub Actions to ensure reproducibility, scalability, and continuous delivery.

---

## 🚀 Project Overview

* **Problem**: Predict `RainTomorrow` based on 20+ meteorological features.
* **Model**: XGBoost Classifier with Label Encoding for categorical features.
* **UI**: Simple Flask Web Interface for input and prediction.
* **Deployment**:

  * Containerized with Docker
  * Deployed to Google Kubernetes Engine (GKE)
  * Automated using GitHub Actions CI/CD pipeline

---

## 📊 Tech Stack

| Layer         | Tools                                          |
| ------------- | ---------------------------------------------- |
| Frontend      | HTML, CSS, Jinja2 (Flask Templates)            |
| Backend       | Flask (Python)                                 |
| Model         | XGBoost + LabelEncoder                         |
| Container     | Docker                                         |
| Orchestration | Kubernetes (GKE)                               |
| CI/CD         | GitHub Actions                                 |
| Cloud         | Google Cloud Platform (GKE, Artifact Registry) |

---

## 🧠 Features

* Clean web UI with confidence-based color prediction
* Uses trained ML model (XGBoost)
* LabelEncoders for all categorical inputs
* Production-grade Docker and K8s setup
* Fully automated CI/CD pipeline via GitHub Actions

---

## 🧪 Model Details

* **Model**: XGBoostClassifier
* **Accuracy**: \~85%
* **Features Used**: 24
* **Encoding**: LabelEncoder for 5 categorical features
* **Output**: Binary classification (YES/NO) + confidence %

---

## 📦 Project Structure

```
MLOPS_RainFlux_project/
│
├── app.py                         # Flask app for predictions
├── Dockerfile                     # Docker image setup
├── kubernates-deployment.yaml    # K8s deployment manifest
├── requirements.txt              # Python dependencies
├── setup.py                      # Packaging config
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

---

## 🛠️ Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/aimldinesh/RainFlux.git
cd RainFlux

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate

# 3. Install dependencies
pip install -e .  # or pip install -r requirements.txt
# 4. Run locally
python app.py
```

---

## 🐳 Docker Usage

```bash
# Build the Docker image
docker build -t rainflux-app .

# Run the container
docker run -p 5000:5000 rainflux-app
```
---

## 🚀 CI/CD Workflow

* **Trigger**: Push to `main` branch
* **Tool**: GitHub Actions
* **Pipeline Steps**:

  * Authenticate with Google Cloud
  * Build Docker image
  * Push to Artifact Registry
  * Deploy to GKE

File path: `.github/workflows/deploy.yml`

---

📸 Project Screenshots
🔍 Local Testing – Rain Prediction Output
<p align="center"> <img src="https://github.com/aimldinesh/RainFlux/blob/main/images/app_prediction_yes_on_local.PNG" width="48%" /> <img src="https://github.com/aimldinesh/RainFlux/blob/main/images/app_prediction_NO_on_local.PNG" width="48%" /> </p>
⚙️ GitHub Actions – CI/CD Pipeline
<p align="center"> <img src="https://github.com/aimldinesh/RainFlux/blob/main/images/Build_and_deploy_start_using_github_actions.PNG" width="48%" /> <img src="https://github.com/aimldinesh/RainFlux/blob/main/images/Build_and_deploy_complete_using_github_actions.PNG" width="48%" /> </p>
☁️ GCP Deployment – GKE + Kubernetes
<p align="center"> <img src="https://github.com/aimldinesh/RainFlux/blob/main/images/app_deployed_ongcp1.PNG" width="32%" /> <img src="https://github.com/aimldinesh/RainFlux/blob/main/images/app_deployed_on_gcp2.PNG" width="32%" /> <img src="https://github.com/aimldinesh/RainFlux/blob/main/images/app_deployed_on_gcp3.PNG" width="32%" /> </p>
🌐 App Running on GCP External IP
<p align="center"> <img src="https://github.com/aimldinesh/RainFlux/blob/main/images/app_running_on_gcp_ip1.PNG" width="32%" /> <img src="https://github.com/aimldinesh/RainFlux/blob/main/images/app_running_on_gcp_ip2.PNG" width="32%" /> <img src="https://github.com/aimldinesh/RainFlux/blob/main/images/app_running_on_gcp_ip_3.PNG" width="32%" /> </p>
✅ CI/CD Pipeline – Deployment Success
<p align="center"> <img src="https://github.com/aimldinesh/RainFlux/blob/main/images/github_deploy_done.PNG" width="60%" /> </p>

---

## 🙌 Acknowledgements

* [Weather Data ](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package)
* XGBoost, scikit-learn
* Google Cloud GKE & Artifact Registry
* GitHub Actions CI/CD

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---
