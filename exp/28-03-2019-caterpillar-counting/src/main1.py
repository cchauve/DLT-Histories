# We consider the caterpillar tree and generate the countig sequence 

from trees   import *
from dpcount import *
from utils   import *

import math

def is_power2(num):
    return num != 0 and ((num & (num - 1)) == 0)

if __name__=="__main__":
    kMin       = int(sys.argv[1]) # min size (#leaves) of considered trees
    kMax       = int(sys.argv[2]) # max size (#leaves) of considered trees
    nMax       = int(sys.argv[3]) # history max size (#leaves)    
    out_file   = open(sys.argv[4],'w') # output file
    
    CAT = {k: {n: 0 for n in  range(1,nMax+1)} for k in range(kMin,kMax+1)}
    
    caterpillar = buildCaterpillar(kMax)
    labelTree(caterpillar)
    catNodes = {}
    for node in caterpillar.allNodes():
        catNodes[node.getHeight()] = node.getID()

    S1,H1,D1,T1 = fillMatrices(caterpillar,nMax,{'D':True,'L':True,'T':False},1.0)
    for k in range(kMin,kMax+1):
        for n in range(1,nMax+1):
            CAT[k][n] = int(H1[catNodes[k-1]][n])

    seq = '#k/n\t'
    for n in range(1,nMax+1):
        seq+=str(n)+','
    seq+='\n'
    out_file.write(seq.replace(',\n','\n'))
    for k in range(kMin,kMax+1):
        seq=str(k)+'\t'
        for n in range(1,nMax+1):
            seq+=str(CAT[k][n])+','
        seq+='\n'
        out_file.write(seq.replace(',\n','\n'))
            
    #if is_power2(k):
    #    completeTree = buildCompleteTree(int(math.log(k,2)))
