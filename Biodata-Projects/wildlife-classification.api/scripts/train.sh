chmod +x scripts/train.sh

#!/bin/bash
# GPU-enabled training script

set -e

echo "Starting GPU training..."

export CUDA_VISIBLE_DEVICES=0

python training/train.py --device cuda

echo "Training complete."
