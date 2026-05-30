# phishing-URL-detection-app
This app detects phishing URL. 

Project Organization
------------

# Project Structure

```text
phishing-url-detection-app/
│
├── frontend/                              # React frontend application
│   └── Dockerfile                         # Frontend container configuration
│
├── backend/
│   │
│   ├── app/                               # Production inference application
│   │   ├── api/                           # FastAPI routes and endpoints
│   │   ├── config/                        # API configuration and settings
│   │   ├── artifacts/                     # Trained models and evaluation outputs
│   │   │   ├── models/
│   │   │   └── metrics/
│   │   ├── utils/                         # Inference utilities
│   │   │   ├── __init__.py
│   │   │   ├── preprocessing.py
│   │   │   └── load_model_test.py
│   │   ├── requirements.txt              # Inference dependencies
│   │   └── main.py                        # FastAPI application entry point
│   │
│   ├── data/
│   │   ├── raw/                           # Raw dataset files
│   │   └── processed/                     # Processed datasets
│   │
│   ├── src/                               # Training and experimentation package
│   │   ├── connections/
│   │   │   ├── __init__.py
│   │   │   └── s3_connections.py          # AWS S3 interactions
│   │   │
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   └── common.py                  # Common helper functions
│   │   │
│   │   ├── components/
│   │   │   ├── __init__.py
│   │   │   ├── data_ingestions.py         # Data ingestion component
│   │   │   ├── model_evaluation_mlflow.py # Model evaluation and MLflow tracking
│   │   │   ├── model_training.py          # Model training logic
│   │   │   └── prepare_base_model.py      # Base model preparation
│   │   │
│   │   ├── config/
│   │   │   ├── __init__.py
│   │   │   └── configuration.py           # Project configuration manager
│   │   │
│   │   ├── constants/
│   │   │   └── __init__.py                # Global constants
│   │   │
│   │   ├── pipeline/
│   │   │   ├── __init__.py
│   │   │   ├── stage_01_data_ingestions.py
│   │   │   ├── stage_02_prepare_base_model.py
│   │   │   ├── stage_03_model_training.py
│   │   │   ├── stage_04_model_evaluation_mlflow.py
│   │   │   └── prediction.py
│   │   │
│   │   ├── entity/
│   │   │   ├── __init__.py
│   │   │   └── config_entity.py           # Configuration dataclasses
│   │   │
│   │   ├── exception.py                   # Custom exceptions
│   │   ├── logger.py                      # Logging configuration
│   │   └── __init__.py
│   │
│   ├── logs/                              # Application and training logs
│   ├── notebooks/                         # EDA and experimentation notebooks
│   ├── saved_models/                      # Persisted trained models
│   ├── tests/                             # Unit and integration tests
│   ├── requirements.txt                   # Training dependencies
│   ├── Dockerfile                         # Backend container configuration
│   ├── setup.py                           # Python package setup
│   ├── test_environment.py                # Environment validation script
│   └── .env                               # Environment variables
│
├── .github/
│   └── workflows/                         # CI/CD pipelines
│
├── docker-compose.yml
├── README.md
└── .github/workflows/

```