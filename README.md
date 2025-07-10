# ☁️ RainFlux: Rain Prediction MLOps System

![CI/CD](https://img.shields.io/github/actions/workflow/status/your-username/RainFlux/deploy.yml?label=CI/CD%20GKE&style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3.9-blue?style=for-the-badge)

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

