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
# X < 1: more parsimonious histories are more likely to be drawn
# X > 1: less parsimonious histories are more likely to be drawn
# The same value of X should be used in filleMatrices and randGen
# WZ = weight given to each leaf. WZ is a dictionary that should
# be indexed by the IDs of the leaves of tree
def fillMatrices(tree,N,MODEL={'D':True,'L':True,'T':False},X=1.0,WZ={i:1.0 for i in range(0,1000)}):

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
                    H[i][n] = Ext(u)*WZ[i]
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

