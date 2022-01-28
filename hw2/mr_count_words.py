import os
import sys
import time
import string
from basicMR import SimpleMapReduce
from Logger import Logger

WORDLIST_FILEPATH = "\\word_lists\\prod\\"
RAND_WORDS_API_URL = "https://random-word-api.herokuapp.com/"
STOP_WORDS = [
    'A', 'AN', 'AND', 'ARE', 'AS', 'BE', 'BY', 
    'FOR', 'IF', 'IN', 'IS', 'IT',  'OF', 'OR', 
    'PY', 'RST', 'THAT', 'THE', 'TO', 'WITH'
]

logger = Logger('Main', 'hw2')

def sumResultWordcount(result_list):
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

def findWords(filename:str):
    """
    Find return a list of iterables with all the words in a given file. Should read all words
    into a string. Then the string should convert all words to uppercase, remove all punctuation,
    and strip any trailing spaces that may exist

    Args:
        filename (str): File to iterate over

    Returns:
        list: iterable list of words for reduce function
    """
    with open(f"{filename}", "r") as current_file:
        words = current_file.read()
        if words == '':
            return []
        
        words = words.rstrip().upper().replace("\n", " ").translate(str.maketrans('', '', string.punctuation)).split(" ")
        word_list = [(word, 1) for word in words if word not in STOP_WORDS]
        return word_list
            
def countWords(item):
    """
    Iterate through the list of words in a file, sum the words, and return the count

    Args:
        item (tuple): Array of tuples with word and an iterable of their counts in the files

    Returns:
        tuple: All counted words and their corresponding sums
    """
    if item == []:
        return ()
    result_word = (item[0], sum(item[1]))
    return result_word

def main(*args):
    total_wordcount = 0
    start_time = time.perf_counter()
    
    if args:
        inputted_files = sys.argv[1:]
        for filepath in inputted_files:
            total_wordcount += countWords(findWords(filepath))
    else:
        word_list_directory = os.listdir(os.getcwd()+"\\word_lists\\prod\\")
        files = [os.getcwd()+WORDLIST_FILEPATH+file for file in word_list_directory]
        reduce = SimpleMapReduce(findWords, countWords)
        total_wordcount += sumResultWordcount(reduce(files))
    
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed word count in {elapsed_time:.5f} seconds | Result: {total_wordcount}")

if __name__ == "__main__":
    main()
