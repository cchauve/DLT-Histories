## ---------------------------------------------------------------------------

UNFILLED=-1
NB = 'nb'
SC = 'score'

def updateCell1(cellList,c=0.0):
    minScore = UNFILLED
    for cell in cellList:
        if minScore == UNFILLED or (cell[SC]!=UNFILLED and minScore>cell[SC]+c):
            minScore = cell[SC]+c
    nbHistories = 0
    for cell in cellList:
        if minScore == cell[SC]+c:
            nbHistories += cell[NB]
    return((nbHistories,minScore))

def updateCell2(cells,n,c):
    minScore = UNFILLED
    for m in range(1,n):
        score1 = cells[n-m][SC]
        score2 = cells[m][SC]
        if score1==UNFILLED:
            currentScore=score2+c
        elif score2==UNFILLED:
            currentScore=score1+c
        else:
            currentScore = score1+score2+c
        if minScore == UNFILLED or minScore>currentScore:
            minScore = currentScore
    nbHistories = 0
    for m in range(1,n):
        score1 = cells[n-m][SC]
        score2 = cells[m][SC]
        if score1==UNFILLED:
            currentScore=score2+c
        elif score2==UNFILLED:
            currentScore=score1+c
        else:
            currentScore = score1+score2+c
        if currentScore == minScore:
            nbHistories += cells[n-m][NB]*cells[m][NB]*c
    return((nbHistories,minScore))


def fillMatricesPars(tree,N,ALLOW_TRANSFERS):
    #global ALLOW_TRANSFERS
    nodes = tree.allNodes()
    S = [[{NB:0,SC:UNFILLED} for n in range(N+1)] for u in nodes]
    H = [[{NB:0,SC:UNFILLED} for n in range(N+1)] for u in nodes]
    D = [[{NB:0,SC:UNFILLED} for n in range(N+1)] for u in nodes]
    T = [[{NB:0,SC:UNFILLED} for n in range(N+1)] for u in nodes]
    for n in range(1,N+1):
        for u in nodes:
            i = u.getID()
            updatedCell = updateCell2(H[i],n,Dup(u))
            D[i][n][NB] = updatedCell[0]
            D[i][n][SC] = updatedCell[1]

            if ALLOW_TRANSFERS:
                if u.getTime() >= 0:
                    receivers = u.getContemporary()
                else:
                    receivers = u.getIncomparable()
                for v in receivers:
                    j = v.getID()
                updatedCell = updateCell2(H[i],n,Tran(u))
                T[i][n][NB] = updatedCell[0]
                T[i][n][SC] = updatedCell[1]

            if u.isLeaf():
                if n==1:
                    H[i][n] = {NB:1,SC:0}
                else: # => n>1
                    updatedCell = updateCell1([D[i][n],T[i][n]])
                    H[i][n][NB] = updatedCell[0]
                    H[i][n][SC] = updatedCell[1]
                        
            else: # => n ancestor
                if u.isBinary():
                    l,r = u.getLeft(),u.getRight()
                    lid,rid= l.getID(),r.getID()
                    updatedCell = updateCell1([H[rid][n],H[lid][n]],Loss(l)) 
                    S[i][n][NB] = updatedCell[0]
                    S[i][n][SC] = updatedCell[1] 
                    for m in range(1,n):
                        if (H[lid][n-m][SC]+H[rid][m][SC])<S[i][n][SC]:
                            S[i][n][SC] = H[lid][n-m][SC]+H[rid][m][SC]
                            S[1][n][NB] = H[lid][n-m][NB]*H[rid][m][NB]
                        elif (H[lid][n-m][SC]+H[rid][m][SC]) == S[i][n][SC]:
                            S[1][n][NB] += H[lid][n-m][NB]*H[rid][m][NB]
                if u.isUnary():
                    c = u.getChild()
                    cid = c.getID()
                    S[i][n][NB] = H[cid][n][NB]
                    S[i][n][SC] = H[cid][n][SC]

                updatedCell = updateCell1([D[i][n],S[i][n],T[i][n]])     
                H[i][n][NB] = updatedCell[0]
                H[i][n][SC] = updatedCell[1]

    S1 = [[0 for n in range(N+1)] for u in nodes]
    H1 = [[0 for n in range(N+1)] for u in nodes]
    D1 = [[0 for n in range(N+1)] for u in nodes]
    T1 = [[0 for n in range(N+1)] for u in nodes]
    for n in range(1,N+1):
        for u in nodes:
            i = u.getID()
            S1[i][n] = S[i][n][NB]
            H1[i][n] = H[i][n][NB]
            D1[i][n] = D[i][n][NB]
            T1[i][n] = T[i][n][NB]

    print(S1)
    print(H1)
    print(D1)
    print(T1)
    return S1,H1,D1,T1
