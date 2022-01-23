""" Main file for unit testing HW2 implementation
"""

import time
from Logger import Logger
from mr_count_words import countWords, findWords

__version__ = '1.0'
__author__ = 'Zac Foteff'

FILEPATH = "word_lists"

logger = Logger('hw2Unittest', 'hw2')

def test_empty_file():
    assert 0 == 0