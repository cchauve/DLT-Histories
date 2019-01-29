#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --account=rrg-chauvec
#SBATCH --output /home/chauvec/wg-anoph/COUNTING_TREES/DLT-Histories/exp/29-01-2019-exp1-redone-2/traces/solve_systems.trace
#SBATCH --error  /home/chauvec/wg-anoph/COUNTING_TREES/DLT-Histories/exp/29-01-2019-exp1-redone-2/traces/solve_systems.error

for K in {3..32}
do
    echo ${K}
    python3.6 src/solve_systems.py ./systems/exp1a_${K}_add1_sys src/
    python3.6 src/${K}_solver.py > systems/exp1a_${K}_asy
done
