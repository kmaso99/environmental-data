# Wildlife Image Classification API

Production-ready-ish **FastAPI + PyTorch** service for wildlife species classification.

## One-command demo

If you have Docker installed, this is the quickest way to run the API locally:

```bash
docker build -t wildlife-api . && docker run --rm -p 8000:8000 wildlife-api
```

Then open:

- http://localhost:8000/docs (Swagger UI)
- http://localhost:8000/health (health check)

## Quick test via curl

Health:

```bash
curl http://localhost:8000/health
```

Predict (replace `path/to/image.jpg`):

```bash
curl -X POST "http://localhost:8000/predict"   -H "accept: application/json"   -F "file=@path/to/image.jpg"
```

## Local dev (no Docker)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Repo layout

```text
app/            FastAPI app + model loading/inference
models/         Model weights (optional)
.github/        CI workflows (tests + docker build)
Dockerfile      Container image for inference
requirements.txt Python deps
```

## Notes

- Swap the placeholder `classes` list in `app/model.py` for your wildlife species labels.
- For production, pin `torch/torchvision` versions and consider CPU-only wheels if you’re deploying on CPU.
