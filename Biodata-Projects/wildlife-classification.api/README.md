# 🐾 Wildlife Image Classification API

FastAPI + PyTorch microservice for wildlife species classification

---

## 📌 Overview

This project is a lightweight, production‑ready **image classification API** built with **FastAPI** and **PyTorch**. It provides a clean, modular inference pipeline for wildlife species classification and is designed to be easily extended with custom datasets, new model weights, or additional endpoints.

The service exposes a /predict endpoint for image uploads, performs preprocessing and model inference, and returns the predicted species label. It also includes a health check endpoint, Docker support, and a CI workflow for automated testing and container builds.

---

## 🚀 Features

- FastAPI backend with automatic OpenAPI/Swagger documentation
- PyTorch inference pipeline with pluggable model weights
- Transfer learning–ready architecture
- Dockerized deployment for reproducible environments
- GitHub Actions CI for testing and container builds
- Simple curl‑based testing for quick verification
- Clean, modular code structure suitable for production or research use

---

## 🐳 One‑Command Demo (Docker)

If you have Docker installed, you can run the API locally with:

```bash
docker build -t wildlife-api . && docker run --rm -p 8000:8000 wildlife-api
```

Then open:

- http://localhost:8000/docs (Swagger UI)
- http://localhost:8000/health (health check)

## 🧪 Quick test via curl

**Health check:**

```bash
curl http://localhost:8000/health
```

**Prediction (replace `path/to/image.jpg`):**

```bash
curl -X POST "http://localhost:8000/predict"   -H "accept: application/json"   -F "file=@path/to/image.jpg"
```

## 🛠️ Local Development (no Docker)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 📂 Repository Structure

```text
app/                FastAPI app, routing, and inference logic
    main.py         API entrypoint
    model.py        Model loading + prediction utilities
    utils.py        Preprocessing helpers

models/             Optional directory for model weights

.github/workflows/  CI pipeline (tests + Docker build)

Dockerfile          Container image definition
requirements.txt    Python dependencies
```

## 🧠 Customization Notes

- Update the placeholder classes list in app/model.py with your actual wildlife species labels.
- For production deployments, pin torch and torchvision versions and consider CPU‑only wheels if running on CPU infrastructure.
- You can swap in any PyTorch model (ResNet, EfficientNet, ViT, etc.) with minimal changes to the inference pipeline.

🌱 Future Enhancements (Optional)

- Add batch inference support
- Integrate model training notebook or pipeline
- Add test coverage reporting
- Deploy to AWS/GCP/Azure with Terraform or Docker Compose
- Add caching for repeated predictions
