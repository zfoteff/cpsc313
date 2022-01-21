from random import randint
import sys

def createFile(corpus: str, writefile: str, size: int) -> None:
    with open(writefile, 'w') as curr_file:
        randIdx1 = randint(0, len(corpus)-1)
        randIdx2 = randint(randIdx1, len(corpus))
        [curr_file.write(corpus[randIdx1:randIdx2] + " ") for x in range(0, size)]
        
def main():
    createFile("Teststringalskjdhfalskdjfhasd;kifihasd;kfjhasdkjfhasdkljfhas", 'out.txt', 50)

if __name__ == '__main__':
    main()