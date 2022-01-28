"""
countWords functional tests
"""

import time
from random import randint
from mr_count_words import countWords
from Logger import Logger

logger = Logger("CountWordFuncTest", "hw2")

def test_returns_tuple():
    """
    Assert countWords method returns a tuple
    """
    test_data = ('a', [1])
    start_time = time.perf_counter()
    assert type(countWords(test_data)) == tuple
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed assert returns dictionary test in {elapsed_time:.5f} seconds.")
    
def test_single_element():
    """
    Assert countWords method functions as normal with a single element
    """
    test_data = ('a', [1])
    start_time = time.perf_counter()
    word_sums = countWords(test_data)
    assert word_sums == ('a', 1)
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed single element list test in {elapsed_time:.5f} seconds. Results: {word_sums}")
    
def test_large_iterable():
    """
    Assert countWords method functions as normal with a large iterable list
    """
    test_data = ('a', [1,1,1,1,1,1,1,1,1])
    start_time = time.perf_counter()
    word_sums = countWords(test_data)
    assert word_sums == ('a', 9)
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed large iterables mixed with small iterables test in {elapsed_time:.5f} seconds. Results: {word_sums}")
    
def test_random_iterable():
    """
    Assert countWords method functions as normal with a randomly large iterable
    """
    range_lower_bound = randint(10, 100)
    range_upper_bound = randint(range_lower_bound, 255)
    random_iterable = [1 for generate_value in range(range_lower_bound, range_upper_bound)]
    test_data = ('a', random_iterable)
    start_time = time.perf_counter()
    word_sums = countWords(test_data)
    assert word_sums[1] == len(random_iterable)
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed random iterable test in {elapsed_time:.5f} seconds. Results: {word_sums}")