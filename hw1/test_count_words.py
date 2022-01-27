""" Main file for testing the HW1 implementation
"""

__version__ = '1.3'
__author__ = 'Zac Foteff'
import sys
sys.path.insert(0, "C:\\Users\\Zac\\GitHub\\cpsc313\hw1\\CountWords.py")

import time
from Logger import Logger
from CountWords import countWords
from CountWords import mergeResults

logger = Logger("test", "hw1")

FILE_PATH = "word_lists"

EXPECTED_OUTPUTS = {
    'empty.txt': 0,
    'single_word.txt': 1,
    'long_word.txt': 1,
    '500_words.txt': 500,
    'every_paragraph': 10,
    'duplicates.txt': 2,
    'alt_spelling.txt': 1,
    'ignored.txt': 0,
    'mixed_ignored.txt': 5,
    'large_list.txt': 370085
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

def getDictSum(word_list):
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
    word_list = countWords(f"{FILE_PATH}/{test_file}")
    assert getDictSum(word_list) == EXPECTED_OUTPUTS[test_file]
    elapsed_time = time.time() - start_time
    logger.log(f"Completed empty file test in {elapsed_time:.5f} seconds")
    
def test_single_word():
    """ Test that a single word returns 1 word
    """
    test_file = "single_word.txt"
    start_time = time.time()
    word_list = countWords(f"{FILE_PATH}/{test_file}")
    assert getDictSum(word_list) == EXPECTED_OUTPUTS[test_file]
    elapsed_time = time.time() - start_time
    logger.log(f"Completed single word test in {elapsed_time:.5f} seconds")

def test_long_word():
    """ Test that an abnormally long word returns 1 word
    """
    test_file = "long_word.txt"
    start_time = time.time()
    word_list = countWords(f"{FILE_PATH}/{test_file}")
    assert getDictSum(word_list) == EXPECTED_OUTPUTS[test_file]
    elapsed_time = time.time() - start_time
    logger.log(f"Completed long word test in {elapsed_time:.5f} seconds")

def test_500_words_file():
    """ Test that a file with 500 words returns 500 words
    """
    test_file = "500_words.txt"
    start_time = time.time()
    word_list = countWords(f"{FILE_PATH}/{test_file}")
    assert getDictSum(word_list) == EXPECTED_OUTPUTS[test_file]
    elapsed_time = time.time() - start_time
    logger.log(f"Completed 500 words test in {elapsed_time:.5f} seconds")

def test_duplicate_words():
    """ Test that duplicates of the same word are counted properly
    """
    test_file = "duplicates.txt"
    start_time = time.time()
    word_list = countWords(f"{FILE_PATH}/{test_file}")
    assert len(word_list) == EXPECTED_OUTPUTS[test_file]
    elapsed_time = time.time() - start_time
    logger.log(f"Completed duplicate words test in {elapsed_time:.5f} seconds")

def test_alt_spelling():
    """ Test that alternate spellings of the same word are counted properly
    """
    test_file = "alt_spelling.txt"
    start_time = time.time()
    word_list = countWords(f"{FILE_PATH}/{test_file}")
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
    word_list_1 = countWords(f"{FILE_PATH}/{test_file}")
    word_list_1_count = getDictSum(word_list_1)
    word_list_2 = countWords(f"{FILE_PATH}/{test_file}")
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
        word_list = countWords(f"{FILE_PATH}/{test}")
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
    word_list = countWords(f"{FILE_PATH}/{test_file}")
    assert len(word_list) == EXPECTED_OUTPUTS[test_file]
    elapsed_time = time.time() - start_time
    logger.log(f"Completed ignore all conjunctions test in {elapsed_time:.5f} seconds")

def test_ignore_mixed_conjunctions():
    """
    Test that words included in the STOP_WORDS constant do not count towards the wordlist when
    mixed in with many other words
    """
    test_file = 'mixed_ignored.txt'
    start_time = time.time()
    start_time = time.time()
    word_list = countWords(f"{FILE_PATH}/{test_file}")
    assert len(word_list) == EXPECTED_OUTPUTS[test_file]
    elapsed_time = time.time() - start_time
    logger.log(f"Completed ignore all conjunctions test in {elapsed_time:.5f} seconds")

def test_large_wordlist():
    """
    Test that program behaves as expected when encountering large files
    """
    test_file = 'large_list.txt'
    start_time = time.time()
    word_list = countWords(f"{FILE_PATH}/{test_file}")
    assert len(word_list) == EXPECTED_OUTPUTS[test_file]
    elapsed_time = time.time() - start_time
    logger.log(f"Completed large file test in {elapsed_time:.5f} seconds")
    
def test_merge_empty_results():
    """
    Test that merging empty word lists returns an empty result
    """
    test_file = "empty.txt"
    start_time = time.time()
    destination = countWords(f"{FILE_PATH}/{test_file}")
    source = countWords(f"{FILE_PATH}/{test_file}")
    mergeResults(destination, source)
    assert destination == {}
    elapsed_time = time.time() - start_time
    logger.log(f"Completed merge empty results test in {elapsed_time:.5f} seconds")

def test_merge_same_results():
    """
    Test that merging two equal files results in matching source and destination result sets
    """
    test_file = "alpha.txt"
    start_time = time.time()
    destination = countWords(f"{FILE_PATH}/{test_file}")
    source = countWords(f"{FILE_PATH}/{test_file}")
    mergeResults(destination, source)
    assert len(destination) == len(source)
    elapsed_time = time.time() - start_time
    logger.log(f"Completed merge same results test in {elapsed_time:.5f} seconds")

def test_merge_different_results():
    """
    Test that merging results with no shared words results in a destination set that is longer than
    it was originally & its length is equal to the combined lengths of the source and destination
    """
    test_file_1 = "alpha.txt"
    test_file_2 = "beta.txt"
    start_time = time.time()
    destination = countWords(f"{FILE_PATH}/{test_file_1}")
    destination_copy = destination.copy()
    source = countWords(f"{FILE_PATH}/{test_file_2}")
    mergeResults(destination, source)
    assert len(destination) > len(destination_copy)
    assert len(destination) == len(source) + len(destination_copy)
    elapsed_time = time.time() - start_time
    logger.log(f"Completed merge different results test in {elapsed_time:.5f} seconds")
    
def test_merge_mixed_results():
    """
    Test that merging results with some shared words results in a result set that is bigger 
    than it was originally, but smaller than the combined lengths of each input
    """
    test_file_1 = "mixed_1.txt"
    test_file_2 = "mixed_2.txt"
    start_time = time.time()
    destination = countWords(f"{FILE_PATH}/{test_file_1}")
    destination_length_before_merge = len(destination)
    source = countWords(f"{FILE_PATH}/{test_file_2}")
    mergeResults(destination, source)
    assert len(destination) > destination_length_before_merge
    assert len(destination) < len(source) + destination_length_before_merge
    elapsed_time = time.time() - start_time
    logger.log(f"Completed merge different results test in {elapsed_time:.5f} seconds")

def test_merge_known_inputs():
    """
    Test that merging two input files with a known frequencies of the same word returns a result set
    that has the same word with the word frequency = frequency(dest) + frequency(source)
    """
    test_file_1 = "merge_known_output_1.txt"
    test_file_2 = "merge_known_output_2.txt"
    start_time = time.time()
    
    destination = countWords(f"{FILE_PATH}/{test_file_1}")
    assert destination['WORD'] == 1
    
    source = countWords(f"{FILE_PATH}/{test_file_2}")
    assert source['WORD'] == 2
    
    mergeResults(destination, source)
    assert destination['WORD'] == 3
    
    elapsed_time = time.time() - start_time
    logger.log(f"Completed merge known outputs test in {elapsed_time:.5f} seconds")

def test_deep_merge_comparison():
    """
    Test that each word in a result set is composed the correct amount of occurrances in the
    destination file and the source file
    """
    test_file_1 = "mixed_1.txt"
    test_file_2 = "mixed_2.txt"
    start_time = time.time()
    destination = countWords(f"{FILE_PATH}/{test_file_1}")
    destination_copy = destination.copy()
    source = countWords(f"{FILE_PATH}/{test_file_2}")
    mergeResults(destination, source)

    assert len(destination) < len(source) + len(destination_copy)
    for word in destination:
        if word in destination_copy.keys() and word not in source.keys():
            # if word is in destination keys make sure the amount in the 
            # result matches the amount in the destination_copy
            assert destination[word] == destination_copy[word]
            
        if word in source.keys() and word not in destination_copy.keys():
            # if word is in destination keys make sure the amount in the 
            # result matches the amount in the destination_copy
            assert destination[word] == source[word]
        
        if word in destination_copy.keys() and word in source.keys():
            # if word is shared by the source and destination make sure the
            # amount in the result is equal to the number of occurances in each
            assert destination[word] == source[word] + destination_copy[word]

    elapsed_time = time.time() - start_time
    logger.log(f"Completed deep equality merge comparison test in {elapsed_time:.5f} seconds")

def test_merge_large_files_results():
    """
    Test that merging large files doesn't cause any issues
    """
    test_file_1 = "500_words.txt"
    test_file_2 = "large_list.txt"
    start_time = time.time()
    destination = countWords(f"{FILE_PATH}/{test_file_1}")
    destination_length_before_merge = len(destination)
    source = countWords(f"{FILE_PATH}/{test_file_2}")
    mergeResults(destination, source)
    assert len(destination) < len(source) + destination_length_before_merge
    elapsed_time = time.time() - start_time
    logger.log(f"Completed merge different results test in {elapsed_time:.5f} seconds")