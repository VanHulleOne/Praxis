# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 07:58:11 2020

licensePlate.py

@author: lvanhulle
"""

from string import ascii_lowercase
from itertools import product
from numba import jit
from collections import Counter

import numpy as np

import re

wordFile = 'words_alpha.txt'

f1 = re.compile(r'o\w*l\w*d')

def areIn(regex, word):
    return bool(regex.search(word))

with open(wordFile, 'r') as f:
    allWords = [w.rstrip() for w in f]

#@profile    
def findMissing(words, letters=ascii_lowercase):
    for plateLetters in product(letters, repeat=3):
        regex = re.compile(r'{}\w*{}\w*{}'.format(*plateLetters))
        found = False
        for word in words:
            if areIn(regex, word):
                found = True
                break
        if not found:
            yield plateLetters

#@profile
def findMissing2(words, letters=ascii_lowercase):
    regs = np.array([re.compile(r'{}\w*{}\w*{}'.format(*trio)) for trio in
                     product(letters, repeat=3)])
    regs.resize(26,26,26)
    letters_dict = {c:i for c,i in zip(letters, range(len(letters)))}
    for word in words:
#        print('Word:', word)
        s = set(word)
        l1 = [letters_dict[c] for c in s]

        possibleRegs = regs[l1][:,l1][:,:,l1].flatten()
        possibleRegs = np.extract(possibleRegs, possibleRegs)

        for reg in possibleRegs:
#            print('Reg:', reg)
#            if not reg:
#                continue
            if areIn(reg, word):
                match = reg.pattern.replace(r'\w*', '')
                regs[letters_dict[match[0]],
                     letters_dict[match[1]],
                     letters_dict[match[2]]
                     ] = None

    return regs


#a1 = np.array()
            
#missing = list(findMissing(allWords[:100], ascii_lowercase))
#
#print(len(missing))
#
#c = Counter(word[0] for word in missing)

r = findMissing2(allWords[:])

# print(c)