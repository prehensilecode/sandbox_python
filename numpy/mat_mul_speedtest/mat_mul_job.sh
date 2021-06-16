#!/bin/bash
#SBATCH -n 1
#SBATCH --cpus-per-task=48
#SBATCH --time=0:15:00
#SBATCH --mem=32G

#module load python/anaconda3
module load python/gcc/3.9.1
which python3

python3 mat_mul.py

