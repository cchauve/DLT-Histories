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
HIST='H'
REC='R'
def Dup(u,HR): # Gene duplication, HR = 'H' for history, 'R' for reconciliation
    COEFF={HIST:1.0,REC:0.5}
    return(COEFF[HR])
def DupGen(u):
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
# Counting histories and reconciliations

# Filling the DP matrix counting the number of histories per size and per subtree
# X: parameter aimed at skewing the uniform distribution for sampling
# X < 1: parsimonious histories are more likely to be sampled
# X > 1: non-parsimonious histories are more likely to be sampled
# The same value of X should be used in filleMatrices and randGen
# MODEL specifies the evolutionary model
# O_MODEL specifies the object (history or reconciliation), HIST or REC
def fillMatrices_aux(tree,N,MODEL={'D':True,'L':True,'T':False},O_MODEL=HIST,X=1.0):

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
                    D[i][n] += H[i][n-m]*H[i][m]*Dup(u,O_MODEL)*X
                if n%2==0:
                    D[i][n] += H[i][int(n/2)]*(1.0-Dup(u,O_MODEL))*X
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

def fillMatricesHist(tree,N,MODEL={'D':True,'L':True,'T':False},X=1.0):
    return(fillMatrices_aux(tree,N,MODEL,HIST,X))

def fillMatricesRec(tree,N,MODEL={'D':True,'L':True,'T':False},X=1.0):
    return(fillMatrices_aux(tree,N,MODEL,REC,X))

# ---------------------------------------------------------------------------
# Sampling histories and reconciliations

def randGen_aux(u,state="H",n=0,S=[],H=[],D=[],T=[],MODEL={'D':True,'L':True,'T':False},O_MODEL=HIST,X=1.0):
    i = u.getID()

    if state == "H":
        if u.isLeaf():
            if n==1:
                return([ExtLbl(u)])
            else: # => n>1
                rand  = random.random()*H[i][n]
                rand -= D[i][n]
                if rand<0:
                    return(randGen_aux(u,'D',n,S,H,D,T,MODEL,O_MODEL,X))
                rand -= T[i][n]
                if rand<0:
                    return(randGen_aux(u,'T',n,S,H,D,T,MODEL,O_MODEL,X))
        else:
            rand = random.random()*H[i][n]
            rand -= D[i][n]
            if rand<0:
                return(randGen_aux(u,'D',n,S,H,D,T,MODEL,O_MODEL,X))
            rand -= S[i][n]
            if rand<0:
                return(randGen_aux(u,'S',n,S,H,D,T,MODEL,O_MODEL,X))
            rand -= T[i][n]
            if rand<0:
                return(randGen_aux(u,'T',n,S,H,D,T,MODEL,O_MODEL,X))

    if state == "D" and MODEL['D']:
        rand = random.random()*D[i][n]
        if O_MODEL==HIST:
            bound = n
        else:
            bound = int(n/2)+1
        for m in range(1,bound):
            rand -= H[i][n-m]*H[i][m]*DupGen(u)*X
            if rand<0:
                return([DupLbl(u)]+randGen_aux(u,'H',n-m,S,H,D,T,MODEL,O_MODEL,X)+randGen_aux(u,'H',m,S,H,D,T,MODEL,O_MODEL,X))
            
    if state == "T" and MODEL['T']:
        rand = random.random()*T[i][n]
        if u.getTime() >= 0:
            receivers = u.getContemporary()
        else:
            receivers = u.getIncomparable()
        for v in receivers:
            j = v.getID()
            for m in range(1,n):
                rand -= H[i][n-m]*H[j][m]*HGT(u,v)*X
                if rand<0:
                    return([HGTLbl(u,v)]+randGen_aux(u,'H',n-m,S,H,D,T,MODEL,O_MODEL,X)+randGen_aux(v,'H',m,S,H,D,T,MODEL,O_MODEL,X))
                
    if state == "S" and (not u.isLeaf()):
        if u.isBinary():
            l,r = u.getLeft(),u.getRight()
            lid,rid= l.getID(),r.getID()
            rand = random.random()*S[i][n]
            if MODEL['L']:
                rand -= Loss(l)*H[rid][n]*X
                if rand<0:
                    return([LossLbl(l)] + randGen_aux(r,'H',n,S,H,D,T,MODEL,O_MODEL,X))
                rand -= Loss(r)*H[lid][n]*X
                if rand<0:
                    return(randGen_aux(l,'H',n,S,H,D,T,MODEL,O_MODEL,X) + [LossLbl(r)])
            for m in range(1,n):
                rand -= H[lid][n-m]*H[rid][m]
                if rand<0:
                    return(randGen_aux(l,'H',n-m,S,H,D,T,MODEL,O_MODEL,X) + randGen_aux(r,'H',m,S,H,D,T,MODEL,O_MODEL,X))
        if u.isUnary():
            c = u.getChild()
            cid = c.getID()
            rand = random.random()*S[i][n]
            rand -= H[cid][n]
            if rand<0:
                return(randGen_aux(c,'H',n,S,H,D,T,MODEL,O_MODEL,X))

    return(None)

def randGenHist(u,state="H",n=0,S=[],H=[],D=[],T=[],MODEL={'D':True,'L':True,'T':False},X=1.0):
    return(randGen_aux(u,state,n,S,H,D,T,MODEL,HIST,X))

def randGenRec(u,state="H",n=0,S=[],H=[],D=[],T=[],MODEL={'D':True,'L':True,'T':False},X=1.0):
    return(randGen_aux(u,state,n,S,H,D,T,MODEL,REC,X))


# ---------------------------------------------------------------------------

USAGE = 'DLTcount <tree> <MODEL> <OBJECT> <n> <number of samples>\n'+'tree = random k | rrandom k | caterpillar k | rcaterpillar k | balanced k | rbalanced k | newick string\n'+'\trandom k = random binary tree with k leaves\n'+'\trrandom k = randomly ranked random binary tree with k leaves\n'+'\tcaterpillar k = caterpillar with k leaves\n'+'\trcaterpillar k = randomly ranked caterpillar with k leaves\n'+'\tbalanced k = balanced binary tree with k leaves\n'+'\trbalanced k = randomly ranked balanced binary tree with k leaves\n'+'\tnewick string = string is the Newick representation of a tree\n'+'MODEL = DL | DLT\n'+'OBJECT = HISR | REC\n'+'n = history/reconciliation size\n'+'number of samples = non-negative integer, number of sampled histories/reconciliations'

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
            tree = buildBalancedTree(k)
        elif s1 == 'rrandom':
            tree_aux = randomOrderedBinaryTree(k)
            (ranking,tree) = rankTreeRandomly(tree_aux)
        elif s1 == 'rcaterpillar':
            tree_aux = buildCaterpillar(k)
            (ranking,tree) = rankTreeRandomly(tree_aux)
        elif s1 == 'rcomplete':
            tree_aux = buildBalancedTree(k)
            (ranking,tree) = rankTreeRandomly(tree_aux)
        else:
            tree = newick2Tree(s1)
        labelTree(tree)
        return(tree)

if __name__ == "__main__":
    tree_type = sys.argv[1]
    next_arg = 2
    tree = getTree(tree_type,sys.argv[next_arg])
    stree = tree.asNewick()
    next_arg += 1
    
    # Reading the evolutionary model
    M = sys.argv[next_arg]
    if M == 'DL':
        MODEL={'D':True,'L':True,'T':False}
    elif M == 'DLT':
        MODEL={'D':True,'L':True,'T':True}
    else:
        print(USAGE)
        sys.exit()
    next_arg += 1

    # Reading the object model
    O = sys.argv[next_arg]
    if O == 'HIST':
        O_MODEL=HIST
    elif O == 'REC':
        O_MODEL=REC
    else:
        print(USAGE)
        sys.exit()
    next_arg += 1

    # Reading the history size
    N = sys.argv[next_arg]
    if N.isdigit():
        n = int(N)
    else:
        print(USAGE)
        sys.exit()
    next_arg += 1

    # Reading the sampling parameters
    NBS = sys.argv[next_arg]
    if NBS.isdigit():        
        nbSamples = int(NBS)
    else:
        print(USAGE)
        sys.exit()
    
    # Counting
    print('#Species tree: '+stree)
    print('#Model: '+M)
    if O_MODEL == HIST:
        print('#History size: '+N)
        S,H,D,T = fillMatricesHist(tree,n,MODEL)
        nbHistories = int(H[tree.getID()][n])
        print('Nb_histories\t'+str(nbHistories))
        for s in range(nbSamples):
            history = randGenHist(tree,'H',n,S,H,D,T,MODEL)
            strHistory = str(history)
            print('Sampled history '+str(s+1)+': '+strHistory)
    elif O_MODEL == REC:
        print('#Reconciliation size: '+N)
        S,H,D,T = fillMatricesRec(tree,n,MODEL)
        nbReconciliations = int(H[tree.getID()][n])
        print('Nb_reconciliations\t'+str(nbReconciliations))
        for s in range(nbSamples):
            reconciliation = randGenRec(tree,'H',n,S,H,D,T,MODEL)
            strReconciliation = str(reconciliation)
            print('Sampled reconciliation '+str(s+1)+': '+strReconciliation)




