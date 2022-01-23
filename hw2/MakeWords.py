"""
Module for creating a user defined number of words that is generated from a seed string
"""

from random import randint
import sys

def createFile(seed: str, writefile="out.txt", size=50, mode=0) -> None:
    """
    Creates random strings from inputted seed string

    Args:
        seed (str): Seed string for generating new random strings
        writefile (str, optional): File to write results to. Defaults to "out.txt".
        size (int, optional): Amount of strings, or bytes, to write to output file. Defaults to 50.
        mode (int): Mode the generator should use. Mode 0: Write specified number of words. Mode 1: Write specified number of bytes
    """
    
    if mode == 0:
        #   Write number of words
        with open(writefile, 'w') as curr_file:
            """
            Select a random string from the 
            [ start of seed string: first half of seed string] : [second half of seed string: end of seed string]
            """
            [curr_file.write(seed[randint(0, (len(seed)/2)-1): randint(len(seed)/2, len(seed))] + " ") for x in range(0, size)]
            
    elif mode == 1:
        #   Write number of bytes
        with open(writefile, 'w') as curr_file:
            bytes_sent = 0
            while bytes_sent < size:
                writeString = seed[randint(0, (len(seed)//2)-1): randint((len(seed)//2), len(seed))] + " "
                
                #   Check that the new string doesnt exceed the 
                while (bytes_sent + len(writeString.encode('utf-8')) > size):
                    #   Reduce generated string  character by character until it matches the correct size
                    writeString = writeString[:-1]
                
                curr_file.write(writeString)
                bytes_sent += len(writeString.encode('utf-8'))
          
            
def main(**args):
    if args:
        createFile(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        
    else:
        seedCorpus = input("Enter a seed string: ")
        inputtedMode = int(input("Enter mode to run\n\t[0]: Generate number of strings\n\t[1]: Generate number of bytes\n: "))
        inputtedSize = int(input("Enter size of file: "))
        createFile(seedCorpus, 'out.txt', inputtedSize, inputtedMode)
        print("Completes. Results available in ./out.txt")

if __name__ == '__main__':
    main()