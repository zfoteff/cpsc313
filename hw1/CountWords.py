"""
Program takes a list of files as input and counts all the words in the list of files,
printing out the list of words with their corresponding counts
"""

__version__ = '0.1'
__author__ = 'Zac Foteff'

import io
import time
from Loggers import MapReduceLogger

logger = MapReduceLogger()

FILEPATH = "word_lists/"

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'be', 'by', 
    'for', 'if', 'in', 'is', 'it',  'of', 'or', 
    'py', 'rst', 'that', 'the', 'to', 'with'
]

def countWords(file_name):
    """ 
    Take a file and output the word list with the counts for that file 
    as a list [['foo', 22], ...]

    Args:
        file_name (String): Name of file to iterate over to count words
    """
    
    #   Load file and start timer
    file = open(f"{file_name}", "r")
    start_time = time.process_time()
    
    words = file.read()
    if words == '':
        """ If words is empty, return an empty directory """
        return {}
    
    #   Convert words to uppercase and split the string into a list of Strings,
    #   delimited by the " " space character
    words = words.upper().replace("\n", " ").split(" ")
    word_list = {}
    for word in words:
        if word not in word_list or len(word_list) == 0:
            word_list[word] = 1
        else:
            word_list[word] = word_list[word] + 1

    #   Kill timing and close file
    elapsed_time = time.process_time() - start_time
    file.close()
    
    logger.log(f"\n\tWordlist: {word_list}\n\tElapsed Time: {elapsed_time}")
    return word_list
    
def main():
    """ 
    Main method to get files from import or command line args. Iterates through 
    all files, counts the words, the combines the results from each
    """
    countWords(FILEPATH+"alpha.txt")
    
if __name__ == '__main__':
    main()