from trees   import *
from dpcount import *
from utils   import *
import math

def is_power2(num):
    return num != 0 and ((num & (num - 1)) == 0)

if __name__=="__main__":
    kmin    = int(sys.argv[1]) # min size (#leaves) of considered trees
    kmax    = int(sys.argv[2]) # max size (#leaves) of considered trees
    nbtrees = int(sys.argv[3]) # number of random trees per size
    nmax    = int(sys.argv[4]) # history max size (#leaves)    

    TREES = {}
    for k in range(kmin,kmax+1):
        TREES[k] = []
        cat = buildCaterpillar(k)
        labelTree(cat)
        TREES[k].append(cat)
        if is_power2(k):
            comptree = buildCompleteTree(int(math.log(k,2)))
            labelTree(comptree)
            TREES[k].append(comptree)
        for i in range(1,nbtrees+1):
            TREES[k].append(randomBinaryTree(k))
            
    for k in TREES.keys():
        for t in TREES[k]:
            print str(k)+"\t"+t.asNewick()
