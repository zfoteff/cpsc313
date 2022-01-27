""" File for testing HW1 implementation against HW2 implementation
"""

#   Add other count characters instance to the python path so it can be imported
import sys
sys.path.append("C:\\Users\\Zac\\GitHub\\cpsc313\\hw1\\")

import time
from CountWords import countWordsForFile
from basicMR import SimpleMapReduce
from mr_count_words import countWords, findWords
from Logger import Logger

__version__ = '1.0'
__author__ = 'Zac Foteff'

logger = Logger('InstanceComparison', 'hw2')

WORDLIST_FILEPATH = "C:\\Users\\Zac\\GitHub\\cpsc313\\hw2\\word_lists\\test\\"
EXPECTED_OUTPUT = {
    'empty.txt': 0,
    'single_word.txt': 1,
    '500_words.txt': 500,
    'large_list.txt': 370103
}   

def test_empty_file():
    test_file = 'empty.txt'
    start_time = time.perf_counter()
    
    #   First iteration
    type_1_start_time = time.perf_counter()
    type_1_result = countWords(findWords(f"{WORDLIST_FILEPATH}{test_file}"))
    assert type_1_result == EXPECTED_OUTPUT[test_file]
    type_1_elapsed_time = time.perf_counter() - type_1_start_time
    logger.log(f"Counted words using counter instance one in {type_1_elapsed_time} seconds. Found {type_1_result} words")
    
    #   Second iteration
    type_2_start_time = time.perf_counter()
    type_2_result = countWordsForFile(f"{WORDLIST_FILEPATH}{test_file}")
    assert type_2_result == EXPECTED_OUTPUT[test_file]
    type_2_elapsed_time = time.perf_counter() - type_2_start_time
    logger.log(f"Counted words using counter instance two in {type_2_elapsed_time} seconds. Found {type_2_result} words")
    
    #   Assert results are the same
    assert type_1_result == type_2_result
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed empty word comparision test {elapsed_time} seconds")
    
def test_single_word_file():
    test_file = 'single_word.txt'
    start_time = time.perf_counter()
    
    #   First iteration
    type_1_start_time = time.perf_counter()
    type_1_result = countWords(findWords(f"{WORDLIST_FILEPATH}{test_file}"))
    assert type_1_result == EXPECTED_OUTPUT[test_file]
    type_1_elapsed_time = time.perf_counter() - type_1_start_time
    logger.log(f"Counted words using counter instance one in {type_1_elapsed_time} seconds. Found {type_1_result} words")
    
    #   Second iteration
    type_2_start_time = time.perf_counter()
    type_2_result = countWordsForFile(f"{WORDLIST_FILEPATH}{test_file}")
    assert type_2_result == EXPECTED_OUTPUT[test_file]
    type_2_elapsed_time = time.perf_counter() - type_2_start_time
    logger.log(f"Counted words using counter instance two in {type_2_elapsed_time} seconds. Found {type_2_result} words")
    
    #   Assert results are the same
    assert type_1_result == type_2_result
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed empty word comparision test {elapsed_time} seconds")
    
def test_large_file():
    test_file = '500_words.txt'
    start_time = time.perf_counter()
    
    #   First iteration
    type_1_start_time = time.perf_counter()
    type_1_result = countWords(findWords(f"{WORDLIST_FILEPATH}{test_file}"))
    assert type_1_result == EXPECTED_OUTPUT[test_file]
    type_1_elapsed_time = time.perf_counter() - type_1_start_time
    logger.log(f"Counted words using counter instance one in {type_1_elapsed_time} seconds. Found {type_1_result} words")
    
    #   Second iteration
    type_2_start_time = time.perf_counter()
    type_2_result = countWordsForFile(f"{WORDLIST_FILEPATH}{test_file}")
    assert type_2_result == EXPECTED_OUTPUT[test_file]
    type_2_elapsed_time = time.perf_counter() - type_2_start_time
    logger.log(f"Counted words using counter instance two in {type_2_elapsed_time} seconds. Found {type_2_result} words")
    
    #   Assert results are the same
    assert type_1_result == type_2_result
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed empty word comparision test {elapsed_time} seconds")
    
def test_not_equal_on_different_input():
    test_file_1 = 'single_word.txt'
    test_file_2 = '500_words.txt'
         
    #   First iteration
    start_time = time.perf_counter()
    assert countWordsForFile(f"{WORDLIST_FILEPATH}{test_file_1}") != countWords(findWords(f"{WORDLIST_FILEPATH}{test_file_2}"))
    elapsed_time = time.perf_counter()
    logger.log(f"Completed different input comparision test {elapsed_time} seconds")