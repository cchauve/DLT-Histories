# Sampling histories and reconciliations

from trees   import *
from DLTcount import *

import math
import random

if __name__=="__main__":
    k   = 16    # size (#leaves) of considered trees
    n   = 30    # size of histories
    mk  = 50    # Number of random trees
    mn  = 10000 # Number of samples
    model   = sys.argv[1]
    objects = sys.argv[2]
    seed    = 101

    if model == 'UDL':
        MODEL  = {'D':True, 'L': True, 'T':False}
        ranked = False
    elif model == 'UDLT':
        MODEL = {'D':True, 'L': True, 'T':True}
        ranked = False
    elif model == 'RDL':
        MODEL  = {'D':True, 'L': True, 'T':False}
        ranked = True
    elif model == 'RDLT':
        MODEL = {'D':True, 'L': True, 'T':True}
        ranked = True
        
    random.seed(seed)

    if objects == 'HIST':
        output = open('../results/samples_H_'+str(k)+'_'+str(n)+'_'+model,'w')
    elif objects == 'REC':
        output = open('../results/samples_R_'+str(k)+'_'+str(n)+'_'+model,'w')
    
    for i in range(0,mk):    
        utree  = randomOrderedBinaryTree(k)
        labelTree(utree)
        output.write('# S_'+str(i)+'\t'+utree.asNewick())
        if ranked:
            (ranking,rtree) = rankTreeRandomly(utree)
            labelTree(rtree)
            output.write('\t'+str(ranking)+'\n')
            stree = rtree
        else:
            output.write('\n')
            stree = utree

        allLeaves = []
        allNodes  = stree.allNodes()
        for node in allNodes:
            if node.isLeaf():
                allLeaves.append(node.getID())

        if objects == 'HIST':
            S,H,D,T = fillMatricesHist(stree,n,MODEL)
        elif objects == 'REC':
            S,H,D,T = fillMatricesRec(stree,n,MODEL)
            
        for j in range(0,mn):
            if objects == 'HIST':
                hr = randGenHist(stree,'H',n,S,H,D,T,MODEL)
            elif objects == 'REC':
                hr = randGenRec(stree,'H',n,S,H,D,T,MODEL)
                
            nZ = {}
            for q in allLeaves:
                nZ[q] = hr.count('Z'+str(q))
            strHR = str(hr)
            nD = strHR.count('D')
            nL = strHR.count('L')
            nT = strHR.count('T')
            for q in allLeaves:                    
                output.write('Z'+str(q)+':'+str(nZ[q])+' ')
            output.write('D:'+str(nD)+' ')
            output.write('L:'+str(nL)+' ')
            output.write('T:'+str(nT)+'\n')

    output.close()
