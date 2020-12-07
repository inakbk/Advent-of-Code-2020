# The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); 
# start by counting all the trees you would encounter for the slope right 3, down 1:

# From your starting position at the top-left, check the position that is right 3 and down 1. 
# Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

import numpy as np
import sys

kart = np.genfromtxt('day3.in',dtype='str',comments='0')
N = len(kart[0])
#print(N)

def walk_one_step(next_line,x_prev,x_step,counter):
	x_now = x_prev + x_step
	if x_now >= N:
		x_now = x_now - N
	pos = next_line[x_now]
	if pos == '#':
		# Hit a tree
		counter += 1
		#print(line[:x_now] + 'X' + line[x_now+1:])#, ':', line)
	#else:
	#	print(line[:x_now] + 'O' + line[x_now+1:])#, ':', line)
	return x_now, counter

"""
# Part 1:
x_prev = 0
x_step = 3
cnt = 0
for line in kart[1:]:
	x_now, cnt = walk_one_step(line,x_prev,x_step,cnt)
	x_prev = x_now

print(cnt)
"""

"""
    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""
print(kart[0], "(first line)")

x_steps = [1,3,5,7,1]
down = [1,1,1,1,2]
skips = [0,0,0,0,1]
cnts = np.zeros(len(x_steps))
answer = 1

for i in range(len(x_steps)):
	x_step = x_steps[i]
	d = down[i]
	skip = skips[i]
	x_prev = 0
	cnt = 0
	for line in kart[1:]:
		if skip == 1:
			skip = 0
		else:
			x_now, cnt = walk_one_step(line,x_prev,x_step,cnt)
			x_prev = x_now
			skip = skips[i]

	print(cnt)
	cnts[i] = cnt
	answer = answer*cnt

print(answer)

