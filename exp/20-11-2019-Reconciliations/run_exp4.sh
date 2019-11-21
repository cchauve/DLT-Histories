#!/bin/bash
#SBATCH --time=48:00:00
#SBATCH --mem=8000M
#SBATCH --account=rrg-chauvec
#SBATCH --output /home/chauvec/wg-anoph/COUNTING_TREES_v2/DLT-Histories/exp/20-11-2019-Reconciliations/traces/exp_4.trace
#SBATCH --error  /home/chauvec/wg-anoph/COUNTING_TREES_v2/DLT-Histories/exp/20-11-2019-Reconciliations/traces/exp_4.error

cd /home/chauvec/wg-anoph/COUNTING_TREES_v2/DLT-Histories/exp/20-11-2019-Reconciliations/src

python exp4_sampling.py UDL  HIST
python exp4_sampling.py UDLT HIST
python exp4_sampling.py RDL  HIST
python exp4_sampling.py RDLT HIST

python exp4_sampling.py UDL  REC
python exp4_sampling.py UDLT REC
python exp4_sampling.py RDL  REC
python exp4_sampling.py RDLT REC
