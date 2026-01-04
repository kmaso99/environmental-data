"""
Prepare the Bird Individual ID dataset for training.

This script:
- Validates folder structure
- Creates train/val/test splits if missing
"""

from pathlib import Path
import shutil
import random

DATA_DIR = Path("data/birds")
TRAIN = DATA_DIR / "train"
VAL = DATA_DIR / "val"
TEST = DATA_DIR / "test"

def create_split():
    if TRAIN.exists():
        print("Dataset already prepared.")
        return

    print("Preparing dataset...")

    # Original dataset folder
    original = DATA_DIR / "Bird_individualID"

    classes = [d for d in original.iterdir() if d.is_dir()]

    TRAIN.mkdir(parents=True)
    VAL.mkdir(parents=True)
    TEST.mkdir(parents=True)

    for cls in classes:
        images = list(cls.glob("*.jpg"))
        random.shuffle(images)

        n = len(images)
        train_split = int(n * 0.7)
        val_split = int(n * 0.15)

        splits = {
            TRAIN / cls.name: images[:train_split],
            VAL / cls.name: images[train_split:train_split + val_split],
            TEST / cls.name: images[train_split + val_split:],
        }

        for split_dir, imgs in splits.items():
            split_dir.mkdir(parents=True, exist_ok=True)
            for img in imgs:
                shutil.copy(img, split_dir / img.name)

    print("Dataset prepared successfully.")

if __name__ == "__main__":
    create_split()
