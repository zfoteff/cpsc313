import os
import sys
import time
import requests
from Logger import Logger

RAND_WORDS_API_URL = "https://random-word-api.herokuapp.com/"
STOP_WORDS = [
    'A', 'AN', 'AND', 'ARE', 'AS', 'BE', 'BY', 
    'FOR', 'IF', 'IN', 'IS', 'IT',  'OF', 'OR', 
    'PY', 'RST', 'THAT', 'THE', 'TO', 'WITH'
]

def create_file(corpus:str, filename:str, size:int):
    with open(filename, "w") as current_file:
        for line in current_file:
            line = line
            
def countWords(item):
    pass

def findWords(item):
    pass

def main():
    start_time = time.perf_counter()
    
    elapsed_time = time.perf_counter() - start_time

if __name__ == "__main__":
    main()