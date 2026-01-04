"""
Verify dataset integrity before training.

Checks:
- train/val/test folders exist
- each split contains class directories
- each class directory has images
"""

import os
from pathlib import Path

DEFAULT_DATA_DIR = Path("data/birds")
IMG_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

def iter_images(folder: Path):
    for p in folder.rglob("*"):
        if p.is_file() and p.suffix.lower() in IMG_EXTS:
            yield p

def verify(data_dir: Path) -> None:
    required = ["train", "val", "test"]

    for split in required:
        split_path = data_dir / split
        if not split_path.exists():
            raise FileNotFoundError("Missing split: " + str(split_path))

        class_dirs = [p for p in split_path.iterdir() if p.is_dir()]
        if not class_dirs:
            raise ValueError("No class directories found in " + str(split_path))

        for cls_dir in class_dirs:
            imgs = list(iter_images(cls_dir))
            if not imgs:
                raise ValueError("Class " + cls_dir.name + " has no images in " + split)

    print("Dataset verification passed at " + str(data_dir))

if __name__ == "__main__":
    data_dir_str = os.environ.get("DATA_DIR", str(DEFAULT_DATA_DIR))
    data_dir = Path(data_dir_str)
    verify(data_dir)
