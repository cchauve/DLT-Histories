from trees   import *
from dpcount import *
from utils   import *

if __name__=="__main__":    
    t = randomBinaryTree(5)
    (times,tr) = rankTreeRandomly(t)
    print tree2Newick(t)
    print(times)
    print tree2Newick(tr)
