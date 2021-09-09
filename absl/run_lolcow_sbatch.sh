#!/bin/bash
#SBATCH -p gpu
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-gpu=12
#SBATCH --mem-per-cpu=40G
#SBATCH --time=1:00:00

echo $SLURM_NODELIST
echo $TMPDIR

module load python/gcc

cp external_runscript.sh $TMPDIR
mkdir $TMPDIR/fakedata
ls -l $TMPDIR/fakedata
./run_lolcow.py
