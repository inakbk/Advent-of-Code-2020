import numpy as np
import sys

def count_agree(persons):
	agree = 0
	if len(persons) == 1:
		agree = len(persons[0])
	else:
		first_pers = persons[0]
		for q in first_pers:
			ag = np.zeros(len(persons)-1)
			for i in range(1,len(persons)):
				if q in persons[i]:
					ag[i-1] = 1
			if np.sum(ag) == len(persons)-1:
				agree +=1
	return agree

with open('day6.in','r') as infile:
	lines = infile.readlines()

sum_of_counts = 0
persons = []
for line in lines:
	if line == '\n':
		agree = count_agree(persons)
		sum_of_counts += agree
		print("count=",agree,persons)
		persons = []
	else:
		persons.append(line.strip())

agree = count_agree(persons)
sum_of_counts += agree

print("count=",agree,persons,"--> Last one, DONE!	")

print("Sum=",sum_of_counts)


