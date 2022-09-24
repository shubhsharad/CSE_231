###########################################################
    #  Project 7
    #
    #   open_file() function
    #   read_file(fp) function   
    #   history_of_country(country,country_names,list_of_regime_lists) function
    #   historical_allies(regime,country_names,list_of_regime_lists) function
    #   top_coup_detat_count(top, country_names,list_of_regime_lists) function
    #   main() function
    #       display MENU
    #       prompt for input
    #       if input == 1
    #           prompt for country 
    #           show type of Regime in country
    #       if input == 2
    #           prompt for regime
    #           show list of allies
    #       if input == 3
    #           prompt user for input for top variable
    #           display top number of countries with most coup detats
    #       if input == q
    #           break
    #       display end message.
    #   end of program
###########################################################



import csv
from operator import itemgetter

REGIME=["Closed autocracy","Electoral autocracy","Electoral democracy","Liberal democracy"]
MENU='''\nRegime Options:
            (1) Display regime history
            (2) Display allies
            (3) Display chaotic regimes        
    '''

def open_file():
    '''
    This function prompts the user for the name of the input file 
    and after opening it, return its pointer.
    Parameters: none
    Returns: file pointer
    Displays: prompt and error message
    '''
    while True:
        file_name = input("Enter a file: ")
        try:
            fp = open(file_name,"r")
            break
        except:
            print("File not found. Please try again.")
            continue
    return fp
    
def read_file(fp):
    ''' 
    This function reads a file in the csv format, checks for country
    appends it to a country_names list. Makes a list_of_regime_lists for 
    each country. Uses loops to go through the csv file.
    Parameters: file pointer
    Returns: country_names, list_of_regime_lists
    Displays: nothing
    '''
    country_names = []
    list_of_regime_lists = []
    temp = []
    csvreader = csv.reader(fp)
    next(csvreader,None)
    
    for line in csvreader:
        country_name = line[1]
        political_regime = int(line[-1])
        
        if not country_name:
            country_names.append(country_name)
            temp.append(political_regime)
        
        elif country_name not in country_names:
            country_names.append(country_name)
            list_of_regime_lists.append(temp)
            temp = []
            temp.append(political_regime)
            
        elif country_name in country_names:
            temp.append(political_regime)
            
    
    list_of_regime_lists.append(temp)
    list_of_regime_lists.pop(0)
            
    return country_names, list_of_regime_lists

def history_of_country(country,country_names,list_of_regime_lists):
    ''' 
    This function wants to figure out the dominant regime in 
    a country by using the lists that we created earlier.
    uses max and index functions to help dominant regime of the country.
    Parameters: str, list of str, list of list of ints
    Returns: type of regime from REGIME list
    Displays: nothing
    '''
    regime_temp_list = [0,0,0,0]
    i = country_names.index(country)
    for count in list_of_regime_lists[i]:
        regime_temp_list[count] += 1
    maximum_occurence = max(regime_temp_list)
    fin = regime_temp_list.index(maximum_occurence)
    return (REGIME[fin])


def historical_allies(regime,country_names,list_of_regime_lists):
    ''' 
    Using the help of the previous function, history_of_country, we want 
    to figure out which countries are historical allies in that they have the 
    same political ideology that is the most dominant in their history
    Parameters: str, list of str, list of lists of ints
    Returns: allies_list
    Displays: nothing
    '''
    allies_list = []
    for country in country_names:
        regime_of_country = history_of_country(country, country_names, list_of_regime_lists)
        if regime == regime_of_country:
            allies_list.append(country)
        else:
            continue
    return allies_list
            
            


def top_coup_detat_count(top, country_names,list_of_regime_lists):          
    '''
    In this function, we want to figure out which countries 
    had the most coups in their history. In other words, how many times their
    regime changed for example in this list. We want to calculate how many times 
    each country had a coup and return the top number of countries 
    with the most coups sorted from most to least.
    Parameters: int, list of str, list of lists of ints
    Returns: coup_list2
    Displays: nothing
    '''
    coup_list = []
    coup_list2 = []
    for i in range(0,len(list_of_regime_lists)):
        
        count = 0
        for j in range(1,len(list_of_regime_lists[i])):
            if list_of_regime_lists[i][j] != list_of_regime_lists[i][j-1]:
                count = count + 1
        coup_list.append((country_names[i],count))
    coup_list.sort(key= itemgetter(1),reverse = True)
        
    for i in range(0,int(top)):
        try:
            coup_list2.append(coup_list[i])
        except:
            break
    
    return coup_list2
                
def main():
    # by convention "main" doesn't need a docstring
    fp = open_file()
    country_names, list_of_regime_lists = read_file(fp)
    
    while True:
        print(MENU)
        while True:
            user_input = input("Input an option (Q to quit): ")
            
            if user_input not in ["q","Q","1","2","3"]:
                print("Invalid choice. Please try again.")
            else:
                break
            
        if user_input == "q" or user_input == "Q":
            break
        
        elif user_input == "1":
            while True:
                country = input("Enter a country: ")
                if country not in country_names:
                    print("Invalid country. Please try again.")
                else:
                    break
            
            regime = history_of_country(country, country_names, list_of_regime_lists)
            
            if regime == REGIME[1] or regime == REGIME[2]:
                print("\nHistorically {} has mostly been an {}".format(country,regime))
            else:
                print("\nHistorically {} has mostly been a {}".format(country, regime))
                
        
        elif user_input == "2":
            while True:
                regime = input("Enter a regime: ")
                
                if regime not in REGIME:
                    print("Invalid regime. Please try again.")
                else:
                    break
            regime_string = ""
            allies_list = historical_allies(regime, country_names, list_of_regime_lists)
            
            for cont in allies_list:
                regime_string = regime_string+ cont + ", "
                
            print("\nHistorically these countries are allies of type:",regime)
            print(regime_string[:-2])
        
        elif user_input == '3':
            while True:
                top_count = input("Enter how many to display: ")
                
                if top_count.isdigit() and int(top_count)>0:
                    break
                else:
                    print("Invalid number. Please try again.")
                    continue
            
            top_count = int(top_count)
                  
            top_list = top_coup_detat_count(top_count, country_names,\
                                            list_of_regime_lists)
            
            print("\n{: >25} {: >8}".format("Country", "Changes"))
            print()
            
            for i in top_list:
                country_n = i[0]
                num = str(i[1])
                print("{: >25} {: >8}".format(country_n, num))
            
    print("The end.")
            
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main() 