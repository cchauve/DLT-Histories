#!/usr/bin/env python

"""solve_system.py: solves systems of polynomial equations provided as input."""
"""input format: one line per instance"""
"""size<TAB>tree index<TAB>tree newick<SPACE>subtrees<TAB>degree of system<TAB>system"""
"""output format: one line per instance"""
"""size<TAB>tree index<TAB>growth factor"""
"""generates also a file <SIZE>_<TREE INDEX>_solver.py' that encodes the precise commands to solve the system for the instance"""

__author__  = "Cedric Chauve"
__date__    = "January 28, 2019"

import os, sys

# Reading systems
SYSTEMS = {}
SIZE    = '0'
input_file = sys.argv[1]
input_stream = open(input_file,'r').readlines()
for l in input_stream:
    if l[0] != '#':
        l1 = l.rstrip().split('\t')
        SIZE   = l1[0]
        tree   = l1[1]
        system_degree    = int(l1[4])
        system_equations = l1[5].replace('{','').replace('}','').replace('[','').replace(']','').replace('^','**').replace('R','r').split(',')
        SYSTEMS[tree] = (system_degree,system_equations)

# Writing the solver script
output_dir  = sys.argv[2]

solver_name = output_dir+'/'+SIZE+'_solver.py'
solver_file = open(solver_name,'w')
solver_file.write('import numpy as np\n')
solver_file.write('import scipy\n')
solver_file.write('import scipy.optimize as opt\n')
solver_file.write('\n')
solver_file.write('ALL_RHS = {}\n')

for tree in SYSTEMS.keys():
    (system_degree,system_equations) = SYSTEMS[tree]

    solver_file.write('\n')
    solver_file.write('def f_'+tree+'(X):\n')
    VAR = '\t(z'
    for i in range(0,system_degree):
        VAR +=',r'+str(i)
    VAR += ') = X\n'
    solver_file.write(VAR)
    EQS = '\tf = ['
    for eq in system_equations:
        EQS += eq+','
    EQS +=','
    solver_file.write(EQS.replace(',,',']\n'))
    solver_file.write('\treturn(f)\n')
    solver_file.write('\n')
    RHS = ''
    for i in range(0,system_degree+1):
        RHS +='0,'
    RHS += ','

    solver_file.write('ALL_RHS['+tree+'] = ['+RHS.replace(',,',']')+'\n')

solver_file.write('\n')
solver_file.write('def solve_nk(f,t):\n\treturn(opt.newton_krylov(f,ALL_RHS[t],f_tol=1e-14))\n')
solver_file.write('\n')
solver_file.write('if __name__ == \'__main__\':\n')
solver_file.write('\tprint(\'#size\ttree index\tgrowth factor\')\n')
for tree in SYSTEMS.keys():
    solver_file.write('\tsol_nk_'+tree+' = solve_nk('+'f_'+tree+','+tree+')\n')
    solver_file.write('\tprint(\''+SIZE+'\\t'+tree+'\\t\'+str(1.0/sol_nk_'+tree+'[0]))\n')
solver_file.close()

