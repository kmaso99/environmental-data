from fastapi import FastAPI, File, UploadFile
from app.model import predict

app = FastAPI(title="Wildlife Image Classification API", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
async def predict_endpoint(file: UploadFile = File(...)):
    image_bytes = await file.read()
    result = predict(image_bytes)
    return result
