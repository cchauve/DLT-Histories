#!/bin/bash
#SBATCH --time=48:00:00
#SBATCH --mem=8000M
#SBATCH --account=rrg-chauvec
#SBATCH --output /home/chauvec/wg-anoph/COUNTING_TREES/DLT-Histories/exp/20-02-2019-parsimony/traces/expUDL.trace
#SBATCH --error  /home/chauvec/wg-anoph/COUNTING_TREES/DLT-Histories/exp/20-02-2019-parsimony/traces/expUDL.error

cd src
python2.7 main.py 8 10 50 10000 False False ../results/samples_8_10_U_DL
python2.7 main.py 8 15 50 10000 False False ../results/samples_8_15_U_DL
python2.7 main.py 8 20 50 10000 False False ../results/samples_8_20_U_DL
python2.7 main.py 16 20 50 10000 False False ../results/samples_16_20_U_DL
python2.7 main.py 16 30 50 10000 False False ../results/samples_16_30_U_DL
cd ../results
gzip samples_8_10_U_DL
gzip samples_8_15_U_DL
gzip samples_8_20_U_DL
gzip samples_16_20_U_DL
gzip samples_16_30_U_DL
cd ../
