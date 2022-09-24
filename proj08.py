###########################################################
    #  Project 8
    #
    #   open_file() function
    #   max_in_region() function
    #   min_in_region() function
    #   
    #   read_file(fp) function   
    #   add_per_capita() function
    #   dispay_region() function
    #   main() function
    #       fp = open_file()
    #       master_dict = read_file(fp)
    #       add_per_capita(master_dict)
    #       iterate through dictionary
    #           display region function
    #       display end message
    #   end of program
###########################################################

import csv
from operator import itemgetter

def open_file():
    '''
    This function prompts the user for the name of the input file 
    and after opening it, return its pointer.
    Parameters: none
    Returns: file pointer
    Displays: prompt and error message
    '''
    # loop to input check
    while True:
        # variable that stores file name
        file_name = input("Input a file: ")
        try:
            # opening file for reading with encoding
            fp = open(file_name,encoding='utf-8')
            break
        except:
            # error message
            print("Error: file does not exist. Please try again.")
            continue
    # returns file pointer
    return fp

def max_in_region(D,region):
    '''
    Find the maximum per-capita diabetes in the region.
    Return the country name and percapita diabetes value in a tuple. 
    Parameters: dictionary of lists
    Returns: tuple (string, float)
    Displays: nothing
    '''
    # empty list
    lst = []
    # iterates through every country
    for i in D[region]:
        # tuple of name and diabetes
        x = (i[0],i[-1])
        # appending it to empty list
        lst.append(x)
    # using max and itemgetter to return max value according to diabetes
    return max(lst,key = itemgetter(1))

             
def min_in_region(D,region):
    '''
    Find the minimum per-capita diabetes in the region. 
    The minimum should be higher than 0. 
    Return the country name and per-capita diabetes value in a tuple. 
    Parameters: dictionary of lists
    Returns: tuple (string, float)
    Displays: nothing
    '''
    # empty list
    lst = []
    # iterates through every country
    for i in D[region]:
        # tuple of name and diabetes
        if i[-1] != 0:
            # appending it to empty list
            x = (i[0],i[-1])
            lst.append(x)
    # using max and itemgetter to return max value according to diabetes
    return min(lst,key = itemgetter(1))


def read_file(fp):
    '''
    Read the file referenced by the parameter.
    and create a dictionary of lists of lists.
    Parameters: file pointer
    Returns: dictionary of sorted list of lists
    Displays: nothing
    '''
    # creates a list of all entries in the file
    csvreader = csv.reader(fp)
    #skips a line
    next(csvreader,None)
    # initialise an empty dictionary
    dictionary = {}
    for line in csvreader:
        #use try and except to check for entries in the file
        try: 
            region = line[1]
        except:
            continue
        try: 
            country = line[2]
        except:
            continue
        try: 
            # make population a float and replace commas with empty spaces
            # for easy reading
            population  = float(line[5].replace(",",""))
        except:
            continue
        try: 
            # make diabetes a float and replace commas with empty spaces
            # for easy reading
            diabetes = float(line[9].replace(",",""))
        except:
            continue
        # checks for the same entry in the dictionary
        if region not in dictionary:
            dictionary[region] = []
        # temporary list of country, diabetes and population
        temp_list = [country, diabetes, population]
        # append each entry into the dictionary
        dictionary[region].append(temp_list)
    # code to sort the dictionary     
    for i in dictionary:
        dictionary[i].sort()
    # function returns dictionary with all entries
    return dictionary
        

def add_per_capita(D):
    '''
    Calculate diabetes per capita for each country 
    and region by simply dividing the diabetes value by the population value.
    Parameters: dictionary of lists
    Returns: dictionary of lists
    Displays: formatted data
    '''
    # accesses each region in the dictionary
    for i_list in D:
        # access each country in one region
        for j_item in D[i_list]:
            try:
                # per_capita found after dividing popualtion by diabetes
                per_capita = j_item[1]/j_item[-1]
                # append each per_capita to the list
                j_item.append(per_capita)
            except:
                # append 0.0 if not valid 
                j_item.append("0.0")
    # returns dictionary
    return D
                
def display_region(D,region):
    '''
    Display the summary data for the region (string) followed
    by a table with the data for each country.
    Parameters: dictionary of lists, string
    Returns: nothing
    Displays: table of region data
    '''
    # temporary list
    temp_list = []
    
    # for each country in the region
    for lst in D[region]:
        # gets index
        idx = D[region].index(lst)
        #   checks if entry of country is equal to country
        if lst[0] == region:
            reg_sum = [lst[0], lst[1], lst[2], lst[-1]]
            D[region].pop(idx)
    
    # for each country in the region
    for lst in D[region]:
        temp = [lst[0], lst[1], lst[2], lst[-1]]
        # appending to temp_list for ease in printing
        temp_list.append(temp)
        
    
    print("Type1 Diabetes Data (in thousands)")   
    print("{:<37s} {:>9s} {:>12s} {:>11s}".format("Region","Cases",\
                                                  "Population","Per Capita"))
    print("{:<37s} {:>9.0f} {:>12,.0f} {:>11.5f}".format(*reg_sum))
    print("{:<37s} {:>9s} {:>12s} {:>11s}".format("Country","Cases",\
                                                  "Population","Per Capita"))
    # sorts according to per_capita and reverses the list
    temp_list.sort(key = itemgetter(3), reverse= True)
    for i in temp_list:
        print("{:<37s} {:>9.1f} {:>12,.0f} {:>11.5f}".format(*i))
    print("\nMaximum per-capita in the {} region".format(region))
    print("{:<37s} {:>11s}".format("Country","Per Capita"))
    print("{:<37s} {:>11.5f}".format(*max_in_region(D, region)))
    print("\nMinimum per-capita in the {} region".format(region))
    print("{:<37s} {:>11s}".format("Country","Per Capita"))
    print("{:<37s} {:>11.5f}".format(*min_in_region(D, region)))
    print("-"*72)
    
def main():
    #calling all functions
    fp = open_file()
    dct = read_file(fp)
    add_per_capita(dct)
    
    for i in dct:
        display_region(dct, i)
    
    
    print('\n Thanks for using this program!\nHave a good day!')
        

if __name__ == "__main__": 
    main()