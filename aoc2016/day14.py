#!/usr/bin/env python3

import fileinput
import hashlib

salt = ''

for line in fileinput.input():
    salt = line.strip()

def md5(i):
    return hashlib.md5((salt + str(i)).encode('utf-8')).hexdigest()

def checkNple(s, n):
    i = 0
    while i < len(s):
        char = s[i]
        consecutive = 0
        while i < len(s) and s[i] == char: 
            consecutive += 1
            i += 1
        if consecutive >= n:
            return char
    return False

def checkTriple(s):
    return checkNple(s, 3)

def checkPentuple(s):
    return checkNple(s, 5)

def checkKey(n):
    char = checkTriple(md5(n))
    if char != False:
        for i in range(n + 1, n + 1001):
            if char * 5 in md5(i):
                return True
    return False

i = 0
keysFound = 0
while keysFound < 64:
    if checkKey(i):
        keysFound += 1
    i += 1

print(i - 1)

