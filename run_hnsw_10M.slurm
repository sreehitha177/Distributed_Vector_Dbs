#!/bin/bash
#SBATCH --job-name=hnsw_10M
#SBATCH --output=logs/hnsw_10M_%j.out
#SBATCH --error=logs/hnsw_10M_%j.err
#SBATCH --time=04:00:00
#SBATCH --partition=defq
#SBATCH --mem=64G
#SBATCH --cpus-per-task=8

# Load your environment
source ~/work1/single_host_search/venv/bin/activate

# Optional: Use all available threads
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

# Run your indexing and/or search script
python hnsw_index.py

