<!-- Project Banner --> 
<p align="center">
    
![Wildlife Image Classification API Banner](https://github.com/kmaso99/environmental-data/blob/main/Biodata-Projects/wildlife-classification.api/banner.jpg)

</p>

<!-- Badges --> 
<p align="center">
    
![Build Status](https://github.com/kmaso99/environmental-data/actions/workflows/ci.yml/badge.svg)
![Docker](https://img.shields.io/badge/container-docker-blue)
[![API Docs](https://img.shields.io/badge/docs-FastAPI-green)](http://localhost:8000/docs)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-EE4C2C)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-blue)
![Docker](https://img.shields.io/badge/Docker-Ready-0db7ed)

</p>

# 🐾 Wildlife Image Classification API

Production-ready-ish FastAPI + PyTorch microservice for wildlife species classification, specifically birds

For full citation details, see the “Credits & Citation” section at the bottom of this README.

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

---

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

## 🌱 Future Enhancements (Optional)

- Add batch inference support
- Integrate model training notebook or pipeline
- Add test coverage reporting
- Deploy to AWS/GCP/Azure with Terraform or Docker Compose
- Add caching for repeated predictions

---

## 📚 Credits & Citation

### 🐦 Dataset
[![Dataset](https://img.shields.io/badge/Dataset-Bird%20Individual%20ID-green)](https://github.com/AndreCFerreira/Bird_individualID)

This project uses the **Bird Individual ID** dataset:

Ferreira, A. C., Silva, L. R., Renna, F., Brandl, H. B., Renoult, J. P., Farine, D. R., Covas, R., & Doutrelant, C. (2020).  
*Deep learning-based methods for individual recognition in small birds.*  
Methods in Ecology and Evolution.

If you use this dataset in academic or published work, please cite the authors:

```text
@article{deeplearningbirds,
  title={Deep learning-based methods for individual recognition in small birds},
  author={André C. Ferreira, Liliana R. Silva, Francesco Renna, Hanja B. Brandl, Julien P. Renoult, Damien R. Farine, Rita Covas and Claire Doutrelant},
  journal={Methods in Ecology and Evolution},
  year={2020}
}
```

**Dataset Repository:** https://github.com/AndreCFerreira/Bird_individualID  
**Contact:** André C. Ferreira (via GitHub profile)

## ✍️ How to Cite This Project

If you use this codebase, training pipeline, or API design in your own work, please cite:

Mason, K. (2026). Wildlife Image Classification API: A FastAPI + PyTorch service for single-species bird identification. GitHub repository: https://github.com/kmaso99/environmental-data

```text
@misc{mason2026wildlifeapi,
author       = {Kate Mason},
title        = {Wildlife Image Classification API: A FastAPI + PyTorch service for single-species bird identification},
year         = {2026},
howpublished = {\url{https://github.com/kmaso99/environmental-data}},
}
```
