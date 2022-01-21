""" File for testing HW1 implementation against HW2 implementation
"""

#   Add other count characters instance to the python path so it can be imported
import sys
sys.path.insert(0, "C:\\Users\\Zac\\GitHub\\cpsc313\hw1")

import time
import CountWords
from mr_count_words import countWords, findWords
from Logger import Logger

__version__ = '1.0'
__author__ = 'Zac Foteff'

FILEPATH = "word_lists"

logger = Logger('hw2InstanceComparison', 'hw2')

def test_empty_file():
    assert 0 == 0