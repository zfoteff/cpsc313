""" File for testing HW1 implementation against HW2 implementation
"""

#   Add other count characters instance to the python path so it can be imported
import sys
sys.path.append("C:\\Users\\Zac\\GitHub\\cpsc313\\hw1\\")

import time
import CountWords
from basicMR import SimpleMapReduce
from mr_count_words import countWords, findWords
from Logger import Logger

__version__ = '1.0'
__author__ = 'Zac Foteff'

FILEPATH = "word_lists"

logger = Logger('InstanceComparison', 'hw2')

def test_empty_file():
    assert 0 == 0
    
def test_equal_on_same_input():
    pass
    
def test_not_equal_on_different_input():
    pass