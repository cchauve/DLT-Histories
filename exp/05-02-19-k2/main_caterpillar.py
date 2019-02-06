# We look at counting results for a caterpillar species tree

from trees   import *
from dpcount import *
from utils   import *

import math
import random

def growth_constant(a,n):
    return(math.exp(math.log(math.pow(n,1.5)*a)/n))

if __name__=="__main__":
    k = int(sys.argv[1])
    n = int(sys.argv[2])
    s = int(sys.argv[3])
    
    random.seed(s)

    utree  = buildCaterpillar(k)
    labelTree(utree)
    print(utree.asNewick())
    (ranking,rtree) = rankTreeRandomly(utree)
    labelTree(rtree)
    print(ranking)
    print(rtree.asNewick())
    uS1,uH1,uD1,uT1 = fillMatrices(utree,n,False)
    uS2,uH2,uD2,uT2 = fillMatrices(utree,n,True)
    rS1,rH1,rD1,rT1 = fillMatrices(rtree,n,False)
    rS2,rH2,rD2,rT2 = fillMatrices(rtree,n,True)
    print('U,DL:\tn='+str(n)+'\t'+str(uH1[utree.getID()][n])+'\tgrowth constant='+str(growth_constant(uH1[utree.getID()][n],n)))
    print('U,DLT:\tn='+str(n)+'\t'+str(uH2[utree.getID()][n])+'\tgrowth constant='+str(growth_constant(uH2[utree.getID()][n],n)))
    print('R,DL:\tn='+str(n)+'\t'+str(rH1[rtree.getID()][n])+'\tgrowth constant='+str(growth_constant(rH1[rtree.getID()][n],n)))
    print('R,DLT:\tn='+str(n)+'\t'+str(rH2[rtree.getID()][n])+'\tgrowth constant='+str(growth_constant(rH2[rtree.getID()][n],n)))
