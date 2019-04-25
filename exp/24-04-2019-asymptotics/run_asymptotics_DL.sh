#!/bin/bash
#SBATCH --time=48:00:00
#SBATCH --account=rrg-chauvec
#SBATCH --output /home/chauvec/wg-anoph/COUNTING_TREES/DLT-Histories/exp/15-04-2019-asymptotics/traces/main_DL.trace
#SBATCH --error  /home/chauvec/wg-anoph/COUNTING_TREES/DLT-Histories/exp/15-04-2019-asymptotics/traces/main_DL.error

cd /home/chauvec/wg-anoph/COUNTING_TREES/DLT-Histories/exp/15-04-2019-asymptotics/src
for K in {3..16}
do
    echo ${K}
    python2.7 main_DL.py ../data/exp1a_${K}_add1_asy DL ../results/exp1a_${K}_DL_asy
done
