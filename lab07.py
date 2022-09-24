import csv
from operator import itemgetter

INDUSTRIES = ['Agriculture', 'Business services', 'Construction', 'Leisure/hospitality', 'Manufacturing']

def read_file(fp):
    '''Docstring'''
    csv_reader = csv.reader(fp)
    count = 0
    while count < 4:
        next(csv_reader)
        count = count+1
    ilist = []
    for row in csv_reader:
        data_list = []
        if row[0] != "":
            for column in row:
                data_list.append(column)
            ilist.append(data_list)
    return ilist

def get_totals(L):
    '''Docstring'''
    sum_US = 0
    sum_states = 0
    return None,None  # temoprary return value so main runs

def get_industry_counts(L):
    '''Docstring'''
    largestNumberOfIndustries = []
    for indust in INDUSTRIES:
        count = 0
        for row in L[1:]:
                if row[9] == indust:
                    count = count + 1
        largestNumberOfIndustries.append([indust, count])  
    largestNumberOfIndustries = sorted(largestNumberOfIndustries, \
                                       key=itemgetter(1), reverse = True)
    return largestNumberOfIndustries
    # temoprary return value so main runs

def get_largest_states(L):
    '''Docstring'''
    return None  # temoprary return value so main runs

def main():    
    fp = open("immigration.csv")
    L = read_file(fp)
    
    us_pop,total_pop = get_totals(L)
    if us_pop and total_pop:  # if their values are not None
        print("\nData on Illegal Immigration\n")
        print("Summative:", us_pop)
        print("Total    :", total_pop)
    
    states = get_largest_states(L)
    if states:  # if their value is not None
        print("\nStates with large immigrant populations")
        for state in states:
            state = state.replace('\n',' ')
            print(state)        
    
    counters = get_industry_counts(L)
    if counters:  # if their value is not None
        print("\nIndustries with largest immigrant populations by state")
        print("{:24s} {:10s}".format("industry","count"))
        for tup in counters:
            print("{:24s} {:2d}".format(tup[0],tup[1]))
        
if __name__ == "__main__":
    main()