import string
from operator import itemgetter


def add_word( word_map, word ):
    ''' Function to add a word to the dictionary and check for repetition
        Parameter(Dictionary,word)'''

    # If word is not in the dictionary, add it to the dictionary 
    
    if word not in word_map:
        word_map[ word ] = 0

    # increment count of words
    word_map[ word ] += 1


def build_map( in_file, word_map ):
    ''' Function used to create a dictionary and remove spaces and punctuation
        Parameter(File pointer,dictionary)'''

    for line in in_file:

        # Splitting every line into a list of words
        word_list = line.split()

        for word in word_list:

            # Stripping words of spaces and punctuation and making them 
            # lowercase
            word = word.strip().strip(string.punctuation).lower()
            if word:        
                add_word(word_map, word)
        

def display_map( word_map ):
    '''Function used to print Sorted List to the user
        Parameter(dictionary)'''
    word_list = list()

    # appends the items in the dictionary to a list with the key 
    # and value pairs seperated as tuples
    for word, count in word_map.items():
        word_list.append( (word, count) )

    # sorts the list by frequency of each word
    freq_list = sorted( word_list)
    freq_list = sorted( freq_list, key=itemgetter(1),reverse=True )

    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format( item[0], item[1] ) )


def open_file():
    ''' Function to open the file for reading'''
    
    try:
        in_file = open(input(" Enter File Name:"))
        
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file


word_map = dict()
in_file = open_file()

if in_file != None:

    build_map( in_file, word_map )
    display_map( word_map )
    in_file.close()

