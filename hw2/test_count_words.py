import time
from random import randint
from mr_count_words import countWords
from Logger import Logger

logger = Logger("CountWordFuncTest", "hw2")

def test_returns_int():
    data = []
    start_time = time.perf_counter()
    assert type(countWords(data)) == int
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed assert returns int test in {elapsed_time:.5f} seconds")

def test_empty_list():
    data = []
    start_time = time.perf_counter()
    word_count = countWords(data)
    assert word_count == 0
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed empty list test in {elapsed_time:.5f} seconds")
    
def test_single_element_list():
    data = [['a', 1]]
    start_time = time.perf_counter()
    word_count = countWords(data)
    assert word_count == 1
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed single element list test in {elapsed_time:.5f} seconds")
    
def test_normal_list():
    data = [
        ['a', 1], ['b', 1], ['c', 1], ['d', 1], ['e', 1], ['f', 1], ['g', 1],
        ['h', 1], ['i', 1], ['j', 1], ['k', 1], ['l', 1], ['m', 1], ['n', 1]
    ]
    start_time = time.perf_counter()
    word_count = countWords(data)
    assert word_count == 14
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed standard list test in {elapsed_time:.5f} seconds")
    
def test_duplicate_elements():
    data = [['a', 1], ['a', 1], ['a', 1], ['a', 1], ['a', 1], ['a', 1], ['a', 1]]
    start_time = time.perf_counter()
    word_count = countWords(data)
    assert word_count == 7
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed duplicate elements test in {elapsed_time:.5f} seconds")