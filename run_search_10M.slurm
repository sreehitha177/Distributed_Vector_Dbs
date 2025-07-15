#!/bin/bash
#SBATCH --job-name=search_10M
#SBATCH --output=logs/search_10M_%j.out
#SBATCH --error=logs/search_10M_%j.err
#SBATCH --partition=defq
#SBATCH --time=01:00:00
#SBATCH --mem=32G
#SBATCH --cpus-per-task=4

# Load your environment
source ~/work1/single_host_search/venv/bin/activate

# Optional: set OpenMP threads
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

# Run the search script
python search.py

