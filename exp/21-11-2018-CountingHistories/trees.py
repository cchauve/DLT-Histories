import os,sys
import random

class Node:
    def __init__(self, children=[], id=-1, time=-1):
        self.children = children[:]
        for c in self.children:
            c.setParent(self)
        self.id = id
        self.parent = None
        self.time = time
    def getID(self):
        return self.id
    def setID(self,id):
        self.id =  id
    def getTime(self):
        return self.time
    def getLength(self):
        n = 1
        for c in self.children:
            n += c.getLength()
        return n

    def setParent(self,u):
        self.parent = u
    def getParent(self):
        return self.parent

    def isRoot(self):
        return(self.parent==None)
    def isBinary(self):
        return len(self.children)==2
    def isUnary(self):
        return len(self.children)==1
    def isLeaf(self):
        return len(self.children)==0

    def getChildren(self):
        return self.children
    def getLeft(self):
        assert len(self.children)==2
        return self.children[0]
    def getRight(self):
        assert len(self.children)==2
        return self.children[1]
    def getChild(self):
        assert len(self.children)==1
        return self.children[0]

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
    def getContemporary(self):
        return [v for v in self.getIncomparable() if v.getTime() == self.time]

    def shave(self):
        if len(self.children)>0:
            nchildren = [c.shave() for c in self.children if c.shave() is not None]
            return Node(nchildren, self.id, self.time)
        else:
            return None

def buildCaterpillar(k):
    if k==0:
        return Node()
    else:
        return Node([Node(),buildCaterpillar(k-1)])

def buildTimedCaterpillar(k,h=None):
    if h is None:
        h=0
    if k==0:
        return Node([],-1,h)
    else:
        # Single branch
        u = Node([],-1,h+k)
        for i in range(h+k-1,h,-1):
            u = Node([u],-1,i)
        return Node([u,buildTimedCaterpillar(k-1,h+1)],-1,h)

def labelTree(t,currentID=0):
    for c in t.getChildren():
        currentID = labelTree(c,currentID)
    t.setID(currentID)
    return currentID+1

def printTree(t,indent=0):
    print " "*(indent)+"-> %s (t=%s)"%(t.getID(),t.getTime())
    for c in t.getChildren():
        printTree(c,indent+1)


if __name__=="__main__":
    k = int(sys.argv[1])
    timed = True
    showTree = False

    i = 2
    while i<len(sys.argv):
        if sys.argv[i].lower()=="--timed":
            i+=1
            timed = parseBoolean(sys.argv[i])

    cat = buildCaterpillar(k)
    if timed:
        cat = buildTimedCaterpillar(k)
    else:
        cat = buildCaterpillar(k)
    
    labelTree(cat)
    printTree(cat)
