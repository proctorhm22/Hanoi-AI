"""
Docstring for python_sol.game_test
"""

# TODO: actually write unit tests

import unittest

# add script directory to import path even if the project was opened as a single
# file instead of as a directory or a project
import os
import sys
scriptdir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(scriptdir)

# import the Temperature class from temperature.py
from hanoi import Hanoi

class BasicTest(unittest.TestCase):
    def test_valid_constructor(self):
        game = Hanoi(num_disks=7)
        self.assertEqual(game.num_disks, 7)
        self.assertEqual(game.opt_moves_count, 2**7-1)
    
    # def test_invalid_constructor(self):
    #     with self.assertRaises(ValueError):
    #         Temperature()
    #     with self.assertRaises(ValueError):
    #         Temperature(C=100, F=212)
    #     with self.assertRaises(ValueError):
    #         Temperature(F=212, K=373.15)
    #     with self.assertRaises(ValueError):
    #         Temperature(C=100, K=373.15)
    #     with self.assertRaises(ValueError):
    #         Temperature(C=100, F=212, K=373.15)
    
    def test_valid_swap(self):
        pass

    def test_invalid_swap(self):
        pass

if __name__=='__main__':
    unittest.main()