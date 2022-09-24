###########################################################
    #   Project 6
    #   get_option() function
    #   open_file() function
    #   read_file() function
    #   print_data() funcion
    #   get_christmas_songs() function
    #   sort_by_peak() function
    #   sort_by_weeks_on_list() function
    #   song_score() function
    #   sort_by_score() function
    #   main() function
    #       print("\nBillboard Top 100\n")
    #       open_file() function is called
    #       read_file() function is called and a master_list is made
    #       while loop is started:
    #           get_option() function is called
    #           multiple if statements are used for different inputs from user
    #           if input == b
    #               sort_by_peak() function is called
    #           if input == c
    #               sort_by_weeks_on_list() function is called
    #           if input == d
    #               sort_by_score() function is called
    #           if input == a
    #               get_christmas_songs() function is called
    #           if input == q
    #               print("\nThanks for using this program!
    #                       \nHave a good day!\n")
    #   Program Ends
    ###########################################################

import csv
from operator import itemgetter

# Keywords used to find christmas songs in get_christmas_songs()
CHRISTMAS_WORDS = ['christmas', 'navidad', 'jingle', 'sleigh', 'snow',\
                   'wonderful time', 'santa', 'reindeer']

# Titles of the columns of the csv file. used in print_data()
TITLES = ['Song', 'Artist', 'Rank', 'Last Week', 'Peak Rank', 'Weeks On']

# ranking parameters -- listed here for easy manipulation
A,B,C,D = 1.5, -5, 5, 3

#The options that should be displayed
OPTIONS = "\nOptions:\n\t\
        a - display Christmas songs\n\t\
        b - display songs by peak rank\n\t\
        c - display songs by weeks on the charts\n\t\
        d - display scores by calculated rank\n\t\
        q - terminate the program \n"

#the prompt to ask the user for an option
PROMPT = "Enter one of the listed options: "

def get_option():
    '''
    Function to show options to the user and then check for proper input.
    Keep checking until user provides correct input.
    i_string: value input by user
    checks for correct input
    returns: i_string
    '''
    print(OPTIONS)
    l = ["a","b","c","d","q"]
    while True:
        i_string = input(PROMPT).lower()
        if i_string in l:
            break
        else:
            print('Invalid option!\nTry again')
            continue
    return i_string

def open_file():
    '''
    Function to open file to read
    also checks whether input file name is wrong or not.
    input: none
    returns: file pointer 
    '''
    while True:
        i_file = input('Enter a file name: ')
        try:
            f_inp = open(i_file,"r")
            break
        except:
            print('\nInvalid file name; please try again.\n')
            continue
    return f_inp

def read_file(fp):
    '''
    reads the file and creates a master list that contains a list 
    of songs from each file. Also checks for entries where entry is -1.
    Skips header line and reads every song entry and appends it to the master
    list.
    input = file pointer (fp)
    returns: master_list with all songs in it.
    '''
    master_list = []
    csvreader = csv.reader(fp)
    next(csvreader,None)
    for line in csvreader:
        song = line[0]
        artist = line[1]
        try:
            weeks = int(line[5])
        except:
            weeks = -1
        try:
            peek = int(line[4])
        except:
            peek = -1
        try:
            last_week = int(line[3])
        except:
            last_week = -1
        try:
            rank = int(line[2])
        except:
            rank = -1
        item = [song,artist,rank,last_week,peek,weeks]
        master_list.append(item)
    return master_list

def print_data(song_list):
    '''
    This function is provided to you. Do not change it
    It Prints a list of song lists.
    '''
    if not song_list:
        print("\nSong list is empty -- nothing to print.")
        return
    # String that the data will be formatted to. allocates space
    # and alignment of text
    format_string = "{:>3d}. "+"{:<45.40s} {:<20.18s} "+"{:>11d} "*4
    
    # Prints an empty line and the header formatted as the entries will be
    print()
    print(" "*5 + ("{:<45.40s} {:<20.18s} "+"{:>11.9s} "*4+'\n'+'-'*120)\
          .format(*TITLES))

    # Prints the formatted contents of every entry
    for i, sublist in enumerate(song_list, 1):
        #print(i,sublist)
        print(format_string.format(i, *sublist).replace('-1', '- '))

def get_christmas_songs(master_list):
    '''
    Function to check which songs in the master list are christmas songs. 
    goes through the song title in each song inside master list and checks
    for christmas words.If christmas words are found, then it is appended to
    another christmas list that contains only christmas songs. 
    input = master list
    returns = christmas_list which contains a list of christmas songs
    '''
    christmas_list = []
    for i in range(len(master_list)):
        for j in CHRISTMAS_WORDS:
            if j in master_list[i][0].lower():
                christmas_list.append(master_list[i])
    christmas_list.sort()
    return christmas_list
                
def sort_by_peak(master_list):
    '''
    Function to sort the songs by their peak. 
    if the peak is -1, then the song is removed from the list
    then sort() function is used with key and itemgetter to sort by peak. 
    '''
    sorted_by_peak = []
    sorted_by_peak = sorted\
        ((i for i in master_list if (i[4]!=-1)),key = itemgetter(4))
    return sorted_by_peak
    

def sort_by_weeks_on_list(master_list):
    '''
    Function to sort the songs by the number of weeks on list. 
    if the number of weeks on list is -1, then the song is removed from 
    the list,
    then sort() function is used with key and itemgetter to sort by weeks
    on list.
    '''
    for i in master_list:
        if i[5] == -1:
            master_list.remove(i)
    master_list.sort(key = itemgetter(5),reverse = True)
    return master_list
        
def song_score(song):
    '''
    Function to calculate the song score of the each song in the master list
    checks for -1 in entries and then makes new variables for easy calculation.
    score is then calculated with the variables and constants calculated 
    earlier.
    input: song (list)
    returns: score (float)
    '''
    rank_delta = song[2]-song[3]
    weeks_on_chart = song[5]
    if song[2]== -1:
        curr_rank = -100
    else:
        curr_rank = 100-song[2]
    if song[4] == -1:
        peak_rank = -100
    else:
        peak_rank = 100 - song[4]
    score = float((A*peak_rank)+(B*rank_delta)+(C*weeks_on_chart)+\
                  (D*curr_rank))
    return score

def sort_by_score(master_list):
    '''
    Function to sort the songs by their score calculated in the song_score()
    function. Once the list is sorted according to the scores, and if there 
    is a tie, then a second value is passed to the itemgetter function to
    sort according to name. The list is displayed in descending order.
    Input: Master_List
    returns: new_list that contains the list of sings sorted by score
    '''
    score_list=[]
    new_list = []
    for i in master_list:
        score = song_score(i)
        temp = [i,score]
        score_list.append(temp)
    score_list.sort(key = itemgetter(1,0),reverse = True)
    for j in score_list:
        j.pop()
        new_list.append(j[0])
    return new_list

def main():
    '''
    Function that calls other functions and is the main driver of the program.
    It opens the file and calls other functions in a loop.
    '''
    print("\nBillboard Top 100\n")
    fp = open_file()
    master_list = read_file(fp)
    print_data(master_list)
    while True:
        user_input = get_option()
        if user_input =="q":
            break
        elif user_input == "b":
            print_data(sort_by_peak(master_list))  
        elif user_input == "c":
            print_data(sort_by_weeks_on_list(master_list))
        elif user_input == "d":
            print_data(sort_by_score(master_list))
        elif user_input == "a":
            christmas_list = get_christmas_songs(master_list)
            print_data(christmas_list)
            if len(christmas_list) == 0:
                print('None of the top 100 songs are Christmas songs.')
            else:
                try:
                    per = int((len(christmas_list)/len(master_list))*100)
                    print('\n{:d}% of the top 100 songs are Christmas songs.'\
                          .format(per))
                except:
                    print('None of the top 100 songs are Christmas songs.')
    print("\nThanks for using this program!\nHave a good day!\n")
            

# Calls main() if this modules is called by name
if __name__ == "__main__":
    main()           
    
    
    
