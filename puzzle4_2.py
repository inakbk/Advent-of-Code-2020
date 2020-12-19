import numpy as np
import sys
import re

"""
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

Your job is to count the passports where all required fields are both present and valid according to the above rules.
"""
fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']

def check_entries(category,entr):
    cnt=1
    for i in range(len(entr)):
        #print(category[i],entr[i])
        if category[i] == fields[0] and not (1920 <= int(entr[i]) <= 2002):
            #byr (Birth Year) - four digits; at least 1920 and at most 2002.
            cnt = 0
            #print(entr[i],category[i])
        elif category[i] == fields[1] and not (2010 <= int(entr[i]) <= 2020):
            #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
            cnt = 0
        elif category[i] == fields[2] and not (2020 <= int(entr[i]) <= 2030):
            #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
            cnt = 0
        elif category[i] == fields[3]:
            #hgt (Height) - a number followed by either cm or in:
            #    If cm, the number must be at least 150 and at most 193.
            #    If in, the number must be at least 59 and at most 76.
            unit = entr[i][-2:]
            nr = entr[i][:-2]
            if unit not in ['cm','in']:
                cnt = 0
            elif unit == 'cm' and not (150 <= int(nr) <= 193):
                cnt = 0
            elif unit == 'in' and not (59 <= int(nr) <= 76):
                cnt = 0
        elif category[i] == fields[4]:
            #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
            e = entr[i][1:]
            if len(e) != 6:
                cnt = 0
            elif not bool(re.match('^[a-f0-9]+$', e)):
                cnt = 0
        elif category[i] == fields[5] and entr[i] not in ['amb','blu','brn','gry','grn','hzl','oth']:
            #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
            cnt = 0
        elif category[i] == fields[6]:
            #pid (Passport ID) - a nine-digit number, including leading zeroes.
            if len(entr[i]) != 9 or not entr[i].isdigit():
                cnt = 0
                
    return cnt

def check_passport(passport):
    cnt1=1
    cnt2=1
    f = []; x = []
    for line in passport:
        splt = line.split(' ')
        for entry in splt:
            f.append(entry.split(':')[0].strip())
            x.append(entry.split(':')[1].strip())
    for flds in fields:
        if flds not in f and flds != 'cid':
            #print(flds, "passport not valid")
            cnt1=0

    cnt2 = check_entries(f,x)
    
    cnt = min(cnt1,cnt2)
    if len(f) < 7 or len(f) > 8:
        cnt = 0 
    return cnt

with open('day4.in','r') as infile:
	lines = infile.readlines()

counter = 0
passport = []
for i in range(len(lines)):
    line = lines[i]
    if line == '\n':
        #print('----new passport')
        #print(passport)
        cnt = check_passport(passport)
        if cnt == 1:
            print("Success:", passport)
        counter += cnt
        passport = []
    else:
        passport.append(line)

    if i==len(lines)-1:
        #print('----new passport')
        #print(passport)
        cnt = check_passport(passport)
        counter += cnt

print("Nr of valid passports:", counter)



