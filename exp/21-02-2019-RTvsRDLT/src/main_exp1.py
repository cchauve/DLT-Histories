# Experiment 1. 
# We generate trees in a range size (kMin=argv[1],kMax=argv[2])
# For each size we generate nbTrees=argv[3] trees
# The first tree is always the caterpillar
# If k is a power of 2 the second tree is the complete binary tree
# The other trees are random binary trees
# For each tree, we consider it as unranked and then generate nbRankings=argv[4] random rankings
# For each configuration we generate histories in the size range (1,nMax=argv[5])
# We specify the random seed=argv[6] and the output file=argv[7]

from trees   import *
from dpcount import *
from utils   import *

import math
import random

def is_power2(num):
    return num != 0 and ((num & (num - 1)) == 0)

def ranking2String(ranking):
    strRanking = ""
    for i in ranking.keys():
        strRanking += str(i)+":"+str(ranking[i])+"."
    return strRanking

if __name__=="__main__":
    kMin       = int(sys.argv[1]) # min size (#leaves) of considered trees
    kMax       = int(sys.argv[2]) # max size (#leaves) of considered trees
    nbTrees    = int(sys.argv[3]) # number of trees per size
    nbRankings = int(sys.argv[4]) # number of rankings per tree
    nMax       = int(sys.argv[5]) # history max size (#leaves)    
    seed       = int(sys.argv[6]) # random seed
    out_file   = sys.argv[7]      # output file

    output = open(out_file,"w")
    output.write("#command line\t"+str(sys.argv)+"\n")
    output.write("#size_tree\ttree_index\tranking_type\ttree/ranking\tnumber_of_histories\n")
    random.seed(seed)
    
    TREES       = {}
    for k in range(kMin,kMax+1):
        TREES[k] = {}
        caterpillar = buildCaterpillar(k)
        labelTree(caterpillar)
        idxTrees = 0
        TREES[k][idxTrees]={0:caterpillar}
        idxTrees += 1
        if is_power2(k):
            completeTree = buildCompleteTree(int(math.log(k,2)))
            labelTree(completeTree)
            TREES[k][idxTrees]={0:completeTree}
            idxTrees += 1
        for i in range(idxTrees,nbTrees):
            TREES[k][i] = {0:randomBinaryTree(k)}
            
        for i in range(0,nbTrees):
            unrankedTree = TREES[k][i][0]
            for r in range(1,nbRankings+1):
                TREES[k][i][r] = rankTreeRandomly(unrankedTree)
            
    for k in TREES.keys():
        for i in range(0,nbTrees):
            unrankedTree = TREES[k][i][0]
            s = str(k)+"\t"+str(i)+"\tU\t"+unrankedTree.asNewick()+"\t"
            for n in range(1,nMax+1):
                S,H,D,T = fillMatrices(unrankedTree,n,False)
                nbHistories = int(H[unrankedTree.getID()][n])
                s += str(nbHistories)+" "
            output.write(s+"\n")
            for r in range(1,nbRankings+1):
                [ranking,rankedTree] = TREES[k][i][r]
                s = str(k)+"\t"+str(i)+"\tR\t"+ranking2String(ranking)+"\t"
                for n in range(1,nMax+1):
                    S,H,D,T = fillMatrices(rankedTree,n,False)
                    nbHistories = int(H[rankedTree.getID()][n])
                    s += str(nbHistories)+" "
                output.write(s+"\n")
