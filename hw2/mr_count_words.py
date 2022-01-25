import os
import sys
import time
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
        words = current_file.read()
        
        if words == '':
            return []
        
        words = words.rstrip().replace("\n", " ").split(" ")
        word_list = []
        [(word_list.append([word, 1]) if word not in STOP_WORDS else '') for word in words]
        elapsed_time = time.perf_counter() - start_time
        logger.log(f"Find words method\n\tFile: {filename}\n\tElapsed Time: {elapsed_time:.5f}\n\tNumber of words found: {len(word_list)}")
        return word_list
            
def countWords(item:list):
    start_time = time.perf_counter()
    word_list = {}
    for word, amount in item:
        if word in word_list:
            word_list[word] += amount
        else:
            word_list[word] = amount
    word_count = sum(word_list.values())
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Count words method\n\tElapsed Time: {elapsed_time:.5f}\n\tNumber of words found: {word_count}")
    return word_count

def main(*args):
    """
    Main function for countwords program
    """
    file_count = 0
    total_wordcount = 0
    start_time = time.perf_counter()
    if args:
        #   get filenames from command line args
        inputted_files = sys.argv[1:]
        for filepath in inputted_files:
            countWords(findWords(filepath))
            file_count += 1
            
    else:
        word_list_directory = os.listdir(os.getcwd()+WORDLIST_FILEPATH)
        for file in word_list_directory:
            total_wordcount += countWords(findWords(word_list_directory+file))
            #map_reduce = SimpleMapReduce(countWords, findWords, 4)
            file_count += 1
    
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed word count of {file_count} files in {elapsed_time:.5f} | Result: {total_wordcount}")

if __name__ == "__main__":
    main()
