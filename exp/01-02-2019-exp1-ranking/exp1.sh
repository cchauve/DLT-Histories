#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --mem=8000M
#SBATCH --account=rrg-chauvec
#SBATCH --output /home/chauvec/wg-anoph/COUNTING_TREES/DLT-Histories/exp/01-02-2019-exp1-ranking/traces/exp1.trace
#SBATCH --error  /home/chauvec/wg-anoph/COUNTING_TREES/DLT-Histories/exp/01-02-2019-exp1-ranking/traces/exp1.error

cd src
python2.7  main_exp1.py 3 32 100 10 50 20 ../results/exp1
cd ../results
gzip exp1_*
cd ../
