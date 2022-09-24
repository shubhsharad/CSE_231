###########################################################
    #  Computer Project #2
    #
    #  Algorithm
    #    display Banner for the program
    #    Take a prompt from the user
    #    use if and while statements to start a loop
    #       take input from user for details of rental
    #       use another while loop to correct wrong entries
    #       calculate total cost and miles driven for all cases
    #       display customer summary
    #       give the user option to continue or finish the program
    #    display closing message
    
    ###########################################################
import math

#Code to Display Banner
BANNER = "\nWelcome to Horizons car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BD, D, W) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)" 
print(BANNER)
print("")

#Prompt from the user to continue the program
prompt = input("Would you like to continue (A/B)? ")
if prompt == "B":
    print("Thank you for your loyalty.")
#While loop to take input and calculate required variables
while prompt == "A":
    class_code = input("\nCustomer code (BD, D, W): ")
    # while loop to check whether input class_code is correct
    while class_code != "BD" and class_code != "D" and class_code != "W":
        print("\n\t*** Invalid customer code. Try again. ***")
        class_code = input("\nCustomer code (BD, D, W): ")
    #input of Required variables
    no_of_days = int(input("\nNumber of days: "))
    odo_reading_start = int(input("Odometer reading at the start: "))
    odo_reading_end = int(input("Odometer reading at the end:   "))
    #if clause to calculate values for BD class code
    if class_code == "BD":
        if odo_reading_start > odo_reading_end:
            miles_driven = ((1000000-odo_reading_start)+odo_reading_end)/10
        else:
            miles_driven = (odo_reading_end-odo_reading_start)/10
        total_cost = no_of_days*40 + miles_driven*0.25       
    #if clause to calculate values of D class code
    if class_code == "D":
        if odo_reading_start > odo_reading_end:
            miles_driven = ((1000000-odo_reading_start)+odo_reading_end)/10
        else:
            miles_driven = (odo_reading_end-odo_reading_start)/10
        avg_miles_day = miles_driven/no_of_days
        if avg_miles_day > 100:
            total_cost = no_of_days*60 + (miles_driven-(no_of_days*100))*0.25
        else:
            total_cost = no_of_days*60
    #if clause code to calculate values of W class code
    if class_code == "W":
        if odo_reading_start > odo_reading_end:
            miles_driven = ((1000000-odo_reading_start)+odo_reading_end)/10
        else:
            miles_driven = (odo_reading_end-odo_reading_start)/10
        no_of_weeks = math.ceil(no_of_days/7)
        avg_miles_week = miles_driven/no_of_weeks
        if avg_miles_week > 900 and avg_miles_week < 1500:
            total_cost = no_of_weeks*190+ no_of_weeks*100
        elif avg_miles_week >1500:
            total_cost = no_of_weeks*190+ no_of_weeks*200+ \
            (miles_driven-1500*no_of_weeks)*0.25
        else:
            total_cost = no_of_weeks*190
    #Final Customer Summary
    print("\nCustomer summary:")
    print("\tclassification code:", class_code)
    print("\trental period (days):", no_of_days)
    print("\todometer reading at start:", odo_reading_start)
    print("\todometer reading at end:  ", odo_reading_end)
    print("\tnumber of miles driven: ", miles_driven)
    print("\tamount due: $", float(total_cost))
    print("")
    #Prompt for user to continue the program or exit
    prompt =input("Would you like to continue (A/B)? ")
    if prompt == "B":
        #Closing Message
        print("Thank you for your loyalty.")
   
    
   
