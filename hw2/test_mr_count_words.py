""" Main file for unit testing HW2 implementation
"""

import time
from Logger import Logger
from mr_count_words import countWords, findWords
from basicMR import SimpleMapReduce

__version__ = '1.0'
__author__ = 'Zac Foteff'

FILEPATH = "word_lists"

logger = Logger('MRUnittest', 'hw2')

WORDLIST_FILEPATH = "C:\\Users\\Zac\\GitHub\\cpsc313\\hw2\\word_lists\\test\\"
EXPECTED_OUTPUT = {
    'empty.txt': 0,
    'single_word.txt': 1,
    '500_words.txt': 500,
    'large_list.txt': 370103
}   

def test_returns_int():
    files_to_test = ['empty.txt']
    start_time = time.perf_counter()
    reduce = SimpleMapReduce(countWords, findWords)
    test_result = reduce(files_to_test.)
    assert type(test_result) == int
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed returns integer test in {elapsed_time} seconds")

def test_empty_file():
    files_to_test = ["empty.txt"]
    start_time = time.perf_counter()
    reduce = SimpleMapReduce(countWords, findWords)
    test_result = reduce([files_to_test])
    assert test_result == EXPECTED_OUTPUT['empty.txt']
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed returns integer test in {elapsed_time} seconds")
    
def test_single_word():
    test_file = "single_word.txt"
    start_time = time.perf_counter()
    test_result = SimpleMapReduce(countWords, findWords)
    assert test_result == EXPECTED_OUTPUT[test_file]
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed returns integer test in {elapsed_time} seconds")