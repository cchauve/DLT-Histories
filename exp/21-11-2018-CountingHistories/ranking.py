from trees import *
import random


def randomRanking(n):
    res = []
    l = n.getLength()
    weights = {n:l}
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
                    weights[v] = v.getLength()
                break
    return res

if __name__=="__main__":
    t = Node([Node([],101),Node([Node([],102),Node([],103)],104)],100)
    #printTree(t)
    for i in range(80000):
        print "->".join(["%s"%(u.getID()) for u in randomRanking(t)])
