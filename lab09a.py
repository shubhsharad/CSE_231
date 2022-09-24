from operator import itemgetter

def build_map( in_file1, in_file2 ):
    data_map = {}
    in_file1.readline()
    in_file2.readline()

    #READ EACH LINE FROM FILE 1
    for line in in_file1.readlines():
       
        
        # Split the line into two words
        continent_list = line.strip().split()
        
        # Convert to Title case, discard whitespace
        continent = continent_list[0].strip().title()
        country = continent_list[1].strip().title()
        # Ignore empty strings
        if continent != "":
            # If current continent not in map, insert it 
            # YOUR CODE
            if continent not in data_map:
                data_map[continent] = {}
            # If country is not empty insert (continent is guaranteed to be in map)
            #YOUR CODE
            if country:
            
                 # If current country not in map, insert it 
                 if country not in data_map[continent]:
                     data_map[continent][country]=[]
                     

    #READ EACH LINE FROM FILE 2   
    for line in in_file2.readlines():
        

        # Split the line into two words
        countries_list = line.strip().split()
        
        # Convert to Title case, discard whitespace
        country = countries_list[0].strip().title()
        city = countries_list[1].strip().title()
        
        # Ignore empty strings
        if country != "":
            
            # insert city (country is guaranteed to be in map)
            for continent in data_map:
                if country in data_map[continent]:
                    if city not in data_map[continent][country]:
                        data_map[continent][country].append(city)
            
    return data_map

def display_map( data_map ):
    for cont in sorted(data_map.keys()):
        print("{}:".format(cont))
        for country in sorted(data_map[cont]):
            print("{:>10s} --> ".format(country),end = '')
            city_lst=sorted(data_map[cont][country])
            for city in city_lst:
                if city !=city_lst[-1]:
                    print('{}, '.format(city),end = '')
                else:
                    print('{}'.format(city),end='\n')

def open_file():

    try:
        filename = input("Enter file name: ")
        in_file = open( filename, "r" )
        
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file

def main():

    # YOUR CODE
    data_map = {}
    in_file1 = open_file() #Continents with countries file: continents.txt
    in_file2 = open_file() #Countries with cities file: cities.txt

    if in_file1 != None and in_file2 != None:
        
        data_map = build_map( in_file1, in_file2 ) # data_map is a dictionary
        display_map( data_map )
        
        in_file1.close()
        in_file2.close()

if __name__ == "__main__":
    main()