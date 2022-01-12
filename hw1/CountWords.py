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
    start_time = time.time()
    
    words = file.read()
    if words == '':
        """ If words is empty, return an empty directory """
        return {}
    
    #   Convert words to uppercase and split the string into a list of Strings,
    #   delimited by the " " space character
    words = words.upper().replace("\n", " ").split(" ")
    word_list = {}
    for word in words:
        if word not in word_list.keys():
            word_list[word] = 1
        else:
            word_list[word] = word_list[word] + 1

    #   Kill timing and close file
    elapsed_time = time.time() - start_time
    file.close()
    
    logger.log(f"\n\tWordlist: {word_list}\n\tElapsed Time: {elapsed_time:.5f}")
    return word_list
    
def main(*args, **kwargs):
    """ 
    Main method to get files from import or command line args. Iterates through 
    all files, counts the words, the combines the results from each
    """
    
    total_words = {}
    if len(args) > 0:
        #   Get filenames from command line arguments and count the words in them
        for filename in args:
            total_words.update(countWords(filename))
            
        print(total_words)
            
            
    else: 
        #   Get filenames of mock wordlists and count the words in them
        directory_files = os.listdir(os.getcwd()+"\\mock_lists")
        for filename in directory_files:
            total_words.update(countWords(os.getcwd()+"\\mock_lists\\"+filename))
            
        print(total_words)
    
if __name__ == '__main__':
    main()