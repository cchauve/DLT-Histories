#!/bin/bash
#SBATCH --time=48:00:00
#SBATCH --mem=8000M
#SBATCH --account=rrg-chauvec
#SBATCH --output /home/chauvec/wg-anoph/COUNTING_TREES_v2/DLT-Histories/exp/20-11-2019-Reconciliations/traces/exp_3.trace
#SBATCH --error  /home/chauvec/wg-anoph/COUNTING_TREES_v2/DLT-Histories/exp/20-11-2019-Reconciliations/traces/exp_3.error

cd /home/chauvec/wg-anoph/COUNTING_TREES_v2/DLT-Histories/exp/20-11-2019-Reconciliations/src/
python exp3_count_histories_reconciliations_ranked_trees.py
