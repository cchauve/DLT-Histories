def getSystem(t,MODEL={'D':True,'L':True,'T':False,'SL':False}):
    if not MODEL['L'] and MODEL['SL']:
        print('ERROR: SL allowed while L not allowed')
        
    # Tree t nodes
    allNodes = t.allNodes()
    K        = len(allNodes)
    
    # create symbolic variables needed for the determinant
    symVarStr  = ','.join(['b'+str(i) for i in range(K)])   
    symVarList = sp.symbols(symVarStr)
    
    M     = np.zeros((K,K)) 
    mySys = []    
    for u in allNodes:
        i  = u.getID()
	bi = 'b'+i
        eq = ''
        
        # Duplication
        if MODEL['D']:
	    eq += '-'+bi+'+'+bi+'^2'
            M[i][i] = 2*symVarList[i]-1

        if u.isLeaf():
            eq = eq+'z'
        elif u.isUnary():
            c  = u.getChild().getID()
            bc = 'b'+c
            eq += bc # Unary speciation
            M[i][c] = symVarList[c]+1
        else:
            l,r = u.getLeft(),u.getRight()
            bl  = 'b'+l
            br  = 'b'+r
            if not MODEL['SL']:
                eq += bl+'*'+br+'+'+bl+'+'+br # Speciation
            if MODEL['L']:
                eq += bl+'+'+br # SpeciationLoss
            M[i][l] = symVarList[l]+1
            M[i][r] = symVarList[r]+1

        # HGT
        if MODEL['T']:
            if u.getTime() >= 0:
                receivers = u.getContemporary()
            else:
                receivers = u.getIncomparable()
            for v in receivers:
               j  = v.getID()
               bj = 'b'+j
               eq = eq+'+'+bi+'*'+bj
               M[i][i] += symVarList[j]
               M[i][j]  = symVarList[i]

        mySys.append(eq)

    return((mySys,M))

    #detM = M.det()
    #mySys.append(""+detM)
