# We look at counting results for a species tree of size 2

from trees   import *
from dpcount import *
from utils   import *

import math
import random

def growth_constant(a,n):
    return(math.exp(math.log(math.pow(n,1.5)*a)/n))

if __name__=="__main__":
    k = 2
    n = int(sys.argv[1])
    m = int(sys.argv[2]) # Number of samples
    s = int(sys.argv[3])
    tosample = (sys.argv[4] == 'True')
    toprint  = (sys.argv[5] == 'True')
    
    random.seed(s)

    utree  = buildCompleteTree(1)
    labelTree(utree)
    print(utree.asNewick())
    (ranking,rtree) = rankTreeRandomly(utree)
    labelTree(utree)
    print(ranking)
    print(rtree.asNewick())
    uS1,uH1,uD1,uT1 = fillMatrices(utree,n,False)
    uS2,uH2,uD2,uT2 = fillMatrices(utree,n,True)
    rS1,rH1,rD1,rT1 = fillMatrices(rtree,n,False)
    rS2,rH2,rD2,rT2 = fillMatrices(rtree,n,True)
    print('U,DL:\tn='+str(n)+'\t'+str(uH1[utree.getID()][n])+'\tgrowth constant='+str(growth_constant(uH1[utree.getID()][n],n)))
    print('U,DLT:\tn='+str(n)+'\t'+str(uH2[utree.getID()][n])+'\tgrowth constant='+str(growth_constant(uH2[utree.getID()][n],n)))
    print('R,DL:\tn='+str(n)+'\t'+str(rH1[rtree.getID()][n])+'\tgrowth constant='+str(growth_constant(rH1[utree.getID()][n],n)))
    print('R,DLT:\tn='+str(n)+'\t'+str(rH2[rtree.getID()][n])+'\tgrowth constant='+str(growth_constant(rH2[utree.getID()][n],n)))

    if tosample:
        print('Sampling u,DL histories')
        histories_UDL = []
        for i in range(0,m):
            history = randGen(utree,"H",n,uS1,uH1,uD1,uT1)
            if history not in histories_UDL:
                histories_UDL.append(history)
        print('There are '+str(len(histories_UDL))+' histories')
        if toprint:
            for h in histories_UDL:
                print(h)
