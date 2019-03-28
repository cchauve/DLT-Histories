from trees import *
import random

GGD_PREAMBLE = """TYPE=GRAMMAR

SYMBOLS=WORDS

START = H%s

RULES ="""

"""def createGGDGrammar(k,CancelDups=True,CancelLosses=True):
    n = 2*k+1
    out = GGD_PREAMBLE%n+"\n"

    for x in range(k):
        i = n-x
        il = i-1
        ir = i-k
        if x==k-1:
            il=1
        out += "H%s -> D%s;\n"%(i,i)
        out += "H%s -> S%s;\n"%(i,i)
        out += "S%s -> H%s H%s;\n"%(i,ir,il)
        out += "S%s -> H%s x%s;\n"%(i,ir,il)
        out += "S%s -> x%s H%s;\n"%(i,ir,il)
        out += "D%s -> H%s H%s y%s;\n\n"%(i,i,i,i)
    for i in range(k+1,0,-1):
        out += "H%s -> Z%s;\n"%(i,i)
        out += "H%s -> D%s;\n"%(i,i)
        out += "D%s -> H%s H%s y%s;\n\n"%(i,i,i,i)
    if CancelDups:
        for i in range(n,0,-1):
            out += "y%s -> ;\n"%(i)
    if CancelLosses:
        for i in range(n-1,0,-1):
            out += "x%s -> ;\n"%(i)
    return out"""


## ---------------------------------------------------------------------------
# Counting and sampling histories

# Functions counting the number of ways an event can occur
def Ext(u):
    return 1.0
def Loss(u):
    return 1.0
def Dup(u):
    return 1.0
def Tran(u,v):
    return 1.0

def ExtLbl(u):
    return "Z%s"%(u.getID())
def LossLbl(u):
    return "L%s"%(u.getID())
def DupLbl(u):
    return "D%s"%(u.getID())
def TranLbl(u,v):
    return "T%s->%s"%(u.getID(),v.getID())


# X: parameter aimed at skewing the uniform distribution for sampling
# X < 1: parsimonious histories are more likely to be drawn
# X > 1: non-parsimonious histories are more likely to be drawn
# The same value of X should be used in filleMatrices and randGen
def fillMatrices(tree,N,MODEL={'D':True,'L':True,'T':False},X=1.0):

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
                        T[i][n] += H[i][n-m]*H[j][m]*Tran(u,v)*X
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

    return S,H,D,T

def randGen(u,state="H",n=0,S=[],H=[],D=[],T=[],MODEL={'D':True,'L':True,'T':False},X=1.0):
    i = u.getID()

    if state == "H":
        if u.isLeaf():
            if n==1:
                return [ExtLbl(u)]
            else: # => n>1
                rand  = random.random()*H[i][n]
                rand -= D[i][n]
                if rand<0:
                    return randGen(u,'D',n,S,H,D,T,MODEL,X)
                rand -= T[i][n]
                if rand<0:
                    return randGen(u,'T',n,S,H,D,T,MODEL,X)
        else:
            rand = random.random()*H[i][n]
            rand -= D[i][n]
            if rand<0:
                return randGen(u,'D',n,S,H,D,T,MODEL,X)
            rand -= S[i][n]
            if rand<0:
                return randGen(u,'S',n,S,H,D,T,MODEL,X)
            rand -= T[i][n]
            if rand<0:
                return randGen(u,'T',n,S,H,D,T,MODEL,X)

    if state == "D" and MODEL['D']:
        rand = random.random()*D[i][n]
        for m in range(1,n):
            rand -= H[i][n-m]*H[i][m]*Dup(u)*X
            if rand<0:
                return [DupLbl(u)]+randGen(u,'H',n-m,S,H,D,T,MODEL,X)+randGen(u,'H',m,S,H,D,T,MODEL,X)
            
    if state == "T" and MODEL['T']:
        rand = random.random()*T[i][n]
        if u.getTime() >= 0:
            receivers = u.getContemporary()
        else:
            receivers = u.getIncomparable()
        for v in receivers:
            j = v.getID()
            for m in range(1,n):
                rand -= H[i][n-m]*H[j][m]*Tran(u,v)*X
                if rand<0:
                    return [TranLbl(u,v)]+randGen(u,'H',n-m,S,H,D,T,MODEL,X)+randGen(v,'H',m,S,H,D,T,MODEL,X)
                
    if state == "S" and (not u.isLeaf()):
        if u.isBinary():
            l,r = u.getLeft(),u.getRight()
            lid,rid= l.getID(),r.getID()
            rand = random.random()*S[i][n]
            if MODEL['L']:
                rand -= Loss(l)*H[rid][n]*X
                if rand<0:
                    return [LossLbl(l)] + randGen(r,'H',n,S,H,D,T,MODEL,X)
                rand -= Loss(r)*H[lid][n]*X
                if rand<0:
                    return randGen(l,'H',n,S,H,D,T,MODEL,X) + [LossLbl(r)]
            for m in range(1,n):
                rand -= H[lid][n-m]*H[rid][m]
                if rand<0:
                    return randGen(l,'H',n-m,S,H,D,T,MODEL,X) + randGen(r,'H',m,S,H,D,T,MODEL,X)
        if u.isUnary():
            c = u.getChild()
            cid = c.getID()
            rand = random.random()*S[i][n]
            rand -= H[cid][n]
            if rand<0:
                return randGen(c,'H',n,S,H,D,T,MODEL,X)

    return None


## ---------------------------------------------------------------------------
# Counting parsimonious histories.
# We compute matrices similar to above but each cell contains a pair of numbers:
# cell[NB] = number of parsimonious histories
# cell[SC] = score of parsimonious histories

# Cost functions for evolutionary events
def costLoss(u):
    return 1.0
def costDup(u):
    return 1.0
def costTran(u,v):
    return 1.0

UNFILLED=-1  # Initial score values for unfilled cells 
NB = 'nb'    # Index of cells: number of parsimonious histories
SC = 'score' # Index of cells: parsimony score

# Auxiliary functions:

# Scan a list of cells to find the one(s) with the minimum score
# and return the total number of found histories with min scores
# Each cell is given a cost for an evolutionary event associated to it
# that increases its score and a multiplicity that records in how
# many ways the event can occur.
def updateCell1(cellList,costs,multiplicities):
    minScore = UNFILLED
    nbCells  = len(cellList)
    for c in range(0,nbCells):
        cell = cellList[c]
        if minScore == UNFILLED or (cell[SC]!=UNFILLED and minScore>cell[SC]+costs[c]):
            minScore = cell[SC]+costs[c]
    nbHistories = 0
    for c in range(0,nbCells):
        cell = cellList[c]
        if minScore == cell[SC]+costs[c]:
            nbHistories += cell[NB]*multiplicities[c]
    return({NB: nbHistories, SC: minScore})

# Cartesian product of two cells lists indexed by size,
# with a target size n and a cost and multiplicity associated to
# a specific evolutionary event.
# The aim is to find the pairs leading to a minimum score and the total
# number of histories they define
def updateCell2(cells1,cells2,n,cost,multiplicity):
    minScore     = UNFILLED
    for m in range(1,n):
        score1 = cells1[n-m][SC]
        score2 = cells2[m][SC]
        if score1!=UNFILLED and score2!=UNFILLED:
            currentScore = score1+score2+cost
            if minScore == UNFILLED or minScore>currentScore:
                minScore = currentScore
    nbHistories = 0
    for m in range(1,n):
        score1 = cells1[n-m][SC]
        score2 = cells2[m][SC]
        if score1!=UNFILLED and score2!=UNFILLED:
            currentScore = score1+score2+cost
            if currentScore == minScore:
                nbHistories += cells1[n-m][NB]*cells2[m][NB]*multiplicity
    return({NB: nbHistories, SC: minScore})

# Fill matrices considering only parsimonious histories
def fillMatricesPars(tree,N,MODEL={'D':True,'L':True,'T':False}):
    nodes = tree.allNodes()
    S = [[{NB:0,SC:UNFILLED} for n in range(N+1)] for u in nodes]
    H = [[{NB:0,SC:UNFILLED} for n in range(N+1)] for u in nodes]
    D = [[{NB:0,SC:UNFILLED} for n in range(N+1)] for u in nodes]
    T = [[{NB:0,SC:UNFILLED} for n in range(N+1)] for u in nodes]

    for n in range(1,N+1):
        for u in nodes:
            i = u.getID()
            if MODEL['D']:
                D[i][n] = updateCell2(H[i],H[i],n,costDup(u),Dup(u))

            if MODEL['T']:
                if u.getTime() >= 0:
                    receivers = u.getContemporary()
                else:
                    receivers = u.getIncomparable()
                receiversCells = []
                for v in receivers:
                    j = v.getID()
                    receiversCells.append(updateCell2(H[i],H[j],n,costTran(u,v),Tran(u,v)))
                T[i][n] = updateCell1(receiversCells,[0.0 for c in receiversCells],[1 for c in receiversCells])

            if u.isLeaf():
                if n==1:
                    H[i][n] = {NB:1,SC:0.0}
                else: # => n>1
                    H[i][n] = updateCell1([D[i][n],T[i][n]],[0.0,0.0],[1,1])
                        
            else: # => n ancestor
                if u.isBinary():
                    l,r = u.getLeft(),u.getRight()
                    lid,rid= l.getID(),r.getID()
                    if MODEL['L']:
                        S[i][n] = updateCell1([H[rid][n],H[lid][n]],[costLoss(r),costLoss(l)],[Loss(r),Loss(l)])                    
                    for m in range(1,n):
                        if (H[lid][n-m][SC]+H[rid][m][SC])<S[i][n][SC]:
                            S[i][n] = {NB: H[lid][n-m][NB]*H[rid][m][NB], SC: H[lid][n-m][SC]+H[rid][m][SC]}
                        elif (H[lid][n-m][SC]+H[rid][m][SC]) == S[i][n][SC]:
                            S[i][n][NB] += H[lid][n-m][NB]*H[rid][m][NB]
                if u.isUnary():
                    c = u.getChild()
                    cid = c.getID()
                    S[i][n] = {NB: H[cid][n][NB], SC: H[cid][n][SC]}

                H[i][n] = updateCell1([D[i][n],S[i][n],T[i][n]],[0.0,0.0,0.0],[1,1,1])     

    return S,H,D,T

def extractNbHistoriesMatrixPars(M,tree,N):
    nodes = tree.allNodes()
    M1 = [[0 for n in range(N+1)] for u in nodes]
    for n in range(1,N+1):
        for u in nodes:
            i = u.getID()
            M1[i][n] = M[i][n][NB]
    return(M1)

def extractScoresMatrixPars(M,tree,N):
    nodes = tree.allNodes()
    M1 = [[0 for n in range(N+1)] for u in nodes]
    for n in range(1,N+1):
        for u in nodes:
            i = u.getID()
            M1[i][n] = M[i][n][SC]
    return(M1)
