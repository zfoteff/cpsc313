""" File for testing HW1 implementation against HW2 implementation
"""

import time
from Logger import Logger
import mr_count_words
import "../hw1/CountWords"

__version__ = '1.0'
__author__ = 'Zac Foteff'

FILEPATH = "word_lists"

logger = Logger('Unittest', 'hw2')

def test_empty_file():
    assert 0 == 0