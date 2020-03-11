# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 07:58:11 2020

licensePlate.py

@author: lvanhulle
"""

from string import ascii_lowercase
from itertools import product
from numba import jit

wordFile = 'words_alpha.txt'

def areIn(letters, word):
    wordIter = iter(word)    
    try:
        for letter in letters:
            while True:
                char = next(wordIter)
                if char == letter:
                    break
    except Exception:
        return False
    return True

    # for letter in letters:
    #     while True:
    #         try:
    #             char = next(wordIter)
    #         except Exception:
    #             return False
    #         if char == letter:
    #             break
    # return True


with open(wordFile, 'r') as f:
    allWords = [w.rstrip() for w in f]

# @profile    
def findMissing(words, letters=ascii_lowercase):
    for plateLetters in product(letters, repeat=3):
        found = False
        for word in words:
            if areIn(plateLetters, word):
                found = True
                break
        if not found:
            yield plateLetters
            
missing = list(findMissing(allWords, ascii_lowercase))

print(len(missing))