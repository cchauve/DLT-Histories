# Experiment 1. Addendum 1
# Generating a file with the tree formatted for Michael's program syntax

from trees import *
import sys
import gzip

if __name__=="__main__":
    exp1_results = sys.argv[1] # results of experiment 1, assumed to be gzipped

    output = open(exp1_results.replace('.gz','_add1'),'w')
    output.write('#command line\t'+str(sys.argv)+'\n')
    output.write('#size_tree\ttree_index\ttree\treformatted tree\n')
    output.flush()
    
    with gzip.open(exp1_results, 'rb') as f:
        exp1_stream = f.readlines()
    for l in exp1_stream:
        if l[0] != '#':
            l1 = l.split('\t')
            if l1[3] == 'DL':
                newickTree    = l1[4]
                t             = newick2Tree(newickTree)
                subtreeLabels = computeUniqueSubtrees(t)
                output.write(l1[0]+'\t'+l1[1]+'\t'+newickTree+'\t')
                output.write('[')
                nbSubtrees = len(subtreeLabels)
                for i in range(0,nbSubtrees-1):
                    output.write(str(subtreeLabels[i])+',')
                output.write(str(subtreeLabels[i+1])+']\n')
    output.flush()
    output.close()
            
