# Experiment 1. Addendum 3
# Generating a file with the Horton-Strahler number of each tree

from trees import *
import sys

if __name__=="__main__":
    exp1_dir     = sys.argv[1]
    output_dir   = sys.argv[2]

    for i in range(3,33):
        input_name1 = exp1_dir+'/exp1a_'+str(i)+'_asy'
        input_name2 = exp1_dir+'/exp1a_'+str(i)+'_add1'
        output_name = output_dir+'/exp1a_'+str(i)+'_hs'
        output = open(output_name,'w')
        output.write('#command line\t'+str(sys.argv)+'\n')
        output.write('#size_tree\ttree_index\ttree\tHortonStrahler number\tbalanced\tgrowth factor\n')
        output.flush()

        treesDict = {}
        exp1_stream2 = open(input_name2,'r').readlines()
        for l in exp1_stream2:
            if l[0] != '#':
                l1      = l.split('\t')
                treeId  = l1[1]
                treeStr = l1[2]
                treesDict[treeId] = treeStr
                
        exp1_stream1 = open(input_name1,'r').readlines()
        for l in exp1_stream1:
            if l[0] != '#':
                l1 = l.split('\t')
                treeId        = l1[1]
                growthFactor  = l1[2].rstrip()
                t             = newick2Tree(treesDict[treeId])
                labelTree(t)
                h             = computeHortonStrahler(t)
                b             = isBalanced(t)
                output.write(l1[0]+'\t'+l1[1]+'\t'+treesDict[treeId]+'\t'+str(h)+'\t'+str(b)+'\t'+growthFactor+'\n')
        output.flush()
        output.close()

