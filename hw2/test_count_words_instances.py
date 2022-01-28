""" 
Testing HW1 implementation against HW2 implementation
"""

#   Add other count characters instance to the python path so it can be imported
import sys
sys.path.append("C:\\Users\\Zac\\GitHub\\cpsc313\\hw1\\")

import time
import requests
from CountWords import countWordsForFile
from random import randint
from basicMR import SimpleMapReduce
from mr_count_words import countWords, findWords
from Logger import Logger

__version__ = '1.0'
__author__ = 'Zac Foteff'

logger = Logger('InstanceComparison', 'hw2')

WORDLIST_FILEPATH = "C:/Users/Zac/GitHub/cpsc313/hw2/word_lists/test/"
WORDLIST_WINDOWS_FILEPATH = "C:\\Users\\Zac\\GitHub\\cpsc313\\hw2\\word_lists\\test\\"
RAND_WORDS_API_URL = "https://random-word-api.herokuapp.com/"
EXPECTED_OUTPUT = {
    'empty.txt': 0,
    'single_word.txt': 1,
    '500_words.txt': 500,
    'large_list.txt': 370085
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

def test_empty_file():
    """
    Assert both instances handle empty files properly
    """
    test_file = f"{WORDLIST_WINDOWS_FILEPATH}empty.txt"
    test_file_list = [f"{WORDLIST_FILEPATH}empty.txt"]
    start_time = time.perf_counter()
    
    #   First iteration
    type_1_start_time = time.perf_counter()
    type_1_result = countWordsForFile(test_file)
    assert type_1_result == EXPECTED_OUTPUT['empty.txt']
    type_1_elapsed_time = time.perf_counter() - type_1_start_time
    logger.log(f"Counted words using counter instance one in {type_1_elapsed_time} seconds. Found {type_1_result} words")
    
    #   Second iteration
    type_2_start_time = time.perf_counter()
    reduce = SimpleMapReduce(findWords, countWords)
    type_2_result = sum_test_result_wordcounts(reduce(test_file_list))
    assert type_2_result == EXPECTED_OUTPUT['empty.txt']
    type_2_elapsed_time = time.perf_counter() - type_2_start_time
    logger.log(f"Counted words using counter instance two in {type_2_elapsed_time} seconds. Found {type_2_result} words")
    
    #   Assert results are the same
    assert type_1_result == type_2_result
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed empty word comparision test in {elapsed_time} seconds")
    
def test_single_word_file():
    """
    Assert both instances handle single words appropriately
    """
    test_file = f"{WORDLIST_WINDOWS_FILEPATH}single_word.txt"
    test_file_list = [f"{WORDLIST_FILEPATH}single_word.txt"]
    start_time = time.perf_counter()
    
    #   First iteration
    type_1_start_time = time.perf_counter()
    type_1_result = countWordsForFile(test_file)
    assert type_1_result == EXPECTED_OUTPUT["single_word.txt"]
    type_1_elapsed_time = time.perf_counter() - type_1_start_time
    logger.log(f"Counted words using counter instance one in {type_1_elapsed_time} seconds. Found {type_1_result} words")
    
    #   Second iteration
    type_2_start_time = time.perf_counter()
    reduce = SimpleMapReduce(findWords, countWords)
    type_2_result = sum_test_result_wordcounts(reduce(test_file_list))
    assert type_2_result == EXPECTED_OUTPUT["single_word.txt"]
    type_2_elapsed_time = time.perf_counter() - type_2_start_time
    logger.log(f"Counted words using counter instance two in {type_2_elapsed_time} seconds. Found {type_2_result} words")
    
    #   Assert results are the same
    assert type_1_result == type_2_result
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed single word comparision test {elapsed_time} seconds")
    
def test_large_file():
    """
    Assert both instances handle large file inputs
    """
    test_file = f"{WORDLIST_WINDOWS_FILEPATH}500_words.txt"
    test_file_list = [f"{WORDLIST_FILEPATH}500_words.txt"]
    start_time = time.perf_counter()
    
    #   First iteration
    type_1_start_time = time.perf_counter()
    type_1_result = countWordsForFile(test_file)
    assert type_1_result == EXPECTED_OUTPUT["500_words.txt"]
    type_1_elapsed_time = time.perf_counter() - type_1_start_time
    logger.log(f"Counted words using counter instance one in {type_1_elapsed_time} seconds. Found {type_1_result} words")
    
    #   Second iteration
    type_2_start_time = time.perf_counter()
    reduce = SimpleMapReduce(findWords, countWords)
    type_2_result = sum_test_result_wordcounts(reduce(test_file_list))
    assert type_2_result == EXPECTED_OUTPUT["500_words.txt"]
    type_2_elapsed_time = time.perf_counter() - type_2_start_time
    logger.log(f"Counted words using counter instance two in {type_2_elapsed_time} seconds. Found {type_2_result} words")
    
    #   Assert results are the same
    assert type_1_result == type_2_result
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed large file comparision test {elapsed_time} seconds")
    
def test_not_equal_on_different_input():
    """
    Assert both instances do not return the same thing when given different files
    """
    test_file = f"{WORDLIST_WINDOWS_FILEPATH}500_words.txt"
    test_file_list = [f"{WORDLIST_FILEPATH}large_list.txt"]
    start_time = time.perf_counter()
    
    #   First iteration
    type_1_start_time = time.perf_counter()
    type_1_result = countWordsForFile(test_file)
    assert type_1_result == EXPECTED_OUTPUT["500_words.txt"]
    type_1_elapsed_time = time.perf_counter() - type_1_start_time
    logger.log(f"Counted words using counter instance one in {type_1_elapsed_time} seconds. Found {type_1_result} words")
    
    #   Second iteration
    type_2_start_time = time.perf_counter()
    reduce = SimpleMapReduce(findWords, countWords)
    type_2_result = sum_test_result_wordcounts(reduce(test_file_list))
    assert type_2_result == EXPECTED_OUTPUT["large_list.txt"]
    type_2_elapsed_time = time.perf_counter() - type_2_start_time
    logger.log(f"Counted words using counter instance two in {type_2_elapsed_time} seconds. Found {type_2_result} words")
    
    #   Assert results are different
    assert type_1_result != type_2_result
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed single word comparision test {elapsed_time} seconds")
    
def test_random_file():
    """
    Assert both instances return the same result when given a large, random file
    """
    test_file = f"{WORDLIST_WINDOWS_FILEPATH}randomly_generated.txt"
    test_file_list = [f"{WORDLIST_FILEPATH}randomly_generated.txt"]
    num_words = randint(50, 200)
    res = requests.get(f"{RAND_WORDS_API_URL}word?number={num_words}")
    with open(test_file, "w") as current_file:
        [current_file.write(word.replace("[", '').replace("]", '').replace("\"", '').replace(",", " ")) for word in list(res.text)]
    
    start_time = time.perf_counter()
    
    #   First iteration
    type_1_start_time = time.perf_counter()
    type_1_result = countWordsForFile(test_file)
    assert type_1_result == num_words
    type_1_elapsed_time = time.perf_counter() - type_1_start_time
    logger.log(f"Counted words using counter instance one in {type_1_elapsed_time} seconds. Found {type_1_result} words")
    
    #   Second iteration
    type_2_start_time = time.perf_counter()
    reduce = SimpleMapReduce(findWords, countWords)
    type_2_result = sum_test_result_wordcounts(reduce(test_file_list))
    assert type_2_result == num_words
    type_2_elapsed_time = time.perf_counter() - type_2_start_time
    logger.log(f"Counted words using counter instance two in {type_2_elapsed_time} seconds. Found {type_2_result} words")
    
    #   Assert results are the same
    assert type_1_result == type_2_result
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed single word comparision test {elapsed_time} seconds")
    