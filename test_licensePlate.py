# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 11:16:04 2020

test_licensePlate.py

@author: lvanhulle
"""

import licensePlate as lp
import unittest
from itertools import product
import re

class Test(unittest.TestCase):
    
    def testAreIn(self):
        regex = re.compile(r'{}\w*{}\w*{}'.format(*'abc'))
        regex2 = re.compile(r'{}\w*{}\w*{}'.format(*'ood'))
        self.assertTrue(lp.areIn(regex, 'zazbzc')) # spread apart
        self.assertTrue(lp.areIn(regex, 'zabc')) # at the end
        self.assertTrue(lp.areIn(regex, 'abcz')) # at the begining
        self.assertTrue(lp.areIn(regex, 'aabbcc')) # repeated in word
        
        self.assertFalse(lp.areIn(regex, 'cab')) # wrong order
        self.assertFalse(lp.areIn(regex2, 'world')) # repeat in letters
        self.assertFalse(lp.areIn(regex, 'xyz')) # no matching
        
    def testFindMissing(self):
        words = ['world', 'abc']
        letters = 'ord'
        missing = set(product(letters, repeat=3)) - {tuple(letters)}
        
        returnedMissing = set(l for l in lp.findMissing(words, letters))

        self.assertEqual(missing, returnedMissing)
        
        
if __name__ == '__main__':
    unittest.main()