__author__  = "Cedric Chauve, Yann Ponty, Michael Wallner"
__date__    = "November 20, 2019"

# Algorithms to count DLT-histories and DLT-reconciliations for a given species tree

from trees import *

# ---------------------------------------------------------------------------
# Functions counting the number of ways an event can occur
def Ext(u): # Extant leaf
    return(1.0)
def Loss(u): # Gene loss
    return(1.0)
def Dup(u): # Gene duplication
    return(1.0)
def HGT(u,v): # Horizontal Gene Transfer
    return(1.0)
# Functions to print evolutionary events
def ExtLbl(u):
    return("Z%s"%(u.getID()))
def LossLbl(u):
    return("L%s"%(u.getID()))
def DupLbl(u):
    return("D%s"%(u.getID()))
def HGTLbl(u,v):
    return("T%s->%s"%(u.getID(),v.getID()))

# ---------------------------------------------------------------------------
# Counting histories

# Filling the DP matrix counting the number of histories per size and per subtree
# X: parameter aimed at skewing the uniform distribution for sampling
# X < 1: parsimonious histories are more likely to be sampled
# X > 1: non-parsimonious histories are more likely to be sampled
# The same value of X should be used in filleMatrices and randGen
# MODEL specifies the evolutionary model
def fillMatricesHist(tree,N,MODEL={'D':True,'L':True,'T':False},X=1.0):

    nodes = tree.allNodes()

    S = [[0 for n in range(N+1)] for u in nodes]
    H = [[0 for n in range(N+1)] for u in nodes]
    D = [[0 for n in range(N+1)] for u in nodes]
    T = [[0 for n in range(N+1)] for u in nodes]

    for n in range(1,N+1):
        for u in nodes:
            i = u.getID()
            if MODEL['D']:
                for m in range(1,n):
                    D[i][n] += H[i][n-m]*H[i][m]*Dup(u)*X
            if MODEL['T']:
                if u.getTime() >= 0:
                    receivers = u.getContemporary()
                else:
                    receivers = u.getIncomparable()
                for v in receivers:
                    j = v.getID()
                    for m in range(1,n):
                        T[i][n] += H[i][n-m]*H[j][m]*HGT(u,v)*X
            if u.isLeaf():
                if n==1:
                    H[i][n] = Ext(u)
                else: # => n>1
                    H[i][n] = D[i][n] + T[i][n]
            else: # => n ancestor
                if u.isBinary():
                    l,r = u.getLeft(),u.getRight()
                    lid,rid= l.getID(),r.getID()
                    if MODEL['L']:
                        S[i][n] = X*(Loss(l)*H[rid][n] + Loss(r)*H[lid][n])
                    for m in range(1,n):
                        S[i][n] += H[lid][n-m]*H[rid][m]
                if u.isUnary():
                    c   = u.getChild()
                    cid = c.getID()
                    S[i][n] = H[cid][n]
                    
                H[i][n] = D[i][n] + S[i][n] + T[i][n]

    return(S,H,D,T)

# ---------------------------------------------------------------------------
# Counting reconciliations

def fillMatricesRec(tree,N,MODEL={'D':True,'L':True,'T':False},X=1.0):

    nodes = tree.allNodes()

    S = [[0 for n in range(N+1)] for u in nodes]
    H = [[0 for n in range(N+1)] for u in nodes]
    D = [[0 for n in range(N+1)] for u in nodes]
    T = [[0 for n in range(N+1)] for u in nodes]

    for n in range(1,N+1):
        for u in nodes:
            i = u.getID()
            if MODEL['D']:
                for m in range(1,n):
                    D[i][n] += 0.5*H[i][n-m]*H[i][m]*Dup(u)*X
                    if n%2==0:
                        D[i][n] += 0.5*H[i][int(n/2)]*Dup(u)*X
            if MODEL['T']:
                if u.getTime() >= 0:
                    receivers = u.getContemporary()
                else:
                    receivers = u.getIncomparable()
                for v in receivers:
                    j = v.getID()
                    for m in range(1,n):
                        T[i][n] += H[i][n-m]*H[j][m]*HGT(u,v)*X
            if u.isLeaf():
                if n==1:
                    H[i][n] = Ext(u)
                else: # => n>1
                    H[i][n] = D[i][n] + T[i][n]
            else: # => n ancestor
                if u.isBinary():
                    l,r = u.getLeft(),u.getRight()
                    lid,rid= l.getID(),r.getID()
                    if MODEL['L']:
                        S[i][n] = X*(Loss(l)*H[rid][n] + Loss(r)*H[lid][n])
                    for m in range(1,n):
                        S[i][n] += H[lid][n-m]*H[rid][m]
                if u.isUnary():
                    c   = u.getChild()
                    cid = c.getID()
                    S[i][n] = H[cid][n]
                    
                H[i][n] = D[i][n] + S[i][n] + T[i][n]

    return(S,H,D,T)

# ---------------------------------------------------------------------------

USAGE = 'DLTcount <tree> <MODEL> <n>\n'+'tree = random k | rrandom k | caterpillar k | rcaterpillar k | complete h | rcomplete h | newick string\n'+'\trandom k = random binary tree with k leaves\n'+'\trrandom k = randomly ranked random binary tree with k leaves\n'+'\tcaterpillar k = caterpillar with k leaves\n'+'\trcaterpillar k = randomly ranked caterpillar with k leaves\n'+'\tcomplete h = complete binary tree with 2^h leaves\n'+'\trcomplete h = randomly ranked complete binary tree with 2^h leaves\n'+'\tnewick string = string is the Newick representation of a tree\n'+'MODEL = DL | DLT\n'+'n = history size\n'

def getTree(s1,s2):
    if s1 == 'newick':
        tree = newick2Tree(s2)
        labelTree(tree)
        return(tree)
    
    if not s2.isdigit():
        print(USAGE)
        sys.exit()
    else:
        k = int(s2)                
        if s1 == 'random':
            tree = randomOrderedBinaryTree(k)
        elif s1 == 'caterpillar':
            tree = buildCaterpillar(k)
        elif s1 == 'complete':
            tree = buildCompleteTree(k)
        elif s1 == 'rrandom':
            tree_aux = randomOrderedBinaryTree(k)
            (ranking,tree) = rankTreeRandomly(tree_aux)
        elif s1 == 'rcaterpillar':
            tree_aux = buildCaterpillar(k)
            (ranking,tree) = rankTreeRandomly(tree_aux)
        elif s1 == 'rcomplete':
            tree_aux = buildCompleteTree(k)
            (ranking,tree) = rankTreeRandomly(tree_aux)
        else:
            tree = newick2Tree(s1)
        labelTree(tree)
        return(tree)

if __name__ == "__main__":
    tree_type = sys.argv[1]
    next_arg = 2
    tree = getTree(tree_type,sys.argv[next_arg])
    next_arg += 1
    stree = tree.asNewick()
    
    # Reading the evolutionary model
    M = sys.argv[next_arg]
    next_arg += 1
    if M == 'DL':
        MODEL={'D':True,'L':True,'T':False}
    elif M == 'DLT':
        MODEL={'D':True,'L':True,'T':True}
    else:
        print(USAGE)
        sys.exit()

    # Reading the history size
    N = sys.argv[next_arg]
    if N.isdigit():
        n = int(N)
    else:
        print(USAGE)
        sys.exit()
    next_arg += 1
    
    # Counting
    print('#Species tree: '+stree)
    print('#Model: '+M)
    print('#History size: '+N)
    print('#nb_histories\tnb_reconciliations')
    Sh,Hh,Dh,Th = fillMatricesHist(tree,n,MODEL)
    nbHistories = int(Hh[tree.getID()][n])
    Sr,Hr,Dr,Tr = fillMatricesRec(tree,n,MODEL)
    nbReconciliations = int(Hr[tree.getID()][n])
    print(str(nbHistories)+'\t'+str(nbReconciliations))
