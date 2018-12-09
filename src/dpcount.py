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

            
def Ext(u):
    return 1.
def Loss(u):
    return 1.
def Dup(u):
    return 1.
def Tran(u,v):
    return 1.

def ExtLbl(u):
    return "Z%s"%(u.getID())
def LossLbl(u):
    return "L%s"%(u.getID())
def DupLbl(u):
    return "D%s"%(u.getID())
def TranLbl(u,v):
    return "T%s->%s"%(u.getID(),v.getID())

##def ExtLbl(u):
##    return "Z"
##def LossLbl(u):
##    return "L"
##def DupLbl(u):
##    return "D"
##def TranLbl(u,v):
##    return "T%s"%(u.getTime())

def fillMatrices(tree,N):
    global ALLOW_TRANSFERS
    nodes = tree.allNodes()
    S = [[0 for n in range(N+1)] for u in nodes]
    H = [[0 for n in range(N+1)] for u in nodes]
    D = [[0 for n in range(N+1)] for u in nodes]
    T = [[0 for n in range(N+1)] for u in nodes]
    for n in range(1,N+1):
        for u in nodes:
            i = u.getID()
            for m in range(1,n):
                    D[i][n] += H[i][n-m]*H[i][m]*Dup(u)
            if ALLOW_TRANSFERS:
                receivers = u.getIncomparable()
                if u.getTime() >= 0:
                    receivers = u.getContemporary()
                for v in receivers:
                    j = v.getID()
                    for m in range(1,n):
                        T[i][n] += H[i][n-m]*H[j][m]*Tran(u,v)
            if u.isLeaf():
                if n==1:
                    H[i][n] = Ext(u)
                else: # => n>1
                    H[i][n] = D[i][n] + T[i][n]
            else: # => n ancestor
                if u.isBinary():
                    l,r = u.getLeft(),u.getRight()
                    lid,rid= l.getID(),r.getID()
                    S[i][n] = Loss(l)*H[rid][n] + Loss(r)*H[lid][n]
                    for m in range(1,n):
                        S[i][n] += H[lid][n-m]*H[rid][m]
                if u.isUnary():
                    c = u.getChild()
                    cid = c.getID()
                    S[i][n] = H[cid][n]
                    
                H[i][n] = D[i][n] + S[i][n] + T[i][n]
    return S,H,D,T

def randGen(u,state="H",n=0,S=[],H=[],D=[],T=[]):
    global ALLOW_TRANSFERS
    i = u.getID()
    if state == 'D':
        rand = random.random()*D[i][n]
        for m in range(1,n):
            rand -= H[i][n-m]*H[i][m]*Dup(u)
            if rand<0:
                return [DupLbl(u)]+randGen(u,'H',n-m,S,H,D,T)+randGen(u,'H',m,S,H,D,T)
    if state=="T":
        rand = random.random()*T[i][n]
        if ALLOW_TRANSFERS:
            receivers = u.getIncomparable()
            if u.getTime() >= 0:
                receivers = u.getContemporary()
            for v in receivers:
                j = v.getID()
                for m in range(1,n):
                    rand -= H[i][n-m]*H[j][m]*Tran(u,v)
                    if rand<0:
                        return [TranLbl(u,v)]+randGen(u,'H',n-m,S,H,D,T)+randGen(v,'H',m,S,H,D,T)
    if u.isLeaf():
        if state == 'H':
            if n==1:
                return [ExtLbl(u)]
            else: # => n>1
                rand = random.random()*H[i][n]
                rand  -= D[i][n]
                if rand<0:
                    return randGen(u,'D',n,S,H,D,T)
                rand  -= T[i][n]
                if rand<0:
                    return randGen(u,'T',n,S,H,D,T)
    else:
        if state == 'S':
            if u.isBinary():
                l,r = u.getLeft(),u.getRight()
                lid,rid= l.getID(),r.getID()
                rand = random.random()*S[i][n]
                rand -= Loss(l)*H[rid][n]
                if rand<0:
                    return [LossLbl(l)] + randGen(r,'H',n,S,H,D,T)
                rand -= Loss(r)*H[lid][n]
                if rand<0:
                    return randGen(l,'H',n,S,H,D,T) + [LossLbl(r)]
                for m in range(1,n):
                    rand -= H[lid][n-m]*H[rid][m]
                    if rand<0:
                        return randGen(l,'H',n-m,S,H,D,T) + randGen(r,'H',m,S,H,D,T)
            if u.isUnary():
                c = u.getChild()
                cid = c.getID()
                rand = random.random()*S[i][n]
                rand -= H[cid][n]
                if rand<0:
                    return randGen(c,'H',n,S,H,D,T)
                
        elif state == 'H':
            rand = random.random()*H[i][n]
            rand -= D[i][n]
            if rand<0:
                return randGen(u,'D',n,S,H,D,T)
            rand -= S[i][n]
            if rand<0:
                return randGen(u,'S',n,S,H,D,T)
            rand -= T[i][n]
            if rand<0:
                return randGen(u,'T',n,S,H,D,T)
    return None
