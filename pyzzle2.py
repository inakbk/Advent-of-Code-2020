# How many passwords are valid according to their policies?

# 4-5 r: rrrjr
# 9-10 x: pxcbpxxwkqjttx

import numpy as np
import sys
"""
p1,p2,passwords = np.genfromtxt('day2.in',usecols=(0,1,2),dtype='str',unpack=True)
N = len(p1)

range1 = np.zeros(N,dtype=int); range2 = np.zeros(N,dtype=int); letter = np.zeros(N,dtype='str')
for i in range(N):
	p = p1[i].split('-')
	range1[i] = p[0]
	range2[i] = p[1]
	letter[i] = p2[i][:-1]

n = 0
cnt = 0
for pw in passwords:
	if letter[n] in pw:
		c = 0
		for l in pw:
			if l == letter[n]:
				c+=1
		if c < range1[n] or c > range2[n]:
			print("pw failed test, pw=",pw,", letter=",letter[n],", range=",range1[n],range2[n])
			#sys.exit()
		else:
			cnt+=1
			#print("pw success test, pw=",pw,", letter=",letter[n],", range=",range1[n],range2[n])
			#sys.exit()
	n+=1

print(cnt) # 398
"""
# Each policy actually describes two positions in the password, where 1 means the first character,
# 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
# Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
# How many passwords are valid according to the new interpretation of the policies?

# 4-5 r: rrrjr
# 9-10 x: pxcbpxxwkqjttx

p1,p2,passwords = np.genfromtxt('day2.in',usecols=(0,1,2),dtype='str',unpack=True)
N = len(p1)

pos1 = np.zeros(N,dtype=int); pos2 = np.zeros(N,dtype=int); letter = np.zeros(N,dtype='str')
for i in range(N):
	p = p1[i].split('-')
	pos1[i] = int(p[0])-1
	pos2[i] = int(p[1])-1
	letter[i] = p2[i][:-1]

cnt = 0
for n in range(N):
	pw = passwords[n]
	if letter[n]==pw[pos1[n]] and letter[n]!=pw[pos2[n]]:
		print("pw success test, pw=",pw,", letter=",letter[n],", range=",pos1[n],pos2[n])
		cnt+=1
	elif letter[n]!=pw[pos1[n]] and letter[n]==pw[pos2[n]]:
		print("pw success test, pw=",pw,", letter=",letter[n],", range=",pos1[n],pos2[n])
		cnt+=1
	else:
		print("pw failed test, pw=",pw,", letter=",letter[n],", range=",pos1[n],pos2[n])

print(cnt)







