from pathlib import Path

project_structure = {
        "frontend": {
            "public": {},
            "src": {
                "components": {},
                "pages": {},
            },
            "package.json": None,
            "vite.config.js": None,
            "Dockerfile": None,
        },

        "backend": {
            "app": {
                "api": {
                    "__init__.py": None,
                    "routes.py": None,
                },
                "config": {
                    "__init__.py": None,
                    "settings.py": None,
                },
                "models": {
                    "__init__.py": None,
                    "model_loader.py": None,
                },
                "artifacts": {
                    "models": {},
                    "metrics": {},
                },
                "utils": {
                    "__init__.py": None,
                    "preprocessing.py": None,
                    "load_model_test.py": None,
                },
                "requirements.txt": None,
                "main.py": None,
            },

            "data": {
                "raw": {},
                "processed": {},
            },

            "src": {
                "connections": {
                    "__init__.py": None,
                    "s3_connections.py": None,
                },

                "utils": {
                    "__init__.py": None,
                    "common.py": None,
                },

                "components": {
                    "__init__.py": None,
                    "data_ingestion.py": None,
                    "prepare_base_model.py": None,
                    "model_training.py": None,
                    "model_evaluation_mlflow.py": None,
                },

                "config": {
                    "__init__.py": None,
                    "configuration.py": None,
                },

                "constants": {
                    "__init__.py": None,
                },

                "entity": {
                    "__init__.py": None,
                    "config_entity.py": None,
                },

                "pipeline": {
                    "__init__.py": None,
                    "stage_01_data_ingestion.py": None,
                    "stage_02_prepare_base_model.py": None,
                    "stage_03_model_training.py": None,
                    "stage_04_model_evaluation_mlflow.py": None,
                    "prediction.py": None,
                },

                "exception.py": None,
                "logger.py": None,
                "__init__.py": None,
            },

            "notebooks": {},

            "saved_models": {},

            "logs": {},

            "tests": {
                "test_api.py": None,
                "test_preprocessing.py": None,
                "test_model.py": None,
            },

            "requirements.txt": None,
            "setup.py": None,
            "Dockerfile": None,
            "test_environment.py": None,
            ".env": None,
        },

        ".github": {
            "workflows": {}
        },

        "docker-compose.yml": None, 
}


def create_structure(base_path, structure):
    for name, content in structure.items():
        path = base_path / name

        if content is None:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch(exist_ok=True)

        elif isinstance(content, dict):
            path.mkdir(parents=True, exist_ok=True)
            create_structure(path, content)


if __name__ == "__main__":
    create_structure(Path("."), project_structure)
    print("✅ Project structure created successfully!")