#!/bin/bash
#SBATCH --job-name=greeting
#SBATCH --output=slurm/log/greeting_%j.out
#SBATCH --error=slurm/log/greeting_%j.err
#SBATCH --time=24:00:00
#SBATCH --gpus=1
#SBATCH --cpus-per-gpu=8
#SBATCH --mem-per-gpu=40G
#SBATCH --container-image ghcr.io\#arslanardavic/equivarianceeverywhere

set -euo pipefail


# Always start in the directory you ran `sbatch` from (the repo root)
cd "${SLURM_SUBMIT_DIR:-$PWD}"

# Ensure the log directory exists (under slurm/)
mkdir -p slurm/log

# resolve the same filename sbatch will use by expanding %j → $SLURM_JOB_ID
export SLURM_STDOUT_PATH="slurm/log/greeting_${SLURM_JOB_ID}.out"
export SLURM_STDERR_PATH="slurm/log/greeting_${SLURM_JOB_ID}.err"

# Run your training
python exec/greeting.py --message "Hello, World!"

# Change SBATCH out file names and paths for different setups.