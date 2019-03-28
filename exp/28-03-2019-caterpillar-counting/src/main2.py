# Comparing growth rate of the caterpillar and complete binary tree

from trees   import *
from dpcount import *
from utils   import *

import math

def is_power2(num):
    return num != 0 and ((num & (num - 1)) == 0)

if __name__=="__main__":
    kMin       = int(sys.argv[1]) 
    kMax       = int(sys.argv[2]) 
    nMax       = int(sys.argv[3]) 
    out_file   = open(sys.argv[4],'w') # output file

    n=nMax
    out_file.write('#k\tcaterpillar estimated growth rate\tcomplete binary estimated growth rate\tratio caterpillar/complete\n')
    out_file.write('#Comment: growth rates are estimated as the ratio of the number of histories of size '+str(n)+' by the number of histories of size '+str(n-1)+'\n')
    for kexp in range(kMin,kMax+1):
        k = math.pow(2,kexp)
        caterpillarTree = buildCaterpillar(k)
        labelTree(caterpillarTree)
        completeTree = buildCompleteTree(kexp)
        labelTree(completeTree)
        
        S1,H1,D1,T1 = fillMatrices(caterpillarTree,nMax,{'D':True,'L':True,'T':False},1.0)
        S2,H2,D2,T2 = fillMatrices(completeTree,nMax,{'D':True,'L':True,'T':False},1.0)

        catRoot  = caterpillarTree.getID()
        compRoot = completeTree.getID()
        rateCaterpillar = H1[catRoot][nMax]/H1[catRoot][nMax-1]
        rateComplete    = H2[compRoot][nMax]/H2[compRoot][nMax-1]
        #rateCaterpillar = math.exp(math.log(math.pow(n,1.5)*H1[catRoot][n])/n)
        #rateComplete    = math.exp(math.log(math.pow(n,1.5)*H2[catRoot][n])/n)
        out_file.write(str(k)+'\t'+str(rateCaterpillar)+'\t'+str(rateComplete)+'\t'+str(rateCaterpillar/rateComplete)+'\n')
