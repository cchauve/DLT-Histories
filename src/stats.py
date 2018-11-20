import os,sys
import random

GGD_PREAMBLE = """TYPE=GRAMMAR

SYMBOLS=WORDS

START = H%s

RULES ="""

def createGGDGrammar(k,CancelDups=True,CancelLosses=True):
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
    return out

class Node:
    def __init__(self, children=[], id=-1):
        self.children = children[:]
        for c in self.children:
            c.setParent(self)
        self.id = id
        self.parent = None
    def setParent(self,u):
        self.parent = u
    def getParent(self):
        return self.parent
    def isRoot(self):
        return(self.parent==None)
    def getChildren(self):
        return self.children
    def getID(self):
        return self.id
    def setID(self,id):
        self.id =  id
    def getLeft(self):
        assert len(self.children)==2
        return self.children[0]
    def getRight(self):
        assert len(self.children)==2
        return self.children[1]
    def isLeaf(self):
        return len(self.children)==0
    def allNodes(self):
        res = []
        for c in self.children:
            res += c.allNodes()
        res += [self]
        return res
    def getSiblings(self,u):
        return [v for v in self.children if u!=v]
    def getIncomparable(self):
        res = []
        if not self.isRoot():
            p = self.getParent()
            for c in p.getSiblings(self):
                res += c.allNodes()
            res += p.getIncomparable()
        return res

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
    return "T%s-%s"%(u.getID(),v.getID())

##def ExtLbl(u):
##    return ""
def LossLbl(u):
    return ""
def DupLbl(u):
    return "D"
def TranLbl(u,v):
    return "T"


def fillMatrices(tree,N):
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
            for v in u.getIncomparable():
                j = v.getID()
                for m in range(1,n):
                    T[i][n] += H[i][n-m]*H[j][m]*Tran(u,v)
            if u.isLeaf():
                if n==1:
                    H[i][n] = Ext(u)
                else: # => n>1
                    H[i][n] = D[i][n] + T[i][n]
            else: # => n ancestor
                l,r = u.getLeft(),u.getRight()
                lid,rid= l.getID(),r.getID()
                
                S[i][n] = Loss(l)*H[rid][n] + Loss(r)*H[lid][n]
                for m in range(1,n):
                    S[i][n] += H[lid][n-m]*H[rid][m]
                    
                H[i][n] = D[i][n] + S[i][n] + T[i][n]
    return S,H,D,T

def randGen(u,state="H",n=0,S=[],H=[],D=[],T=[]):
    i = u.getID()
    if state == 'D':
        rand = random.random()*D[i][n]
        for m in range(1,n):
            rand -= H[i][n-m]*H[i][m]*Dup(u)
            if rand<0:
                return [DupLbl(u)]+randGen(u,'H',n-m,S,H,D,T)+randGen(u,'H',m,S,H,D,T)
    if state=="T":
        rand = random.random()*T[i][n]
        for v in u.getIncomparable():
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
        l,r = u.getLeft(),u.getRight()
        lid,rid= l.getID(),r.getID()
        if state == 'S':
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

def buildCaterpillar(k):
    if k==0:
        return Node()
    else:
        return Node([Node(),buildCaterpillar(k-1)])

def labelTree(t,currentID=0):
    for c in t.getChildren():
        currentID = labelTree(c,currentID)
    t.setID(currentID)
    return currentID+1

def printTree(t,indent=0):
    print " "*(indent)+"-> %s"%(t.getID())
    for c in t.getChildren():
        printTree(c,indent+1)

    
PATH_GGD = "grammar.ggd"
PATH_TMP = "out.txt"

if __name__=="__main__":
    k = int(sys.argv[1])
    n = int(sys.argv[2])
    nb = int(sys.argv[3])

    cat = buildCaterpillar(k)
    labelTree(cat)
    printTree(cat)

##    for c in cat.allNodes():
##        print c.getID(),[v.getID() for v in c.getIncomparable()]

    S,H,D,T = fillMatrices(cat,n)

    raw = []
    allkeys = set()

    for i in range(nb):
        l = randGen(cat,"H",n, S, H, D, T)
        data = filter(lambda x: len(x) > 0, l)
        vals = {}
        for k in data:
            if k not in vals:
                vals[k] = 0
            vals[k] += 1
        allkeys = allkeys | set(vals.keys())
        raw.append(vals)
    
    
##    ggd = createGGDGrammar(k)
##    f = open(PATH_GGD,"w")
##    f.write(ggd)
##    f.close()
##
##    cmd = "java  -cp GenRGenS2.1-bin.jar GenRGenS.GenRGenS -size %s grammar.ggd -nb %s > %s"%(n,nb,PATH_TMP)
##    print cmd
##    os.system(cmd)
##    
##    for l in open(PATH_TMP):
##        data = l.strip().split()
##        vals = {}
##        for k in data:
##            if k not in vals:
##                vals[k] = 0
##            vals[k] += 1
##        allkeys = allkeys | set(vals.keys())
##        raw.append(vals)

    nbEmpty = 0
    for v in raw:
        for k in allkeys:
            if k not in v:
                nbEmpty +=1
                break

    vEmpty = {k:0 for k in allkeys}
    vAvg = {k:0 for k in allkeys}
    for v in raw:
        for k in allkeys:
            if k not in v:
                vEmpty[k]+=1
            else:
                vAvg[k] += v[k]
    
    print len(raw), nbEmpty
    print "   ".join(["%s->%.2f%% (%.2f)"%(k,100.*v/float(len(raw)),vAvg[k]/float(len(raw))) for (v,k) in sorted([(vEmpty[k],k) for k in allkeys])])

        
