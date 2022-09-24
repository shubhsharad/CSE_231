###########################################################
    #  Project 9
    #
    #   get_option function
    #   open_file(s) function
    #   read_annot_file(fp1) function
    #   read_category_file(fp2) function
    #   collect_category_set() function
    #   collect_img_list_for_categories(D_annot,D_cat,cat_set):
    #    max_instances_for_item(D_image):
    #   main() function
#
    #       display end message
    #   end of program
###########################################################
import json,string
from operator import itemgetter

STOP_WORDS = ['a','an','the','in','on','of','is','was','am','I','me','you','and','or','not','this','that','to','with','his','hers','out','it','as','by','are','he','her','at','its']

MENU = '''
    Select from the menu:
        c: display categories
        f: find images by category
        i: find max instances of categories
        m: find max number of images of categories
        w: display the top ten words in captions
        q: quit
        
    Choice: '''

def get_option():
   '''
   Prompt the user for a valid option (use the MENU variable 
   defined in the starter code)and return it as a string. 
   If an invalid option is input, an error message 
   is displayed, and the user is re-prompted until a valid one is input
   The user input can be input as upper or
   lowercase, but it should be converted to lowercase before being returned.
   
   Parameters: none
   Returns: str (lower case)
   Displays: prompts & error messages
   '''
   l = ["c","f","i","m","w","q"]
   while True:
       i_string = input(MENU).lower()
       if i_string in l:
           break
       else:
           print("Incorrect choice.  Please try again.")
           continue
   return i_string
    
def open_file(s):
   '''
   Prompts for a file name and continues to prompt until a file is correctly 
   opened. The prompt will be customized using the parameter (string).
   
   Parameters: string
   Returns: file pointer
   Displays: prompts & error messages
   '''
    # loop to input check
   while True:
       # variable that stores file name
       file_name = input("Enter a {} file name: ".format(s))
       try:
           # opening file for reading with encoding
           fp = open(file_name,encoding='utf-8',)
           break
       except:
           # error message
           print("File not found.  Try again.")
           continue
   # returns file pointer
   return fp
   
        
def read_annot_file(fp1):
   ''' Read the JSON file referenced by the fp1 parameter. Use the 
   json module’s load method: json.load(fp1). 
   
   Parameters: file pointer
   Returns: dictionary of dictionaries
   Displays: nothing
    '''
   main_dictionary = json.load(fp1)
   return main_dictionary
   

def read_category_file(fp2):
   '''
   The category file is a text file where each line is space separated:
       int string
   Create a dictionary whose key is the int and whose value is the string.
   No key appears twice in any file,so no checking if key is already in 
   dictionary
   
   Parameters: file pointer
   Returns: dictionary
   Displays: nothing
   '''
   new_dictionary = {}
   for x in fp2:
       key = x.split()[0]
       int_key = int(key)
       string_value = x.split()[1]
       new_dictionary[int_key] = string_value
   return new_dictionary


def collect_catogory_set(D_annot,D_cat):
   '''
   This function creates a set of the categories
   actually used in the D_annot dictionary. The categories used are in the 
   list under the 'bbox_category_label' key for each image. Use of multiple 
   nested loops to get to the list of numbers. checks whether current 
   numbers are in the dictionary obtained from read_category_file function.
   If the number is present, adds the object associated with number to the set
   which is taken from the dictionary obtained in read_category_file function
   
   Parameters: dictionary of dictionaries, dictionary
   Returns: set of strings
   Displays: nothing
   '''
   set_of_objects = set()
   for first_dictionary in D_annot:
       for second_entry in D_annot[first_dictionary]:
           if second_entry == "bbox_category_label":
               for number in D_annot[first_dictionary][second_entry]:
                   if number in D_cat:
                       set_of_objects.add(D_cat[number])
   return set_of_objects
                       

def collect_img_list_for_categories(D_annot,D_cat,cat_set):
   ''' 
   This function creates a mapping of each category to the list of images that 
   has an instance of that category. The key will be the category, e.g. truck 
   (string), and the value will be a list of images(strings). 
   The list of images will be sorted in increasing value, i.e. 
   default sorting (notethat the images are strings (of digits) so you are 
   actually sorting strings).
   Parameters: dictionary of dictionaries, dictionary, set of strings
   Returns: dictionary of sorted lists
   Displays: nothing
   '''
   dct = {}
   for obj in cat_set:
       dct[obj] = []
       for first_dictionary in D_annot:
           for second_entry in D_annot[first_dictionary]:
               if second_entry == "bbox_category_label":
                   for number in D_annot[first_dictionary][second_entry]:
                       if obj == D_cat[number]:
                           dct[obj].append(first_dictionary)
   for i in dct:
       dct[i].sort()
   return dct
                       

def max_instances_for_item(D_image):
   ''' 
   Find the most occurrences of an object (category) across all images.
   The parameter is the dictionary returned from 
   the collect_img_list_for_categories function.
   Parameters: dictionary of sorted lists
   Returns: tuple
   Displays: nothing
   '''
   lst = []
   for obj in D_image:
       
       x = int(len(D_image[obj]))
       t = (x,obj)
       lst.append(t)
   highest = max(lst,key = itemgetter(0))
   return highest
       

def max_images_for_item(D_image):
   '''
   This function is almost identical to max_instances_for_item. In this function,
   find the most images that an object (category) appears in. 
   That is, if there are two dogs in an image, that
   counts as one image that a dog appears in.
   Parameters: dictionary of sorted lists
   Returns: tuple
   Displays: nothing
   '''
   lst = []
   for obj in D_image:
       
       x = int(len(set(D_image[obj])))
       t = (x,obj)
       lst.append(t)
   highest = max(lst,key = itemgetter(0))
   return highest
       
   

def count_words(D_annot):
   '''
   Count the occurrences of words in captions. Returns a list of tuples of 
   words and their count of the number of occurrences across all captions.
   The first element of the tuple is the count, and the second element is the 
   word.
   Parameters: dictionary of dictionaries
   Returns: list of tuples
   Displays: nothing
   '''
   dictionary = {}
   for first_dictionary in D_annot:
       for second_entry in D_annot[first_dictionary]:
           if second_entry == "cap_list":
               for sentence in D_annot[first_dictionary][second_entry]:
                   word_list = sentence.split()
                   for word in word_list:
                       word = word.strip(string.punctuation)
                       if word not in STOP_WORDS:
                           if word in dictionary:
                               dictionary[word] = dictionary[word]+1
                           else:
                               dictionary[word] = 1
   count_list = []             
   for word  in dictionary:
       t = (dictionary[word],word)
       count_list.append(t)
   count_list.sort(reverse = True)
   return count_list
                       
   

def main():    
    print("Images\n")
    # your code goes here
    jsonfp = open_file("JSON image")
    categoryfp = open_file("category")
    D_annot = read_annot_file(jsonfp)
    D_cat = read_category_file(categoryfp)
    cat_set = collect_catogory_set(D_annot, D_cat)
    image_dictionary = collect_img_list_for_categories(D_annot, D_cat, cat_set)
    
    while True:
        user_input = get_option()
        if user_input == "q":
            break
        elif user_input == "c":
            print("\nCategories:")
            category_list = []
            for category in cat_set:
                category_list.append(category)
            category_list.sort()  
            for i in category_list:
                string = i +","
            string = string[:-2]
            print(string)
        elif user_input == "f":
            print("\nCategories:")
            category_list = []
            for category in cat_set:
                category_list.append(category)
            category_list.sort()  
            for i in category_list:
                string = i +","
            string = string[:-2]
            print(string)
            while True:
                user_category = input("Choose a category from the list above: ")
                if user_category in category_list:
                    break
                else:
                    print("Incorrect category choice.")
                    continue
            print("\nThe category {} appears in the following \
                  images:".format(user_category))
                  
                  
                  
        elif user_input == "i":
            img_max = max_instances_for_item(image_dictionary)
            print("\nMax instances: the category {} appears {} times in images.".format(img_max[1],img_max[0]))
            
        elif user_input == "m":
            img_max = max_images_for_item(image_dictionary)
            print("\nMax images: the category {} appears in {} images.".format(img_max[1],img_max[0]))
        
        elif user_input == "w":
            count_word = count_words(D_annot)
            numm = int(input("\nEnter number of desired words: "))
            while numm <= 0: # prints error message if input is a negative number
                print("Error: input must be a positive integer: ")
                numm = input("\nEnter number of desired words: ")
            if numm > 0: # goes through code if positive number is entered
                print("\nTop {} words in captions.".format(numm))
                print("{:<14s}{:>6s}".format("word","count"))
                for line in count_word[:numm]:
                    print("{:<14s}{:>6d}".format(line[1],line[0]))
            
    print("\nThank you for running my code.") 
    
# Calls main() if this modules is called by name
if __name__ == "__main__":
    main()     
