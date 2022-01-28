"""
findWords functional tests
"""

import requests
import time
import sys
from random import randint
from mr_count_words import findWords
from Logger import Logger

logger = Logger("FindWordFuncTests", "hw2")

WORDLIST_FILEPATH = "C:\\Users\\Zac\\GitHub\\cpsc313\\hw2\\word_lists\\test\\"
RAND_WORDS_API_URL = "https://random-word-api.herokuapp.com/"
EXPECTED_OUTPUT = {
    'empty.txt': 0,
    'single_word.txt': 1,
    '500_words.txt': 500,
    'large_list.txt': 370085
}

def test_returns_list():
    """
    Assert findWords method returns a list
    """
    test_file = '500_words.txt'
    start_time = time.perf_counter()
    word_list = findWords(f"{WORDLIST_FILEPATH}{test_file}")
    assert type(word_list) == list
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed assert returns list in {elapsed_time}")

def test_empty_file():
    """
    Assert findWords method handles empty files properly
    """
    test_file = 'empty.txt'
    start_time = time.perf_counter()
    word_list = findWords(f"{WORDLIST_FILEPATH}{test_file}")
    assert len(word_list) == EXPECTED_OUTPUT[test_file]
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed empty file test in {elapsed_time:.5f} seconds")
    
def test_single_word():
    """
    Assert findWords method functions properly when it encounters a single word
    """
    test_file = 'single_word.txt'
    start_time = time.perf_counter()
    word_list = findWords(f"{WORDLIST_FILEPATH}{test_file}")
    assert len(word_list) == EXPECTED_OUTPUT[test_file]
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed single word test in {elapsed_time:.5f} seconds")
    
def test_500_words():
    """
    Assert findWords method functions properly when it encounters a known amount of words
    """
    test_file = '500_words.txt'
    start_time = time.perf_counter()
    word_list = findWords(f"{WORDLIST_FILEPATH}{test_file}")
    assert len(word_list) == EXPECTED_OUTPUT[test_file]
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed 500 word test in {elapsed_time:.5f} seconds")
    
def test_large_file():
    """
    Assert findWords method functions properly with large files
    """
    test_file = 'large_list.txt'
    start_time = time.perf_counter()
    word_list = findWords(f"{WORDLIST_FILEPATH}{test_file}")
    assert len(word_list) == EXPECTED_OUTPUT[test_file]
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed large file test in {elapsed_time:.5f} seconds")
    
def test_random_file_size():
    """
    Assert findWords method functions properly when it is given a large, random word file
    """
    test_file = 'randomly_generated.txt'
    num_words = randint(50, 200)
    res = requests.get(f"{RAND_WORDS_API_URL}word?number={num_words}")
    with open(f"{WORDLIST_FILEPATH}{test_file}", "w") as current_file:
        [current_file.write(word.replace("[", '').replace("]", '').replace("\"", '').replace(",", " ")) for word in list(res.text)]
    
    start_time = time.perf_counter()
    word_list = findWords(f"{WORDLIST_FILEPATH}{test_file}")
    assert len(word_list) == num_words
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed large file test in {elapsed_time:.5f} seconds")