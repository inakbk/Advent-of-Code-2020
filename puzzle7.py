import numpy as np 
import sys

def check_gold(rules,col_list):
	test = False
	if 'shiny gold' in col_list:
		test = True
	else:
		for col in col_list:
			if col != 'no other':
				test = check_gold(rules,rules[col])
				if test == True:
					break
	return test


with open('day7.in','r') as infile:
	lines = infile.readlines()

colors = {}

for line in lines:
	col = line.split('bags')[0].strip()
	contain = line.split('contain')[1].strip()[:-1].split(', ')
	subcols = []
	for c in contain:
		if not c.startswith('no other'):
			subcols.append(c[2:].split('bag')[0].strip())
		else:
			subcols.append(c.split('bag')[0].strip())
#	print(col,":",subcols)
	colors.update({col:subcols}) 
#print(colors)

#for key in a_dict:
#...     print(key, '->', a_dict[key])
counter = 0
for key in colors:
	test = check_gold(colors,colors[key])
	if test == True:
		print(key,"YEEES")
		counter += 1

print(counter)


