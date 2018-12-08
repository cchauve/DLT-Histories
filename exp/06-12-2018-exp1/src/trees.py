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

def copyTree(t):
    copyChildren = []
    for child in t.getChildren():
        copyChildren.append(copyTree(child))
    newTree = Node(copyChildren,t.getID(),t.getTime())
    return newTree
        
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
    newTree = copyTree(t)
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
    # Inserting unary nodes on the branches of the ranked tree
    for v in newTree.allNodes():
        if not v.isRoot():
            vtime = v.getTime()
            p     = v.getParent()
            ptime = p.getTime()
            currentNode = p
            for time in range(ptime+1,vtime):
                newNode = Node([v],-1,time)
                newNode.setParent(currentNode)
                newChildren = []
                for child in currentNode.getChildren():                    
                    if v == child:
                        newChildren.append(newNode)
                    else:
                        newChildren.append(child)
                currentNode.setChildren(newChildren)
                currentNode = newNode
    # Returning the new tree
    return newTree

def buildCaterpillar(k):
    if k==0:
        return Node()
    else:
        return Node([Node(),buildCaterpillar(k-1)])

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
