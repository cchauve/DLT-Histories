# Sampling and counting parsimonious histories

from trees   import *
from dpcount import *
from utils   import *

import math
import random

if __name__=="__main__":
    k      = int(sys.argv[1])
    n      = int(sys.argv[2])
    mk     = int(sys.argv[3]) # Number of random trees
    mn     = int(sys.argv[4]) # Number of samples
    hgt    = (sys.argv[5] == 'True')
    ranked = (sys.argv[6] == 'True')
    output = open(sys.argv[7],'w')
    s      = 101
    X      = 0.0000000001
    
    random.seed(s)

    for i in range(0,mk):    
        utree  = randomBinaryTree(k)
        labelTree(utree)
        output.write('# S_'+str(i)+'\t'+utree.asNewick())
        if ranked:
            (ranking,rtree) = rankTreeRandomly(utree)
            labelTree(rtree)
            output.write('\t'+str(ranking)+'\t')
            stree = rtree
        else:
            output.write('\t')
            stree = utree

        allLeaves = []
        allNodes  = stree.allNodes()
        for node in allNodes:
            if node.isLeaf():
                allLeaves.append(node.getID())
            
        S,H,D,T     = fillMatrices(stree,n,hgt,X)
        Sp,Hp,Dp,Tp = fillMatricesPars(stree,n,hgt)
        
        nbPars      = extractNbHistoriesMatrixPars(Hp,stree,n)[stree.getID()][n]
        scorePars   = extractScoresMatrixPars(Hp,stree,n)[stree.getID()][n]
        output.write('scorePars='+str(scorePars)+'\tnbPars='+str(nbPars)+'\n')
        
        for j in range(0,mn):
            history = randGen(stree,'H',n,S,H,D,T,hgt,X)
            nZ = {}
            for q in allLeaves:
                nZ[q] = history.count('Z'+str(q))
            strHistory = str(history)
            nD = strHistory.count('D')
            nL = strHistory.count('L')
            nT = strHistory.count('T')
            for q in allLeaves:              
                output.write('Z'+str(q)+':'+str(nZ[q])+' ')                
            output.write('D:'+str(nD)+' ')
            output.write('L:'+str(nL)+' ')
            output.write('T:'+str(nT)+'\n')
