import requests
import time
from random import randint
from mr_count_words import findWords
from Logger import Logger

logger = Logger("findWordFuncTests", "hw2")

WORDLIST_FILEPATH = "C:\\Users\\Zac\\GitHub\\cpsc313\\hw2\\word_lists\\test\\"
RAND_WORDS_API_URL = "https://random-word-api.herokuapp.com/"
EXPECTED_OUTPUT = {
    'empty.txt': 0,
    'single_word.txt': 1,
    '500_words.txt': 500,
    'large_list.txt': 370103
}

def test_empty_file():
    test_file = 'empty.txt'
    start_time = time.perf_counter()
    word_list = findWords(f"{WORDLIST_FILEPATH}{test_file}")
    assert len(word_list) == EXPECTED_OUTPUT[test_file]
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed empty file test in {elapsed_time:.5f} seconds")
    
def test_single_word():
    test_file = 'single_word.txt'
    start_time = time.perf_counter()
    word_list = findWords(f"{WORDLIST_FILEPATH}{test_file}")
    assert len(word_list) == EXPECTED_OUTPUT[test_file]
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed single word test in {elapsed_time:.5f} seconds")
    
def test_500_words():
    test_file = '500_words.txt'
    start_time = time.perf_counter()
    word_list = findWords(f"{WORDLIST_FILEPATH}{test_file}")
    assert len(word_list) == EXPECTED_OUTPUT[test_file]
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed 500 word test in {elapsed_time:.5f} seconds")
    
def test_large_file():
    test_file = 'large_list.txt'
    start_time = time.perf_counter()
    word_list = findWords(f"{WORDLIST_FILEPATH}{test_file}")
    assert len(word_list) == EXPECTED_OUTPUT[test_file]
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed large file test in {elapsed_time:.5f} seconds")
    
    
def test_random_file_size():
    filename = 'randomly_generated.txt'
    num_words = randint(100, 1000)
    res = requests.get(f"{RAND_WORDS_API_URL}word?number={num_words}")
    with open(f"{WORDLIST_FILEPATH}{filename}", "w") as current_file:
        [current_file.write(word) for word in res.text]
    
    logger.log(f"{RAND_WORDS_API_URL}word?number={num_words}")
    logger.log(res.json)