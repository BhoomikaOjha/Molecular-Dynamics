# This code calls the gaussian software...
# 1. make the input file for gaussian..
# 2. script the gaussian calling code..
# 3. take the input from the gaussian 
# 4. pass the output to main.f90


from periodicTable import *
import pandas as pd 
import json
import numpy as np
import os

# load the data set of the molecular coordinates! 
with open("molecule_coordinates.json") as f:
	data = json.load(f)

# get the coordinates from the json file...
xyz = []
natoms = len(data[0]['atoms'])
print "The no of atoms in the molecule is: ",natoms

# create the gaussian input file name
inputfile = "inGauss.dat"
inpf = open(inputfile,'w')

# call the fortran program with arguments 
	# 1. xyz[]: contains the coordinates
	# 2. atomic nos 
	# 3. mass no 
 	# 4. no of atoms

Z_no = [] # list of atomic no
A_no = [] # list of mass no 

for j in range(natoms):
	xyz.append(data[0]['atoms'][j]['xyz'])

for j in range(natoms):
	ele = str(data[0]['atoms'][j]['type'])	
	Z_no.append(periodic_table[ele][0])
	A_no.append(periodic_table[ele][1])

coo = np.zeros((natoms,3)) # coordinate arrays
for element in range(natoms):
	for c in range(3):
		coo[element][c] = data[0]['atoms'][element]['xyz'][c]


# unpack the xyz coordinates 



print Z_no
print A_no
# scripting starts ...  

rx_ext = 100 # extent of the reaction

os.system("python -m numpy.f2py -c -m md  main.f90 -DF2PY_REPORT_ON_ARRAY_COPY=1")

import md 



md.mod.no_atoms = natoms

md.mod.A = A_no
md.mod.Z = Z_no

for i in range(rx_ext):
	md.mod.xyz = coo
	print coo
	md.mod.foo()

	# create the input to gaussian
	# run gaussian script
	# pipeout the output
	# pass it as gradient to md.mod.grad
	
	coo = md.mod.xyz 
			







