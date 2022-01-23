import sys
import time
from mr_count_words import findWords
from Logger import Logger

logger = Logger('findWordFuncTests', 'hw2')

WORDLIST_FILEPATH = "..\\word_lists\\test\\"

EXPECTED_OUTPUT = {
    'empty.txt': 0,
    'single_word.txt': 1,
    '500_words.txt': 500,
    'large_list.txt': 370085
}

def test_empty_file():
    test_file = 'empty.txt'
    start_time = time.perf_counter()
    word_list = findWords(f"{WORDLIST_FILEPATH}{test_file}")
    assert len(word_list) == EXPECTED_OUTPUT['empty.txt']
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed empty file test in {elapsed_time:.5f} seconds")