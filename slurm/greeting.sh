#!/bin/bash
#SBATCH --job-name=greeting
#SBATCH --output=log/greeting_%j.out
#SBATCH --error=log/greeting_s%j.err
#SBATCH --time=24:00:00
#SBATCH --gpus=1
#SBATCH --cpus-per-gpu=8
#SBATCH --mem-per-gpu=40G
#SBATCH --container-image ghcr.io\#arslanardavic/equivarianceeverywhere

set -euo pipefail

# Work from the directory where you ran `sbatch train.sbatch`
mkdir -p log
cd "${SLURM_SUBMIT_DIR:-$PWD}"

# Use node-local scratch if available, otherwise /tmp
SCRATCH="${SLURM_TMPDIR:-/tmp}"

# Run your training
python exec/greeting.py