from app.model import BirdClassifier
from PIL import Image
import io

def test_model_loads():
    model = BirdClassifier()
    assert len(model.classes) > 0

def test_prediction_runs():
    model = BirdClassifier()
    dummy = Image.new("RGB", (224, 224))
    buf = io.BytesIO()
    dummy.save(buf, format="JPEG")
    buf.seek(0)
    pred = model.predict(buf)
    assert isinstance(pred, str)
