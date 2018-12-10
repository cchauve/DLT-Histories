#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --account=rrg-chauvec
#SBATCH --output /home/chauvec/wg-anoph/COUNTING_TREES/DLT-Histories/exp/06-12-2018-exp1/traces/exp1a.trace
#SBATCH --error  /home/chauvec/wg-anoph/COUNTING_TREES/DLT-Histories/exp/06-12-2018-exp1/traces/exp1a.error

cd src
python2.7  main_exp1.py 3 64 100 100 128 20 ../results/exp1a.txt
cd ../
