#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --mem=8000M
#SBATCH --account=rrg-chauvec
#SBATCH --output /home/chauvec/wg-anoph/COUNTING_TREES/DLT-Histories/exp/09-01-2019-exp1-redone/traces/exp1a.trace
#SBATCH --error  /home/chauvec/wg-anoph/COUNTING_TREES/DLT-Histories/exp/09-01-2019-exp1-redone/traces/exp1a.error

cd src
python2.7  main_exp1.py 3 32 100 50 20 ../results/exp1a
cd ../results
gzip exp1a_*
cd ../
