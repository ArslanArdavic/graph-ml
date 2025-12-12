#!/bin/bash
#SBATCH --job-name=build_env
#SBATCH --output=slurm/log/build/%j.out
#SBATCH --error=slurm/log/build/%j.err
#SBATCH --time=24:00:00
#SBATCH --gpus=1
#SBATCH --cpus-per-gpu=8
#SBATCH --mem-per-gpu=40G
#SBATCH --container-image ghcr.io\#arslanardavic/graph-ml

set -euo pipefail

# Always start in the directory you ran `sbatch` from (the repo root)
cd "${SLURM_SUBMIT_DIR:-$PWD}"

# Ensure the log directory exists (under slurm/)
mkdir -p slurm/log/build

ENV_NAME="graph-found-env"

echo "Using system Python from container:"
which python
python --version

# Create venv
python -m venv "$ENV_NAME"

# Activate venv
source "$ENV_NAME/bin/activate"

# Ensure venv uses same packages as system python
pip install --upgrade pip

# Reinstall requirements to make venv self-contained
pip install -r /app/requirements.txt

# Optional: freeze for reproducibility
pip freeze > "${ENV_NAME}.freeze.txt"

# Pack environment
tar -czf "${ENV_NAME}.tar.gz" "$ENV_NAME"

# Copy artifacts to submit directory
cp "${ENV_NAME}.tar.gz" "${ENV_NAME}.freeze.txt" "$SLURM_SUBMIT_DIR/"

echo "DONE"
echo "Artifacts:"
echo "  $SLURM_SUBMIT_DIR/${ENV_NAME}.tar.gz"