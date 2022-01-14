"""
Program takes a list of files as input and counts all the words in the list of files,
printing out the list of words with their corresponding counts
"""

__version__ = '1.1'
__author__ = 'Zac Foteff'

import os
import time
from Logger import Logger

logger = Logger("main", "hw1")

FILEPATH = "mock_lists/"

STOP_WORDS = [
    'A', 'AN', 'AND', 'ARE', 'AS', 'BE', 'BY', 
    'FOR', 'IF', 'IN', 'IS', 'IT',  'OF', 'OR', 
    'PY', 'RST', 'THAT', 'THE', 'TO', 'WITH'
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
    
    words = file.read()
    if words == '':
        """ If words is empty, return an empty directory """
        return {}
    
    #   Convert words to uppercase and split the string into a list of Strings,
    #   delimited by the " " space character
    words = words.upper().replace("\n", " ").split(" ")
    word_list = {}
    
    #   Start timing and count the words in the file
    start_time = time.time()
    for word in words:
        if word not in STOP_WORDS:
            if word not in word_list.keys(): 
                word_list[word] = 1
            else:
                word_list[word] = word_list[word] + 1

    #   Kill timing and close file
    elapsed_time = time.time() - start_time
    file.close()
    
    logger.log(f"\n\tFile: {file_name}\n\tElapsed Time: {elapsed_time:.5f}\n\tUnique words: {len(word_list.keys())}\n\tTotal words: {sum(word_list.values())}")
    return word_list
    
def main(*args, **kwargs):
    """ 
    Main method to get files from import or command line args. Iterates through 
    all files, counts the words, the combines the results from each
    """
    
    total_words = {}
    start_time = time.time()
    if len(args) > 0:
        #   Get filenames from command line arguments and count the words in them
        for filename in args:
            total_words.update(countWords(filename))
            
    else: 
        #   Get filenames of mock wordlists and count the words in them
        directory_files = os.listdir(os.getcwd()+"\\mock_lists")
        for filename in directory_files:
            #   Merge resuling dict with existing
            total_words.update(countWords(os.getcwd()+"\\mock_lists\\"+filename))
            
    #   Report final timing and results
    elapsed_time = time.time() - start_time;
    logger.log(f"\n\tFile iteration complete:\n\t____________________________\n\tTotal elapsed time: {elapsed_time:.5f}\n\t Total Unique words: {len(total_words.keys())}\n\t Total words: {sum(total_words.values())}")
    
if __name__ == '__main__':
    main()