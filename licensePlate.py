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

# def areIn(letters, word):
#     wordIter = iter(word)    
#     try:
#         for letter in letters:
#             while True:
#                 char = next(wordIter)
#                 if char == letter:
#                     break
#     except Exception:
#         return False
#     return True

def areIn(regex, word):
    return bool(regex.search(word))

with open(wordFile, 'r') as f:
    allWords = [w.rstrip() for w in f]

@profile    
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

a1 = np.array()
            
missing = list(findMissing(allWords[:5], ascii_lowercase))

print(len(missing))

c = Counter(word[0] for word in missing)

# print(c)