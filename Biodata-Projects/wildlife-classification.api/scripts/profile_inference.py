"""
Benchmark inference latency for the FastAPI model.
"""

import time
from app.model import BirdClassifier
from PIL import Image
import io

def benchmark(iterations=50):
    model = BirdClassifier()

    dummy = Image.new("RGB", (224, 224))
    buf = io.BytesIO()
    dummy.save(buf, format="JPEG")
    buf.seek(0)

    times = []
    for _ in range(iterations):
        start = time.time()
        model.predict(buf)
        times.append(time.time() - start)
        buf.seek(0)

    print(f"Avg latency: {sum(times)/len(times):.4f}s")
    print(f"Min latency: {min(times):.4f}s")
    print(f"Max latency: {max(times):.4f}s")

if __name__ == "__main__":
    benchmark()
