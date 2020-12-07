
import numpy as np
import sys

"""
Required fields:
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID) - optional

Example:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in

Count the number of valid passports - those that have all required fields. 
Treat cid as optional. In your batch file, how many passports are valid?
"""

with open('day4_ex.in','r') as infile:
	lines = infile.readlines()

#print(lines)

fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']

n_fields = 0
for line in lines:
	if line == '\n':
		print('new passport')
	else:
		print(line)
		sys.exit()



