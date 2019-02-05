# Experiment 1. 
# We read already generated trees in a range size (kMin=argv[1],kMax=argv[2])
# The trees are stored in files /home/chauvec/wg-anoph/COUNTING_TREES/DLT-Histories/exp/01-02-2019-exp1-ranking//data/exp1a_k_add1 where k is the size
# For each size we generate nbTrees=argv[3] trees
# The first tree is always the caterpillar
# If k is a power of 2 the second tree is the complete binary tree
# The other trees are random binary trees
# For each tree we generate nbRankings=argv[4] random rankings
# For each configuration we generate histories in the size range (1,nMax=argv[5])
# We specify the random seed=argv[6] and the output file=argv[7]

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
    nbRankings = int(sys.argv[4]) # number of rankings per tree
    nMax       = int(sys.argv[5]) # history max size (#leaves)    
    seed       = int(sys.argv[6]) # random seed
    out_file   = sys.argv[7]      # output file

    random.seed(seed)

    print "Reading trees",
    TREES  = {}
    PREFIX = "/home/chauvec/wg-anoph/COUNTING_TREES/DLT-Histories/exp/01-02-2019-exp1-ranking/data/" 
    for k in range(kMin,kMax+1):
        print " "+str(k),
        TREES[k]  = {}
        tree_file = open(PREFIX+"exp1a_"+str(k)+"_add1","r").readlines()
        for l in tree_file:
            if l[0] != "#":
                l1 = l.rstrip().split("\t")
                tree     = newick2Tree(l1[2])
                idxTrees = int(l1[1])
                labelTree(tree)
                TREES[k][idxTrees]={0:tree}

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
            for r in range(1,nbRankings+1):
                s1 = str(k)+"\t"+str(i)+"\tR\tDL\t"+unrankedTree.asNewick()+" "
                s2 = str(k)+"\t"+str(i)+"\tR\tDLT\t"+unrankedTree.asNewick()+" "
                (ranking,rankedTree) = rankTreeRandomly(unrankedTree)
                rankingStr = printRanking(ranking)
                s1 += rankingStr+"\t"
                s2 += rankingStr+"\t"
                for n in range(1,nMax+1):
                    S1,H1,D1,T1 = fillMatrices(rankedTree,n,False)
                    nbHistories1 = int(H1[rankedTree.getID()][n])
                    s1 += str(nbHistories1)+" "
                    S2,H2,D2,T2 = fillMatrices(rankedTree,n,True)
                    nbHistories2 = int(H2[rankedTree.getID()][n])
                    s2 += str(nbHistories2)+" "
                output.write(s1+"\n")
                output.write(s2+"\n")
                output.flush()
                print
        output.close()
