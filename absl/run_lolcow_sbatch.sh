#!/bin/bash
#SBATCH -p gpu
#SBATCH --gres=gpu:2
#SBATCH --cpus-per-gpu=12
#SBATCH --mem-per-cpu=40G
#SBATCH --time=1:00:00

env | grep ^SLURM | sort
echo $TMPDIR
nvidia-smi

module load python/gcc

cp external_runscript.sh $TMPDIR
mkdir $TMPDIR/fakedata
ls -l $TMPDIR/fakedata

if [[ ${SLURM_JOB_PARTITION} = "gpu" ]]
then
    args="--use_gpu"
else
    args=""
fi

./run_lolcow.py $args

