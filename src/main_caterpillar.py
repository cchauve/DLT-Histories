from trees   import *
from dpcount import *
from utils   import *

def buildCaterpillar(k):
    if k==0:
        return Node()
    else:
        return Node([Node(),buildCaterpillar(k-1)])

# def buildTimedCaterpillar(k,h=None):
#     if h is None:
#         h=0
#     if k==0:
#         return Node([],-1,h)
#     else:
#         # Single branch
#         u = Node([],-1,h+k)
#         for i in range(h+k-1,h,-1):
#             u = Node([u],-1,i)
#         return Node([u,buildTimedCaterpillar(k-1,h+1)],-1,h)

if __name__=="__main__":
    #kmin = int(sys.argv[1]) # caterpillar min size
    #kmax = int(sys.argv[2]) # caterpillar max size
    #nmax = int(sys.argv[3]) # history max size    
    
    cat = buildCaterpillar(5)
    printTree(cat)
    catRanked = rankTreeRandomly(cat)

    rtree = newick2Tree("((3:1.3535,(7:0.6196,(9:1.1473,10:0.8569):0.6958):1.1001):0.6598,(2:1.3176,(6:1.5919,(5:0.6078,(1:0.5762,8:0.5574):0.6167):0.6960):0.9951):2.6870);")
    printTree(rtree)
