import numpy as np
import sys

with open('day6.in','r') as infile:
	lines = infile.readlines()

sum_of_counts = 0
answers = []
for line in lines:
	
	if line == '\n':
		unique = []
		ans_join = ''.join(answers)
		for a in ans_join:
			print(a)
			if a not in unique:
				unique.append(a)
		sum_of_counts += len(unique)

		print(''.join(answers),"count=",len(unique),"--> New group")
		answers = []
	else:
		answers.append(line.strip())

unique = []
ans_join = ''.join(answers)
for a in ans_join:
	print(a)
	if a not in unique:
		unique.append(a)
sum_of_counts += len(unique)
print(''.join(answers),"count=",len(unique),"--> Last one, DONE!	")

print("Sum=",sum_of_counts)


