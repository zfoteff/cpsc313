"""
Program takes a list of files as input and counts all the words in the list of files,
printing out the list of words with their corresponding counts
"""

__version__ = '1.3'
__author__ = 'Zac Foteff'

import os
import sys
import time
from Logger import Logger

logger = Logger("main", "hw1")

FILE_PATH = "\\word_lists\\"

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
        # If words is empty, return an empty directory
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
                #   Create new dictionary entry for unencountered word
                word_list[word] = 1
            else:
                #   Incriment dictionary entry by one for encountered word
                word_list[word] = word_list[word] + 1

    #   Kill timing and close file
    elapsed_time = time.time() - start_time
    file.close()
    
    logger.log(f"\n\tFile: {file_name}\n\tElapsed Time: {elapsed_time:.5f}\n\tUnique words: {len(word_list.keys())}\n\tTotal words: {sum(word_list.values())}")
    return word_list

def mergeResults(wordlist_1={}, wordlist_2={}):
    """
    Merge the results of counting words into one dictionary for compiling final results

    Args:
        wordlist_1 (dict): Destination dictionary for source dictionary to merge its results into
        wordlist_2 (dict): Source dictionary to be merged into destination dictionary
    """
    
    for word in wordlist_2:
        if word in wordlist_1.keys():
            wordlist_1[word] = wordlist_1[word] + wordlist_2[word]
        else:
            wordlist_1[word] = wordlist_2[word]
            
def countWordsForFile(filename:str) -> int:
    total_words = {}
    mergeResults(total_words, countWords(filename))
    return sum(total_words.values())
    

def main(*args, **kwargs):
    """ 
    Main method to get files from import or command line args. Iterates through 
    all files, counts the words, the combines the results from each
    """
    total_words = {}
    
    #   Start timer
    start_time = time.time()
    if args:
        #   Get filenames from command line arguments and count the words in them
        inputtedFiles = sys.argv[1:]
        for filepath in inputtedFiles:
            total_words.update(countWords(f"{filepath}"))
            
    else: 
        #   Get files from wordlist directory and count the words in them
        directory_files = os.listdir(os.getcwd()+FILE_PATH)
        for filename in directory_files:
            #   Merge resuling dict with existing
            mergeResults(total_words, countWords(os.getcwd()+FILE_PATH+filename))
            
    #   Report final timing and results
    elapsed_time = time.time() - start_time;
    logger.log(f"\n\tFile iteration complete:\n\t____________________________\n\tTotal elapsed time: {elapsed_time:.5f}\n\t Total Unique words: {len(total_words.keys())}\n\t Total words: {sum(total_words.values())}")
    
if __name__ == '__main__':
    main()