import random


SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORD_LIST_FNAME = 'words.txt'

WORDS_INV_TOTAL = 7

def loadWords():
    '''
    Input: loads words from a file named in the constant 'WORD_LIST_FNAME'
    Returns: a list of all words within the file
    '''
    file = open(WORD_LIST_FNAME, 'r')
    text = file.readlines()
    return text

def dealHand():
    '''
    Returns: a random set of lower case characters 
    based on the 'WORDS_INV_TOTAL' as quantity of random characters
    '''
    return random.sample(SCRABBLE_LETTER_VALUES.keys(), WORDS_INV_TOTAL)
























