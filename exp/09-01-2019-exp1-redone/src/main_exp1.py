# Experiment 1. 
# We generate trees in a range size (kMin=argv[1],kMax=argv[2])
# For each size we generate nbTrees=argv[3] trees
# The first tree is always the caterpillar
# If k is a power of 2 the second tree is the complete binary tree
# The other trees are random binary trees
# For each configuration we generate histories in the size range (1,nMax=argv[4])
# We specify the random seed=argv[5] and the output file=argv[6]

from trees   import *
from dpcount import *
from utils   import *

import math
import random

def is_power2(num):
    return num != 0 and ((num & (num - 1)) == 0)

if __name__=="__main__":
    kMin       = int(sys.argv[1]) # min size (#leaves) of considered trees
    kMax       = int(sys.argv[2]) # max size (#leaves) of considered trees
    nbTrees    = int(sys.argv[3]) # number of trees per size
    nMax       = int(sys.argv[4]) # history max size (#leaves)    
    seed       = int(sys.argv[5]) # random seed
    out_file   = sys.argv[6]      # output file

    random.seed(seed)

    print "Generating trees",
    TREES       = {}
    for k in range(kMin,kMax+1):
        print " "+str(k),
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
            randomTree = randomBinaryTree(k)
            labelTree(randomTree)
            TREES[k][i] = {0:randomTree}

    print 

    print "Counting trees "
    for k in TREES.keys():
        output = open(out_file+"_"+str(k),"w")
        output.write("#command line\t"+str(sys.argv)+"\n")
        output.write("#size_tree\ttree_index\tranking_type\tDL/DLT\ttree/ranking\tnumber_of_histories\n")
        output.flush()
        print "--> "+str(k)
        for i in range(0,nbTrees):
            print "----> tree "+str(i),
            unrankedTree = TREES[k][i][0]
            s1 = str(k)+"\t"+str(i)+"\tU\tDL\t"+unrankedTree.asNewick()+"\t"
            s2 = str(k)+"\t"+str(i)+"\tU\tDLT\t"+unrankedTree.asNewick()+"\t"
            for n in range(1,nMax+1):
                S1,H1,D1,T1 = fillMatrices(unrankedTree,n,False)
                nbHistories1 = int(H1[unrankedTree.getID()][n])
                s1 += str(nbHistories1)+" "
                S2,H2,D2,T2 = fillMatrices(unrankedTree,n,True)
                nbHistories2 = int(H2[unrankedTree.getID()][n])
                s2 += str(nbHistories2)+" "
            output.write(s1+"\n")
            output.write(s2+"\n")
            output.flush()
            print
        output.close()
