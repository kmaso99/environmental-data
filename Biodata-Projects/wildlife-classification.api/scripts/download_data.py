"""
Download the Bird Individual ID dataset into data/birds/.

This script ensures reproducibility by standardizing where and how
the dataset is downloaded.
"""

import subprocess
from pathlib import Path

DATA_DIR = Path("data/birds")

def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    repo_url = "https://github.com/AndreCFerreira/Bird_individualID"

    print(f"Cloning dataset into {DATA_DIR}...")
    subprocess.run(["git", "clone", repo_url, str(DATA_DIR)], check=True)

    print("Download complete.")

if __name__ == "__main__":
    main()
