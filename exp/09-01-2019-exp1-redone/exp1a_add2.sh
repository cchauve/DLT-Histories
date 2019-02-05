#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --mem=8000M
#SBATCH --account=rrg-chauvec
#SBATCH --output /home/chauvec/wg-anoph/COUNTING_TREES/DLT-Histories/exp/09-01-2019-exp1-redone/traces/exp1a_add2.trace
#SBATCH --error  /home/chauvec/wg-anoph/COUNTING_TREES/DLT-Histories/exp/09-01-2019-exp1-redone/traces/exp1a_add2.error

for k in {3..32}
do
    python2.7 src/main_exp1_add2.py results/exp1a_${k}.gz 
done

