
import numpy as np
import sys

def range_half(x1,x2,pos):
	if pos=='F' or pos=='L':
		#print(x1,x2)
		if x2-x1==1:
			x2 = x1
		else:
			x2 = int(x2 - (x2-x1)/2)
		#print(x1,x2)
	elif pos=='B' or pos=='R':
		#print(x1,x2)
		if x2-x1==1:
			x1 = x2
		else:
			x1 = round((x2-x1)/2 + x1)
		#print(x1,x2)
	return x1, x2

with open('day5.in','r') as infile:
	lines = infile.readlines()

sIDs = []
row_list = []
col_list = []
for seat in lines:
	row1 = 0
	row2 = 127
	col1 = 0
	col2 = 7
	seat = seat.strip()
	rows = seat[0:7]
	cols = seat[7:]
	#print(seat,rows,cols)

	for i in range(7):
		row1,row2 = range_half(row1,row2,rows[i])
	if row1!=row2:
		print("ERROR rows ")
	row = row1
	row_list.append(row)

	for i in range(3):
		col1,col2 = range_half(col1,col2,cols[i])
	if col1!=col2:
		print("ERROR cols")
	col = col1
	col_list.append(col)
	#print(col)

	sID = row*8 + col
	#print(sID)

	sIDs.append(sID)

sIDs = np.array(sIDs)

#print(np.max(sIDs))

#sIDs_sort = np.sort(sIDs)
all_rows = np.arange(0,128)
all_cols = np.arange(0,8)
print(col_list[0],len(row_list))

plane_map = np.zeros([128,8])

for i in range(len(col_list)):
	plane_map[row_list[i],col_list[i]] = 1
	#print(plane_map[row_list[i],col_list[i]],row_list[i],col_list[i])

for i in range(128):
	if i==64:
		print(i,plane_map[i,:])
		print(i*8 + 5)




