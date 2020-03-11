# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 11:16:04 2020

test_licensePlate.py

@author: lvanhulle
"""

import licensePlate as lp
import unittest
from itertools import product

class Test(unittest.TestCase):
    
    def testAreIn(self):
        self.assertTrue(lp.areIn('abc', 'zazbzc')) # spread apart
        self.assertTrue(lp.areIn('abc', 'zabc')) # at the end
        self.assertTrue(lp.areIn('abc', 'abcz')) # at the begining
        self.assertTrue(lp.areIn('abc', 'aabbcc')) # repeated in word
        
        self.assertFalse(lp.areIn('abc', 'cab')) # wrong order
        self.assertFalse(lp.areIn('ood', 'world')) # repeat in letters
        self.assertFalse(lp.areIn('abc', 'xyz')) # no matching
        
    def testFindMissing(self):
        words = ['world', 'abc']
        letters = 'ord'
        missing = set(product(letters, repeat=3)) - {tuple(letters)}
        
        returnedMissing = set(l for l in lp.findMissing(words, letters))

        self.assertEqual(missing, returnedMissing)
        
        
if __name__ == '__main__':
    unittest.main()