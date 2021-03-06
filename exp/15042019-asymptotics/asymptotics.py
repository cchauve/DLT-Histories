__author__  = "Cedric Chauve, Michael Wallner"
__date__    = "April 14, 2019"

import sys
import numpy as np
import sympy as syp
import os
from sympy.matrices import Matrix, zeros
from trees import *

# ---------------------------------------------------------------------------
# Given a tree t, creates a system of equation whose solution gives
# the exponential growth factor of the counting sequence for the number
# of histories conditional to t
#
# naive algorithm: create 1 equation per node
# i.e. does not optimize for identical subgrammars due to identical subtrees
#
# Input: 
# t .............. root of species tree: Node class
# MODEL .......... evolutionary model
# Assumption: if not MODEL['L'] then not MODEL['SL']
# Output: 
# mySys .......... String with system of equations
# M .............. Symbolic matrix of the system
def getSystem(t,MODEL={'D':True,'L':True,'T':False,'SL':False}):
    if (not MODEL['L']) and MODEL['SL']:
        print('ERROR: SL allowed while L not allowed')
        
    # Tree t nodes
    allNodes = t.allNodes()
    K        = len(allNodes)
    
    # Create symbolic variables needed for the determinant
    symVarStr  = ','.join(['b'+str(i) for i in range(K)])+',z'
    symVarList = syp.symbols(symVarStr)
    symVarDict = {str(v):v for v in symVarList}

    M     = zeros(K) 
    mySys = []    
    
    for u in allNodes:
        i  = u.getID()
        bi = symVarDict['b'+str(i)]
        eq = 0
        
        # Duplication
        if MODEL['D']:
            eq += -bi+bi*bi
            M[i,i] = 2*symVarList[i]-1

        if u.isLeaf():
            eq += symVarDict['z']
        elif u.isUnary():
            c  = u.getChild().getID()
            bc = symVarDict['b'+str(c)]
            eq += bc # Unary speciation
            M[i,c] = symVarList[c]+1
        else:
            l,r = u.getLeft().getID(),u.getRight().getID()
            bl  = symVarDict['b'+str(l)]
            br  = symVarDict['b'+str(r)]
            if not MODEL['SL']:
                eq += bl*br#+'+'+bl+'+'+br # Speciation
            if MODEL['L']:
                eq += bl+br # SpeciationLoss
            M[i,l] = symVarList[r]+1
            M[i,r] = symVarList[l]+1

        # HGT
        if MODEL['T']:
            if u.getTime() >= 0:
                receivers = u.getContemporary()
            else:
                receivers = u.getIncomparable()
            for v in receivers:
               j  = v.getID()
               bj = symVarDict['b'+str(j)]
               eq += bi*bj
               M[i,i] += symVarList[j]
               M[i,j]  = symVarList[i]

        mySys.append(eq)
        
    detM = M.det(method='det_LU')
    mySys.append(detM)
    
    return((mySys,symVarList))

def solveSystem(mySys,symVarList):
    solver_name = 'tmp_solver.py'
    solver_file = open(solver_name,'w')

    solver_file.write('import numpy as np\n')
    solver_file.write('import scipy\n')
    solver_file.write('import scipy.optimize as opt\n')

    solver_file.write('\n')
    solver_file.write('def f(X):\n')
    VAR = '\t('
    for v in symVarList:
        VAR +=str(v)+','
    VAR += ') = X\n'
    solver_file.write(VAR.replace(',)',')'))
    EQS = '\tf = '+str(mySys)
    solver_file.write(EQS+'\n')
    solver_file.write('\treturn(f)\n')
    solver_file.write('\n')
    RHS = 'RHS = ['
    for i in range(len(symVarList)):
        RHS +='0,'
    RHS += ','
    solver_file.write(RHS.replace(',,',']')+'\n')
    solver_file.write('\n')
    solver_file.write('def tmp_solve(f):\n')
    solver_file.write('\tsol = opt.newton_krylov(f,RHS,f_tol=1e-14)\n')
    solver_file.write('\treturn(1.0/sol['+str(len(symVarList)-1)+'])\n')
    solver_file.write('SOL = tmp_solve(f)\n')
    
if __name__ == "__main__":
    # k = int(sys.argv[1])
    # t = randomBinaryTree(k)
    t = newick2Tree(sys.argv[1])
    labelTree(t)
    s = t.asNewick()

    (sysEqs,sysVars) = getSystem(t)
    solveSystem(sysEqs,sysVars)
    from tmp_solver import SOL
    print(SOL)
