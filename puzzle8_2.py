import numpy as np 
import sys
"""
nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp).
"""

def check_lines(lines):
	N = len(lines)
	line_nrs = []
	accumulator = 0
	loop = False

	i=0
	while not loop:
		line = lines[i].strip()
		instruction = line.split()[0]
		value = line.split()[1]
		
		if i in line_nrs:
			print("Looping!",instruction,value,'accumulator=',accumulator)
			loop = True
			break

		line_nrs.append(i)
		if instruction == 'acc':
			accumulator += int(value)
			print(instruction,value,'acc=',accumulator)
			i+=1
		elif instruction == 'jmp':
			print(instruction,value,'acc=',accumulator)
			i+=int(value)
		elif instruction == 'nop':
			print(instruction,value,'acc=',accumulator)
			i+=1
		
		if i == N:
			print("DONE")
			break

	return accumulator,loop

with open('day8.in','r') as infile:
	lines = infile.readlines()

instr = []
vals = []
for l in lines:
	instr.append(l.split()[0].strip())
	vals.append(l.split()[1].strip())
instr = np.array(instr)
vals = np.array(vals)


ind_nop = np.argwhere(instr=='nop').flatten()
ind_jmp = np.argwhere(instr=='jmp').flatten()
print(ind_nop,ind_jmp)

counter = 0
loop = True
while loop:
	for k in ind_jmp:
		lines_copy = np.copy(lines)
		lines_copy[k] = 'nop '+vals[k]
		print("---change",lines[k].strip(),"-->",lines_copy[k],k)
		accumulator,loop = check_lines(lines_copy)
		if loop==False:
			break
		counter += 1
	# Flaks for glemte å kommentere inn dette!!!
	#for k in ind_nop:
	#	lines_copy = np.copy(lines)
	#	lines_copy[k] = 'jmp '+vals[k]
	#	print("---change",lines[k].strip(),"-->",lines_copy[k])
	#	accumulator,loop = check_lines(lines_copy)
	#	if loop==False:
	#		break
	#	counter += 1
	
	if counter >3:
		break
print(accumulator)



