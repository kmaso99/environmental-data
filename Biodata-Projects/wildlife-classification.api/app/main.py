from fastapi import FastAPI, UploadFile
from model import BirdClassifier

app = FastAPI()
model = BirdClassifier()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
async def predict(file: UploadFile):
    pred = model.predict(file.file)
    return {"prediction": pred}
