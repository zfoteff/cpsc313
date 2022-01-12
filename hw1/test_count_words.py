""" Main file for testing the HW1 implementation
"""

__version__ = '0.1'
__author__ = 'Zac Foteff'

import time
from Loggers import TestLogger
from CountWords import countWords
logger = TestLogger("hw1")

TEST_FILES = [
    'single_word.txt', 'long_word.txt', 'alpha.txt', 
    '500_words.txt', 'every_paragraph.txt', 'empty.txt'
]

EXPECTED_OUTPUTS = {
    'empty.txt': 0,
    'single_word.txt': 1,
    'long_word.txt': 1,
    '500_words.txt': 500,
    'every_paragraph': 10
}

def getDictSum(word_list):
    return sum(word_list.values())

def test_empty_file():
    """ Test that an empty file returns 0 words
    """
    test_file = "empty.txt"
    start_time = time.process_time()
    word_list = countWords(f"mock_lists/{test_file}")
    assert getDictSum(word_list) == EXPECTED_OUTPUTS[test_file]
    elapsed_time = time.process_time() - start_time
    logger.log(f"Completed empty file test in {elapsed_time} seconds")

    
def test_single_word():
    """ Test that a single word returns 1 word
    """
    test_file = "single_word.txt"
    start_time = time.process_time()
    word_list = countWords(f"mock_lists/{test_file}")
    assert getDictSum(word_list) == EXPECTED_OUTPUTS[test_file]
    elapsed_time = time.process_time() - start_time
    logger.log(f"Completed single word test in {elapsed_time} seconds")

def test_long_word():
    """ Test that an abnormally long word returns 1 word
    """
    test_file = "long_word.txt"
    start_time = time.process_time()
    word_list = countWords(f"mock_lists/{test_file}")
    assert getDictSum(word_list) == EXPECTED_OUTPUTS[test_file]
    elapsed_time = time.process_time() - start_time
    logger.log(f"Completed long word test in {elapsed_time} seconds")

def test_500_words_file():
    """ Test that a file with 500 words returns 500 words
    """
    test_file = "500_words.txt"
    start_time = time.process_time()
    word_list = countWords(f"mock_lists/{test_file}")
    assert getDictSum(word_list) == EXPECTED_OUTPUTS[test_file]
    elapsed_time = time.process_time() - start_time
    logger.log(f"Completed 500 words test in {elapsed_time} seconds")

def test_same_expected_output():
    """ 
    Test that a 2 instances of the count_words function returns the same amount of words
    on an file with an unknown amount of words
    """
    test_file = "alpha.txt"
    start_time = time.process_time()
    word_list_1 = countWords(f"mock_lists/{test_file}")
    word_list_1_count = getDictSum(word_list_1)
    word_list_2 = countWords(f"mock_lists/{test_file}")
    word_list_2_count = getDictSum(word_list_2)
    assert word_list_1_count == word_list_2_count
    elapsed_time = time.process_time() - start_time
    logger.log(f"Completed same expected output test in {elapsed_time} seconds")