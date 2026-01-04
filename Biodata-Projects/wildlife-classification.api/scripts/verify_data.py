"""
Verify dataset integrity before training.

Checks:
- train/val/test folders exist
- each class has images
- no empty directories
"""

from pathlib import Path

DATA_DIR = Path("data/birds")

def verify():
    required = ["train", "val", "test"]
    for split in required:
        split_path = DATA_DIR / split
        if not split_path.exists():
            raise FileNotFoundError(f"Missing split: {split_path}")

        classes = list(split_path.iterdir())
        if not classes:
            raise ValueError(f"No classes found in {split_path}")

        for cls in classes:
            images = list(cls.glob("*.jpg"))
            if not images:
                raise ValueError(f"Class {cls.name} has no images in {split}")

    print("Dataset verification passed.")

if __name__ == "__main__":
    verify()
