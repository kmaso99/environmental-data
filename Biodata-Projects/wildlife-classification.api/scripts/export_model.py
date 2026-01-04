"""
Export a trained model into a versioned artifact directory.
"""

import shutil
from pathlib import Path
import datetime

MODEL_DIR = Path("models")
EXPORTS = Path("exports")

def export_model():
    EXPORTS.mkdir(exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    export_path = EXPORTS / f"model-{timestamp}"
    export_path.mkdir()

    shutil.copy(MODEL_DIR / "bird_model.pt", export_path / "bird_model.pt")
    shutil.copy(MODEL_DIR / "classes.json", export_path / "classes.json")

    print(f"Model exported to {export_path}")

if __name__ == "__main__":
    export_model()
