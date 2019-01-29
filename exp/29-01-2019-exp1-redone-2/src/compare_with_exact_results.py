#!/usr/bin/env python

"""compare_with_exact_results.py: compare asymptotics based on exponential growth factor with exact counting data."""
"""input format: model (DL/DLT); exact results file (gzipped); asymptotic results file"""
"""output: for each tree sequence of the rations exact/asymptotic"""

__author__  = "Cedric Chauve"
__date__    = "January 29, 2019"

import sys
import gzip
import io
import csv
import math

MODEL = sys.argv[1]

# Exact results
exact_file = sys.argv[2]
EXACT = {}
with gzip.open(exact_file, 'r') as f:
    exact_data = csv.reader(io.TextIOWrapper(f, newline=""),delimiter='\t')
    for l in exact_data:
        if l[0][0] != "#":
            size = l[0]
            tree = l[1]
            if l[3] == MODEL:
                EXACT[tree] = l[5].rstrip().split()

# Asymptotics results
asymptotics_data = open(sys.argv[3],'r').readlines()
ASYMPT = {}
for l in asymptotics_data:
    if l[0] != "#":
        l1   = l.rstrip().split('\t')
        tree = l1[1]
        ASYMPT[tree] = float(l1[4])

# Comparison
RATIOS = {}
for tree in EXACT.keys():
    RATIOS[tree] = {}
    counting_seq = EXACT[tree]    
    factor       = ASYMPT[tree]
    nmax = len(counting_seq)
    for n in range(0,nmax):
        nb1 = float(counting_seq[n])
        nb2 = math.pow(factor,n+1)/math.pow((n+1),1.5)
        RATIOS[tree][n] = nb1/nb2
        
# Output
output = open(sys.argv[4],'w')
for tree in RATIOS.keys():
    output.write(size+'\t'+tree+'\t'+'U\t'+MODEL+'\t')
    for n in range(0,len(RATIOS[tree])):
        output.write(str(RATIOS[tree][n])+' ')
    output.write('\n')
