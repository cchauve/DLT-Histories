from stats import *
import random 

def correctedLength(t):
    m = t.getLength()
    return m-((m+1)/2)

def randomRanking(n):
    res = []
    l = correctedLength(n)
    weights = {n:l}
    leaves = []
    while len(res)<l:
        acc = sum(weights.values())
        r = random.random()*acc
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
    times = {}
    for i,v in enumerate(res):
        times[v] = i+1
    for v in leaves:
        times[v] = len(res)+1
    return times

if __name__=="__main__":
    t = Node([Node([Node([],1001),Node([],1002)],101),Node([Node([Node([],1003),Node([],1004)],102),Node([Node([],1005),Node([],1006)],103)],104)],100)
    #printTree(t)
    for i in range(80000):
        res = randomRanking(t)
        print res
        print "->".join(["%s"%(u.getID()) for u in res])
