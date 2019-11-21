# Sampling histories

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

    outputHistories       = open('../results/samples_H_'+str(k)+'_'+str(n)+'_'+model,'w')
    outputReconciliations = open('../results/samples_R_'+str(k)+'_'+str(n)+'_'+model,'w')
    
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

        # Histories
        Sh,Hh,Dh,Th = fillMatricesHist(stree,n,MODEL)

        for j in range(0,mn):
            history = randGenHist(stree,'H',n,Sh,Hh,Dh,Th,MODEL)
            nZ = {}
            for q in allLeaves:
                nZ[q] = history.count('Z'+str(q))
            strHistory = str(history)
            nD = strHistory.count('D')
            nL = strHistory.count('L')
            nT = strHistory.count('T')
            for q in allLeaves:                    
                output.write('Z'+str(q)+':'+str(nZ[q])+' ')
            outputHistories.write('D:'+str(nD)+' ')
            outputHistories.write('L:'+str(nL)+' ')
            outputHistories.write('T:'+str(nT)+'\n')

        # Reconciliations
        Sr,Hr,Dr,Tr = fillMatricesRec(stree,n,MODEL)

        for j in range(0,mn):
            reconciliation = randGenRec(stree,'H',n,Sr,Hr,Dr,Tr,MODEL)
            nZ = {}
            for q in allLeaves:
                nZ[q] = reconciliation.count('Z'+str(q))
            strReconciliation = str(reconciliation)
            nD = strReconciliation.count('D')
            nL = strReconciliation.count('L')
            nT = strReconciliation.count('T')
            for q in allLeaves:                    
                output.write('Z'+str(q)+':'+str(nZ[q])+' ')
            outputReconciliations.write('D:'+str(nD)+' ')
            outputReconciliations.write('L:'+str(nL)+' ')
            outputReconciliations.write('T:'+str(nT)+'\n')

    outputHistories.close()
    outputReconciliations.close()
