import numpy as np 
import sys

with open('day7.in','r') as infile:
	lines = infile.readlines()

colors = {}

for line in lines:
	col = line.split('bags')[0].strip()
	contain = line.split('contain')[1].strip()[:-1].split(', ')
	subcols = []
	for c in contain:
		if not c.startswith('no other'):
			subcols.append(c.split('bag')[0].strip())
		else:
			subcols.append(c.split('bag')[0].strip())
	colors.update({col:subcols}) 

#print(colors)

tree_end = []
for key in colors:
	if colors[key] == ['no other']:
		tree_end.append(key)
print("End of tree bags:",tree_end)


def walk_tree(tree,parent_node,parent_nr,parent_pos,val_dict):
	""" leste litt på på wiki om binære trær og ikke binære
	Pre-order (NLR)
	1. Perform pre-order operation.
    2. For each i from 1 to the number of children do:
        Visit i-th, if present.
        Perform in-order operation.
    3. Perform post-order operation.

    preorder(node)
    	if (node == null)
    	    return
    	visit(node)
    	preorder(node.left)
    	preorder(node.right)
	"""
	if parent_node in tree_end:
		pos = parent_pos
		return pos,val_dict

	N_nodes = len(tree[parent_node])	
	children = tree[parent_node]
	for i in range(N_nodes):
		child = children[i][2:]
		child_nr = int(children[i][:2])
		pos = parent_pos + str(i)
		val_dict.update({pos:child_nr}) 
		print(child,":",child_nr,"--> position:",pos)
		pos,val_dict = walk_tree(tree,child,child_nr,pos,val_dict)

	return pos,val_dict

color = 'shiny gold'
print("*START*\n", color)
val_dict = {}
pos,val_dict = walk_tree(colors,color,1,'',val_dict)
print("----")
print(val_dict)

print("----")
counter = 0
for key in val_dict:	
	if len(key) > 1:
		c = val_dict[key[:len(key)+1]]
		for i in range(1,len(key)):
			c = c*val_dict[key[:i]]
			#print("(c=",c,"val=",val_dict[key[:i]],"pos=",key[:i],")")
		counter += c
		#print("counter=",counter,"val=",val_dict[key],"pos=",key)
	else:
		counter += val_dict[key]
		#print("counter=",counter,"val=",val_dict[key],"pos=",key,"(here)")

print(counter)
