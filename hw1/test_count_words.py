""" Main file for testing the HW1 implementation
"""

__version__ = '1.1'
__author__ = 'Zac Foteff'

import time
from Logger import Logger
from CountWords import countWords

logger = Logger("test", "hw1")

EXPECTED_OUTPUTS = {
    'empty.txt': 0,
    'single_word.txt': 1,
    'long_word.txt': 1,
    '500_words.txt': 500,
    'every_paragraph': 10,
    'duplicates.txt': 2,
    'alt_spelling.txt': 1,
    'ignored.txt': 0
}

EXPECTED_DENSITY = {
    'single_word.txt': {
        'ZAC': 1
},
    'duplicates.txt': {
        'WORDS': 1,
        'WORD': 5
    }, 
    'alt_spelling.txt': {
        'WORD': 7
    }
}

def getDictSum(word_list) -> int:
    """ Get sum of all words in the word list dictionary

    Args:
        word_list (dict): Dictionary of words and their frequency in the file

    Returns:
        int: Total number of words in the file
    """
    return sum(word_list.values())

def test_empty_file():
    """ Test that an empty file returns 0 words
    """
    test_file = "empty.txt"
    start_time = time.time()
    word_list = countWords(f"mock_lists/{test_file}")
    assert getDictSum(word_list) == EXPECTED_OUTPUTS[test_file]
    elapsed_time = time.time() - start_time
    logger.log(f"Completed empty file test in {elapsed_time:.5f} seconds")
    
def test_single_word():
    """ Test that a single word returns 1 word
    """
    test_file = "single_word.txt"
    start_time = time.time()
    word_list = countWords(f"mock_lists/{test_file}")
    assert getDictSum(word_list) == EXPECTED_OUTPUTS[test_file]
    elapsed_time = time.time() - start_time
    logger.log(f"Completed single word test in {elapsed_time:.5f} seconds")

def test_long_word():
    """ Test that an abnormally long word returns 1 word
    """
    test_file = "long_word.txt"
    start_time = time.time()
    word_list = countWords(f"mock_lists/{test_file}")
    assert getDictSum(word_list) == EXPECTED_OUTPUTS[test_file]
    elapsed_time = time.time() - start_time
    logger.log(f"Completed long word test in {elapsed_time:.5f} seconds")

def test_500_words_file():
    """ Test that a file with 500 words returns 500 words
    """
    test_file = "500_words.txt"
    start_time = time.time()
    word_list = countWords(f"mock_lists/{test_file}")
    assert getDictSum(word_list) == EXPECTED_OUTPUTS[test_file]
    elapsed_time = time.time() - start_time
    logger.log(f"Completed 500 words test in {elapsed_time:.5f} seconds")

def test_duplicate_words():
    """ Test that duplicates of the same word are counted properly
    """
    test_file = "duplicates.txt"
    start_time = time.time()
    word_list = countWords(f"mock_lists/{test_file}")
    assert len(word_list) == EXPECTED_OUTPUTS[test_file]
    elapsed_time = time.time() - start_time
    logger.log(f"Completed duplicate words test in {elapsed_time:.5f} seconds")

def test_alt_spelling():
    """ Test that alternate spellings of the same word are counted properly
    """
    test_file = "alt_spelling.txt"
    start_time = time.time()
    word_list = countWords(f"mock_lists/{test_file}")
    assert len(word_list) == EXPECTED_OUTPUTS[test_file]
    elapsed_time = time.time() - start_time
    logger.log(f"Completed alternate spelling test in {elapsed_time:.5f} seconds")

def test_same_expected_output():
    """ 
    Test that a 2 instances of the count_words function returns the same amount of words
    on an file with an unknown amount of words
    """
    test_file = "alpha.txt"
    start_time = time.time()
    word_list_1 = countWords(f"mock_lists/{test_file}")
    word_list_1_count = getDictSum(word_list_1)
    word_list_2 = countWords(f"mock_lists/{test_file}")
    word_list_2_count = getDictSum(word_list_2)
    assert word_list_1_count == word_list_2_count
    elapsed_time = time.time() - start_time
    logger.log(f"Completed same expected output test in {elapsed_time:.5f} seconds")
  
def test_expected_density(): 
    """
    Test that the count_words function outputs a list of words with the correct amount of 
    occurences 
    """
    test_files = ['single_word.txt', 'duplicates.txt', 'alt_spelling.txt']
    start_time = time.time()
    
    for test in test_files:
        #   Iterate through all test file examples
        word_list = countWords(f"mock_lists/{test}")
        list_keys = word_list.keys()
        
        for key in list_keys:
            """
            Use each key in the compiled list of words, and check that the compiled 
            density matches the expected density
            """
            assert word_list[key] == EXPECTED_DENSITY[test][key]
        
    elapsed_time = time.time() - start_time
    logger.log(f"Completed expected density test in {elapsed_time:.5f} seconds")
    
def test_ignore_all_conjunctions():
    """
    Test that words included in the STOP_WORDS constant do not count to the wordlist
    """
    test_file = 'ignored.txt'
    start_time = time.time()
    word_list = countWords(f"mock_lists/{test_file}")
    assert len(word_list) == EXPECTED_OUTPUTS[test_file]
    elapsed_time = time.time() - start_time
    logger.log(f"Completed ignore all conjunctions test in {elapsed_time:.5f} seconds")