# Experiment 3. 
# Counting histories and reconciliations for ranked species trees, where 10 random rankings are generated per tree

from trees   import *
from DLTcount import *
import random

if __name__=="__main__":
    kMin       = 3   # min size (#leaves) of considered trees
    kMax       = 25  # max size (#leaves) of considered trees
    nbTrees    = 100 # number of trees per size
    nMax       = 50  # max history size
    nbRankings = 10  # random ranking per trees
    seed       = 20  # random seed
    inputPrefix = '../results/trees' 
    outputPrefix = '../results/ranked' # output file

    random.seed(seed)

    # Reading trees
    TREES = {}
    for k in range(kMin,kMax+1):
        TREES[k] = {}
        inputFile = open(inputPrefix+'_'+str(k)).readlines()
        for line in inputFile:
            if line[0] != "#":
                line1 = line.rstrip().split('\t')
                size   = line1[0]
                treeID = int(line1[1])
                tree   = newick2Tree(line1[2])
                TREES[k][treeID] = tree
                
    # Counting DL and DLT histories and reconciliations
    for k in TREES.keys():
        output = open(outputPrefix+"_"+str(k),"w")
        output.write("#size_tree\ttree_index\thistory/reconciliation\tranking_type\tDL/DLT\ttree/ranking\tnumber_of_histories/reconciliations\n")
        output.flush()
        for i in range(0,nbTrees):
            unrankedTree = TREES[k][i]
            labelTree(unrankedTree)
            for r in range(1,nbRankings+1):
                (ranking,rankedTree) = rankTreeRandomly(unrankedTree)
                rankingStr = printRanking(ranking) 
                hs1 = str(k)+"\t"+str(i)+"\tH\tU\tDL\t"+unrankedTree.asNewick()+" "
                hs2 = str(k)+"\t"+str(i)+"\tH\tU\tDLT\t"+unrankedTree.asNewick()+" "
                hs1 += rankingStr+"\t"
                hs2 += rankingStr+"\t"
                for n in range(1,nMax+1):
                    hS1,hH1,hD1,hT1 = fillMatricesHist(rankedTree,n,MODEL={'D':True,'L':True,'T':False},)
                    nbHistories1 = int(hH1[rankedTree.getID()][n],)
                    hs1 += str(nbHistories1)+" "
                    hS2,hH2,hD2,hT2 = fillMatricesHist(rankedTree,n,MODEL={'D':True,'L':True,'T':True})
                    nbHistories2 = int(hH2[rankedTree.getID()][n])
                    hs2 += str(nbHistories2)+" "
                output.write(hs1+"\n")
                output.write(hs2+"\n")
                output.flush()
                
                rs1 = str(k)+"\t"+str(i)+"\tR\tU\tDL\t"+unrankedTree.asNewick()+" "
                rs2 = str(k)+"\t"+str(i)+"\tR\tU\tDLT\t"+unrankedTree.asNewick()+" "
                rs1 += rankingStr+"\t"
                rs2 += rankingStr+"\t"
                for n in range(1,nMax+1):
                    rS1,rH1,rD1,rT1 = fillMatricesRec(rankedTree,n,MODEL={'D':True,'L':True,'T':False},)
                    nbReconciliations1 = int(rH1[rankedTree.getID()][n],)
                    rs1 += str(nbReconciliations1)+" "
                    rS2,rH2,rD2,rT2 = fillMatricesRec(rankedTree,n,MODEL={'D':True,'L':True,'T':True})
                    nbReconciliations2 = int(rH2[rankedTree.getID()][n])
                    rs2 += str(nbReconciliations2)+" "
                output.write(rs1+"\n")
                output.write(rs2+"\n")
                output.flush()                
        output.close()
