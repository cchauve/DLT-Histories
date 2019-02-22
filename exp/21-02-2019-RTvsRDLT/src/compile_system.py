#!/usr/bin/env python

"""compile_system.py: solves a system of polynomial equations provided as input."""
"""input format: two lines file"""
"""first line = degree of the system"""
"""second line = maple description of the system"""
"""output: list of the values for each variable"""
"""generates also a file sys.argv[1]+'_solver.py' that encodes the precise commands to solve the system"""

__author__  = "Cedric Chauve"
__date__    = "January 28, 2019"

import os, sys
system_file = sys.argv[1]
system_input = open(system_file,'r').readlines()
system_degree    = int(system_input[0])
system_equations = system_input[1].replace('{','').replace('}','').replace('[','').replace(']','').replace('^','**').replace('R','r').split(',')
solver_name = 'tmp_solver.py'
solver_file = open(solver_name,'w')

solver_file.write('import numpy as np\n')
solver_file.write('import scipy\n')
solver_file.write('import scipy.optimize as opt\n')

solver_file.write('\n')
solver_file.write('def f(X):\n')
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
solver_file.write('def solve_fsolve():\n\treturn(opt.fsolve(f, ('+RHS.replace(',,',')')+'))\n')
solver_file.write('\n')
solver_file.write('def solve_nk():\n\treturn(opt.newton_krylov(f, ['+RHS.replace(',,',']')+',f_tol=1e-14))\n')
solver_file.close()

from tmp_solver import f, solve_fsolve, solve_nk

#sol_fsolve = solve_fsolve()
sol_nk     = solve_nk()

def format_sol(sol):
    str_sol = ''
    for x in sol:
        str_sol += str(x)+' '
    str_sol += ' '
    return(str_sol.replace('  ',''))

#print(format_sol(sol_fsolve))
print(format_sol(sol_nk))

os.rename(solver_name,sys.argv[1]+'_solver.py')
