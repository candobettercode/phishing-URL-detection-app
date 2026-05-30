# phishing-URL-detection-app
This app detects phishing URL. 

Project Organization
------------

phishing-url-detection-app/
│
├── frontend/                        # React frontend
│   └── Dockerfile
│
├── backend/
│   ├── app/
│   │   ├── api/                     # Routes
│   │   ├── config/                  # Config/settings
│   │   ├── artifacts/               # ML model loading
│   │	│   ├── models/
│   │	│   └── metrics/
│   │   ├── utils/
│   │	│   ├── __init__.py
│   │	│   ├── preprocessing.py
│   │	│   └── load_model_test.py
│   │   ├── requirements.txt
│   │   └── main.py
│   │
│   ├── data/
│   │	├── raw/
│   │	└── processed/
│   ├── src/
│   │	├── connections/
│   │	│   ├── __init__.py
│   │	│   └── s3_connections.py
│   │	├── utils/
│   │	│   ├── __init__.py
│   │	│   └── common.py
│   │	├── components/
│   │	│   ├── __init__.py
│   │	│   ├── data_ingestions.py
│   │	│   ├── model_evaluation_mlflow.py
│   │	│   ├── model_training.py
│   │	│   └── prepare_base_model.py
│   │	│
│   │	├── config/
│   │	│   ├── __init__.py
│   │	│   └── configuration.py
│   │	├── constants/
│   │	│   └── __init__.py
│   │	├── pipeline/
│   │	│   ├── __init__.py
│   │	│   ├── stage_01_data_ingestions.py
│   │	│   ├── stage_04_model_evaluation_mlflow.py
│   │	│   ├── prediction.py
│   │	│   ├── stage_03_model_training.py
│   │	│   └── stage_02_prepare_base_model.py
│   │	├── entity/
│   │	│   ├── config_entity.py
│   │	│   └── __init__.py.py
│   │	├── exception.py
│   │	├── logger.py
│   │	└── __init__.py
│   │
│   ├── logs/
│   ├── notebooks/                   # EDA/experiments
│   ├── saved_models/
│   ├── tests/
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── setup.py
│   ├── test_environment.py
│   └── .env
│
├── docker-compose.yml
├── README.md
└── .github/workflows/
