"""
Program takes a list of files as input and counts all the words in the list of files,
printing out the list of words with their corresponding counts
"""

__version__ = '0.1'
__author__ = 'Zac Foteff'

import io
import time
from Loggers import MapReduceLogger

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'be', 'by', 
    'for', 'if', 'in', 'is', 'it',  'of', 'or', 
    'py', 'rst', 'that', 'the', 'to', 'with'
]

def count_words(file_name):
    """ 
    Take a file and output the word list with the counts for that file 
    as a list [['foo', 22], ...]

    Args:
        file_name (String): Name of file to iterate over to count words
    """
    
    startTime = time.clock()
    
    #   Logic
    
    deltaTime = time.clock() - startTime
    
def main():
    """ 
    Main method to get files from import or command line args. Iterates through 
    all files, counts the words, the combines the results from each
    """
    
if __name__ == '__main__':
    main()