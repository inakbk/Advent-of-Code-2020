import numpy as np 
import sys
"""
nop +0  | 1
acc +1  | 2, 8(!)
jmp +4  | 3
acc +3  | 6
jmp -3  | 7
acc -99 |
acc +1  | 4
jmp -4  | 5
acc +6  |


nop +0  | 1
acc +1  | 2, 8(!)
jmp +4  | 3
acc +1  | 4
jmp -4  | 5
acc +3  | 6
jmp -3  | 7
acc +1  | 8(!)

acc -99 |
acc +6  |
"""

with open('day8.in','r') as infile:
	lines = infile.readlines()

N = len(lines)
line_nrs = np.ones(N)*-99
accumulator = 0

i=0
for n in range(N):
	line = lines[i].strip()
	instruction = line.split()[0]
	value = line.split()[1]
	
	if i in line_nrs:
		print("DONE",instruction,value,'accumulator=',accumulator)
		break
	line_nrs[n] = i
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





