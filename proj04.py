###########################################################
    #  Computer Project #4
    #   is_float() function
    #   int_to_base13() function
    #   tridecimal_expansion() function
    #   tridecimal_to_conway() function
    #   zeta() fucntion
    #   main()
    #   Algorithm:
    #       while loop runs until user inputs q
    #       error checking is user inputs something other than z,c,q
    #       if input == z
    #       check for input, run zeta function if input is correct
    #       if input == c
    #       check for input, run int_to_base13() function
    #                            tridecimal_expansion() function
    #                            tridecimal_to_conway() function
    #       if input == q
    #       quit
    
    ###########################################################



'''Remember your program header.'''

DELTA = 10**-7  # used for the zeta function

PROMPT = "Enter Z for Zeta, C for Conway, Q to quit: "

def is_float(s):
    '''function is to check whether given string is a float or not.
    uses try and except to return Boolean values.'''
    try:
        float(s)
        return True
    except ValueError:
        return False

def int_to_base13(n):
    ''' Function to convert given input from base 10 to base 13.
        n = input by user(int)
            uses a sinple algorithm of continous division to form number to 
            base 13
        returns x (string)'''
    x = ""
    n = int(n)
    while n > 0:
        remainder = n % 13
        if remainder == 10:
            x = "A"+x
        elif remainder == 11:
            x = "B"+x
        elif remainder == 12:
            x = "C"+x
        else:
            x = str(remainder) + x
        n = n//13
    return x

def tridecimal_expansion(n_str):
    ''' Function to expand the base 13 number obtained. 
        n_str(str) is input
        if A is encoutnered, then replaced with +
        if B is encoutnered, then replaced with -
        if C is encoutnered, then replaced with .
        returns n_str with all A,B,C's replaced'''
    for i in n_str:
        if i == "A":
            n_str = n_str.replace("A","+",1)
        elif i == "B":
           n_str=  n_str.replace("B","-",1)
        elif i == "C":
           n_str=  n_str.replace("C",".",1)
    return n_str

        
def tridecimal_to_conway(n_str):
    ''' Function to convert n_str(input) to a conway float
        Algorithm:
            reverses the string
            adds each character index by index and keeps checking for float
            by using is_flaot function defined above.
            checks for float and '.' in given conway
        if conway float is attainable, returns conway float,
        else returns 0'''
    new_conway = ""
    n_str = n_str[::-1]
    for i in n_str:
        new_conway = i + new_conway
        if is_float(new_conway):
            continue
        else:
            new_conway = new_conway[1:]
            break 
    if is_float(new_conway)and "." in new_conway:
        return float(new_conway)
    else:
        return 0
        

def zeta(n):
    ''' Function used to calcualte sum of an infinite series.
        n is the input that is used as the exponent in all cases.
        DELTA is defined as 10**-7
        new local variables are made for the function
        code is executed only till the difference between two consecutive
        terms is less than DELTA
        total_sum is incremented with term as long as loop runs
        inputs => n (float)
        returns => total_sum(flaot)'''
        
    total_sum = 0
    power = float(n)
    n_term = 0
    difference = 1
    term = 0
    increment = 1
    if power <= 0:
        return None
    else:
        while difference > DELTA:
            term = 1/(increment**power)
            total_sum = total_sum+term
            increment = increment +1
            n_term = 1/(increment**power)
            difference = abs(n_term - term) 
        return total_sum

def main():
    # by convention "main" doesn't need a docstring
    print("Functions")
    while True:
        while True:
            str_input = input(PROMPT).lower()
            if str_input == "z" or str_input == "c" or str_input == "q":
                break
            else:
                print("Error in input.  Please try again.")
        if str_input == "q":
            break
        elif str_input == "z":
            print("Zeta")
            while True:
                z_prompt = input("Input a number: ")
                if z_prompt.isdigit() or z_prompt[1:].isdigit():
                    break
                else:
                    print("Error in input.  Please try again.")
                    continue
            print(zeta(z_prompt))
        elif str_input == "c":
            print("Conway")
            while True:
                c_prompt = input("Input a positive integer: ")
                if c_prompt.isdigit():
                    break
                else:
                    print("Error in input.  Please try again.")
                    continue
            x = int_to_base13(c_prompt)
            print("Base 13:",x)
            y = tridecimal_expansion(x)
            print("Tridecimal:",y)
            z = tridecimal_to_conway(y)
            print("Conway float:",z)
            
    # your code goes here    
    print("\nThank you for playing.")
        
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main()