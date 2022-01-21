import os
import sys
import time
import requests
import basicMR
from Logger import Logger

RAND_WORDS_API_URL = "https://random-word-api.herokuapp.com/"
STOP_WORDS = [
    'A', 'AN', 'AND', 'ARE', 'AS', 'BE', 'BY', 
    'FOR', 'IF', 'IN', 'IS', 'IT',  'OF', 'OR', 
    'PY', 'RST', 'THAT', 'THE', 'TO', 'WITH'
]

logger = Logger('hw2Main', 'hw2')

def create_file(corpus:str, filename:str, size:int):
    with open(filename, "w") as current_file:
        for line in current_file:
            line = line
            
def countWords(item:dict):
    return sum(item.values())

def findWords(item):
    pass

def main():
    start_time = time.perf_counter()
    
    map_reduce = basicMR(countWords, findWords, 4)
    
    elapsed_time = time.perf_counter() - start_time
    logger.log(f"Completed file iteration in {elapsed_time}")

if __name__ == "__main__":
    main()