PROJECT_DIR=Biodata-Projects/wildlife-classification.api

data:
    cd $(PROJECT_DIR) && python scripts/download_data.py && python scripts/prepare_data.py

verify:
    cd $(PROJECT_DIR) && python scripts/verify_data.py

train:
    cd $(PROJECT_DIR) && python training/train.py

test:
    cd $(PROJECT_DIR) && pytest -q

lint:
    cd $(PROJECT_DIR) && flake8 .

run:
    cd $(PROJECT_DIR) && uvicorn app.main:app --reload
