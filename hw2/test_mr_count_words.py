""" 
Main file for testing HW2 map reduce implementation
"""

import time
import requests
from Logger import Logger
from random import randint
from mr_count_words import countWords, findWords
from basicMR import SimpleMapReduce

__version__ = '1.0'
__author__ = 'Zac Foteff'

logger = Logger('MRUnittest', 'hw2')

WORDLIST_FILEPATH = "C:/Users/Zac/GitHub/cpsc313/hw2/word_lists/test/"
RAND_WORDS_API_URL = "https://random-word-api.herokuapp.com/"
EXPECTED_OUTPUT = {
    'empty.txt': [],
    'single_word.txt': 1,
    '500_words.txt': 500,
    'large_list.txt': 370103
}   

def sum_test_result_wordcounts(result_list):
    """
    Helper method to iterate through list of tuples and get a sum of all words

    Args:
        result_list (list): iterable list of tuples populated with words and
        their corresponding wordcounts
    Return:
        int: total wordcount of the list
    """
    total_wordcount = 0
    for word_data in result_list:
        total_wordcount += word_data[1]
    return total_wordcount

def test_returns_list():
    """
    Assert that map reduce method returns a list
    """
    files_to_test = [f"{WORDLIST_FILEPATH}empty.txt"]
    start_time = time.perf_counter()
    reduce = SimpleMapReduce(findWords, countWords)
    test_result = reduce(files_to_test)
    assert type(test_result) == list
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed returns integer test in {elapsed_time} seconds. Result: {test_result}")

def test_empty_file():
    """
    Assert that empty file returns an empty list of words
    """
    files_to_test = [f"{WORDLIST_FILEPATH}empty.txt"]
    start_time = time.perf_counter()
    reduce = SimpleMapReduce(findWords, countWords)
    test_result = reduce(files_to_test)
    assert test_result == EXPECTED_OUTPUT['empty.txt']
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed returns integer test in {elapsed_time} seconds. Result: {test_result}")
    
def test_single_word():
    """
    Assert that map reduce functions as expected with a single word
    """
    files_to_test = [f"{WORDLIST_FILEPATH}single_word.txt"]
    start_time = time.perf_counter()
    reduce = SimpleMapReduce(findWords, countWords)
    test_result = reduce(files_to_test)
    assert sum_test_result_wordcounts(test_result) == EXPECTED_OUTPUT['single_word.txt']
    assert test_result[0][0] == 'ZAC'
    assert test_result[0][1] == 1
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed single word test in {elapsed_time} seconds. Result: {test_result}")
    
def test_500_words():
    """
    Assert that the map reduce functions as expected with a large list of words
    """
    files_to_test = [f"{WORDLIST_FILEPATH}500_words.txt"]
    start_time = time.perf_counter()
    reduce = SimpleMapReduce(findWords, countWords)
    test_result = reduce(files_to_test)
    assert sum_test_result_wordcounts(test_result) == EXPECTED_OUTPUT['500_words.txt']
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed 500 words test in {elapsed_time} seconds. Result: {test_result}")
    
def test_random_words():
    """
    Assert that map reduce functions as expecte when it encounters a large random list of words
    """
    files_to_test = [f"{WORDLIST_FILEPATH}randomly_generated.txt"]
    num_words = randint(50, 200)
    res = requests.get(f"{RAND_WORDS_API_URL}word?number={num_words}")
    with open(f"{WORDLIST_FILEPATH}randomly_generated.txt", "w") as current_file:
        [current_file.write(word.replace("[", '').replace("]", '').replace("\"", '').replace(",", " ")) for word in list(res.text)]
    
    start_time = time.perf_counter()
    reduce = SimpleMapReduce(findWords, countWords)
    test_result = reduce(files_to_test)
    assert sum_test_result_wordcounts(test_result) == num_words
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed random words test in {elapsed_time} seconds. Result: {test_result}")