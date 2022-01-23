import os
import sys
import time
import requests
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

def findWords(filename:str) -> list:
    """
    Find return a list of iterables with all the words in a given file

    Args:
        filename (str): File to iterate over

    Returns:
        list: iterable list of words for reduce function
    """
    with open(f"{filename}", "r") as current_file:
        start_time = time.perf_counter()
        words = current_file.read().upper().rstrip().replace("\n", " ").split(" ")
        word_list = []
        
        # Append each word to the list with the letter one, assuming that it is not in STOP_WORDS
        [(word_list.append([word, 1]) if word not in STOP_WORDS else '') for word in words]
        elapsed_time = time.perf_counter() - start_time
        logger.log(f"\n\tFile: {filename}\n\tElapsed Time: {elapsed_time:.5f}\n\tNumber of words found: {len(word_list)}")
        return word_list
            
def countWords(item:list):
    return sum(item.values())

def main(*args):
    """
    Main function for countwords program
    """
    start_time = time.perf_counter()
    if args:
        #   get filenames from command line args
        inputted_files = sys.argv[1:]
        for filepath in inputted_files:
            findWords(filepath)
            
    else:
        word_list_directory = os.listdir(os.getcwd()+WORDLIST_FILEPATH)
        for file in word_list_directory:
            findWords(os.getcwd()+WORDLIST_FILEPATH+file)
    
    #map_reduce = SimpleMapReduce(countWords, findWords, 4)
    
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed file iteration in {elapsed_time:.5f}")

if __name__ == "__main__":
    main()