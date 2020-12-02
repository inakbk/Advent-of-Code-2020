#In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, 
# so the correct answer is 514579.

#Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

import numpy as np
import sys

nrs = np.genfromtxt('day1.in',dtype=int)
"""
for n in nrs:
	for m in nrs:
		if n+m==2020:
			print(n,m)
			print(m*n)
"""
# find three numbers in your expense report that meet the same criteria.
# what is the product of the three entries that sum to 2020?

for n in nrs:
	for m in nrs:
		for o in nrs:
			if n+m+o==2020:
				print(n,m,o)
				print(m*n*o)
				sys.exit()


