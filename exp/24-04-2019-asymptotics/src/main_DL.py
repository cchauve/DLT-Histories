import sys
from asymptotics import *
import importlib

DATA_FILE = sys.argv[1]
TREES = []
TREES2INFO = {}
MODEL = sys.argv[2]
OUTPUT_FILE = sys.argv[3]

dataFile = open(DATA_FILE,'r').readlines()
outputFile = open(OUTPUT_FILE,'w')
for l in dataFile:
    if l[0] !='#':
        l1 = l.rstrip().split()
        k      = l1[0]
        treeID = l1[1]
        tree   = l1[2]
        t = newick2Tree(tree)
        labelTree(t)
        s = t.asNewick()
        (sysEqs,sysVars) = getSystem(t,MODEL={'D':True,'L':True,'T':False})
        solveSystem(sysEqs,sysVars,MODEL+'_'+k+'_'+treeID)
        tmp_solver = importlib.import_module('tmp_solver_'+MODEL+'_'+k+'_'+treeID, package=None)
        outputFile.write(s+'\t'+str(tmp_solver.SOL)+'\n')
outputFile.close()

