#!/bin/bash
#SBATCH --time=48:00:00
#SBATCH --mem=20G
#SBATCH --account=rrg-chauvec
#SBATCH --output /home/chauvec/wg-anoph/COUNTING_TREES/DLT-Histories/exp/24-04-2019-asymptotics/traces/main_DL.trace
#SBATCH --error  /home/chauvec/wg-anoph/COUNTING_TREES/DLT-Histories/exp/24-04-2019-asymptotics/traces/main_DL.error

cd /home/chauvec/wg-anoph/COUNTING_TREES/DLT-Histories/exp/24-04-2019-asymptotics/src
for K in {3..25}
do
    echo ${K}
    python2.7 main_DL.py ../data/trees_${K} DL ../results/asymptotics_${K}_DL
done
