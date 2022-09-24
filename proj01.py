#Computer Project 1

#Purpose : Easily convert rods into desirable units

# Algorithm
    #Write all required constants.
    #Prompt for rods from the user
    #Convert rods to desired units like miles and meters
    # Round off the numbers acquired to 3 decimals for ease of use
    # Display each individual conversion done.
    #Make final arithmetic calculations for minutes required
    #Display all required conversions. 

ROD_TO_METER = 5.0292
METER_TO_FEET = 0.3048
MILES_TO_METERS = 1609.34
FURLONG_TO_ROD = 40
AVG_WALKING_SPEED = 3.1



num_rod = float(input("Input rods: "))
print("You input",num_rod,"rods.")
print("    ")
print("Conversions")
num_meters = num_rod*ROD_TO_METER
print("Meters:",round(num_meters,3))
num_feet = num_meters/METER_TO_FEET
print("Feet:",round(num_feet,3))
num_miles = num_meters/MILES_TO_METERS
#num_miles = round(num_miles,3)
print("Miles:",round(num_miles,3))
num_furlong = num_rod/FURLONG_TO_ROD
print("Furlongs:",num_furlong)
num_minutes = num_miles/AVG_WALKING_SPEED*60
num_minutes = round(num_minutes,3)
print("Minutes to walk",num_rod,"rods:",num_minutes)