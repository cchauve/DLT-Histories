import sys
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
    def setTime(self,time):
        self.time =  time
    def getLength(self):
        n = 1
        for c in self.children:
            n += c.getLength()
        return n

    def setParent(self,u):
        self.parent = u
    def getParent(self):
        return self.parent
    def getRoot(self):
        if self.parent is not None:
            return self.parent.getRoot()
        else:
            return self

    def extendLeft(self):
        self.children = [Node(self.children),Node()]
        return self.children
    def extendRight(self):
        self.children = [Node(),Node(self.children)]
        return self.children

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
    def setChildren(self,children):
        self.children = children
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
    def copy(self):
        copyChildren = []
        for child in self.getChildren():
            copyChildren.append(child.copy())
        newTree = Node(copyChildren,self.getID(),self.getTime())
        return newTree
    def copy(self):
        copyChildren = []
        for child in self.getChildren():
            copyChildren.append(child.copy())
        newTree = Node(copyChildren,self.getID(),self.getTime())
        return newTree
    def buildUnaryBinary(self,currentTime=0):
        t = self.getTime()
        if t>currentTime:
            return Node([self.buildUnaryBinary(currentTime+1)],-1,currentTime)
        else:
            nChildren = []
            for child in self.getChildren():
                nChildren.append(child.buildUnaryBinary(currentTime+1))
            return Node(nChildren,self.getID(),currentTime)
    def asString(self):
        return "("+",".join([t.asString() for t in self.children])+")"
        
def labelTree(t,currentID=0):
    for c in t.getChildren():
        currentID = labelTree(c,currentID)
    t.setID(currentID)
    return currentID+1

def printTree(t,indent=0):
    print " "*(indent)+"-> %s (t=%s)"%(t.getID(),t.getTime())
    for c in t.getChildren():
        printTree(c,indent+1)

def correctedLength(t):
    m = t.getLength()
    return m-((m+1)/2)

def rankTreeRandomly(t):
    newTree = t.copy()
    # Generating a ranking for the internal nodes of a copy of t
    res     = []
    l       = correctedLength(newTree)
    weights = {newTree:l}
    leaves  = []
    while len(res)<l:
        acc   = sum(weights.values())
        r     = random.random()*acc
        nodes = weights.keys()
        for u in nodes:
            w = weights[u]
            r -= w
            if r<0:
                res.append(u)
                del weights[u]
                for v in u.getChildren():
                    if v.isLeaf():
                        leaves.append(v)
                    else:
                        weights[v] = correctedLength(v)
                break
    # Setting the times/ranks for the nodes and leaves of the copy of t
    times = {}
    for i,v in enumerate(res):
        v.setTime(i)
    for v in leaves:
        v.setTime(len(res))
    printTree(newTree)
    # Inserting unary nodes on the branches of the ranked tree
    newTree = newTree.buildUnaryBinary()
    printTree(newTree)
    # Labeling nodes in postorder
    labelTree(newTree)
    return newTree

def buildCaterpillar(k):
    if k==0:
        return Node()
    else:
        return Node([Node(),buildCaterpillar(k-1)])

def randomBinaryTree(n):
    nodes = [Node()]
    while(len(nodes))<n:
        v = random.choice(nodes)
        if random.randint(0,1)==0:
            nodes += v.extendLeft()
        else:
            nodes += v.extendRight()
    nroot = nodes[0].getRoot()
    # Labeling nodes in postorder
    labelTree(nroot)
    return nroot

def newick2Tree(s):
    # Assumption: s is the newick string of a rooted binary tree
    if s[0] != "(": # Case 1: tree reduced to a leaf
        s1 = s.split(':')[0]
        return Node([],s1,-1)
    else: # Case 2, tree with a root
        # Assumption: we are on the opening (
        i = 1 # Next character
        # Looking for the left subtree
        j = i;
        if s[j] == "(":
            # We look for the closing parenthesis
            c = 1
            while c != 0:
                j += 1
                if s[j] == "(":
                    c += 1
                elif s[j] == ")":
                    c -= 1
            s1 = s[i:j+1]
            while s[j] != ",":
                j += 1
        else:
            while s[j] != ",":
                j += 1
            s1 = s[i:j]
        # Looking for the right subtree
        i = j+1
        j = i
        if s[j] == "(":
            # We look for the closing parenthesis
            c = 1
            while c != 0:
                j += 1
                if s[j] == "(":
                    c += 1
                elif s[j] == ")":
                    c -= 1
            s2 = s[i:j+1]
        else:
            while s[j] != ")":
                j += 1
            s2 = s[i:j]
        # We build the tree
        return Node([newick2Tree(s1),newick2Tree(s2)])