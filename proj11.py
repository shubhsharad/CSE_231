###########################################################
    # Project 11
    #   Import P11_Calendar class
    #   Import P11_Event class
    #   MENU constant
    #   check_time() function. Function used to check whether given time and 
    #   duration are valid 
    #   event_prompt() function: Function is used to check if event entered by
    #   the user is valid or not. 
    #   main() function
    #       calendar is initialized
    #       while loop
    #           MENU is dispalyed
    #           user_input is taken
    #           if user_input is a
    #               event is added
    #           if user_input is l
    #               events are listed 
    #           if user_input is d
    #               event is deleted
    #           if user_input is q
    #               program quits
###########################################################
from p11_calendar import P11_Calendar
from p11_event import P11_Event

CAL_TYPE = ['meeting','event','appointment','other']

MENU = '''Welcome to your own personal calender.
  Available options:
    (A)dd an event to calender
    (D)elete an event
    (L)ist the events of a particular date
    (Q)uit'''

def check_time(time,duration):
    '''
    Return True if the time and duration are valid; return False otherwise
    checks if time and duration are valid for the event
    parameters: time and duration
    displays: nothing
    returns: Boolean values based on whether time and duration are valid or not
    '''
    # creates a list seperated by ";"
    seperated_time = time.split(":")
    #hours
    hh = int(seperated_time[0])
    #minutes
    mm = int(seperated_time[0])
    if type(duration) == str:
        return False
    else:
        duration = int(duration)
    #converting to minutes
    if hh*60+duration > 6*60 and hh*60+duration < 17*60 and duration > 0:
        return True
    else:
        return False
            
def event_prompt():
    '''
    Prompt for an event; re-prompt until a valid event is entered.
    Return the event.
    Prompt for date, time, duration, and cal_type. 
    checks if event entered is valid or not. 
    parameterr: None
    displays: Error message
    returns: event
    '''
    # while loop
    while True:
        # date from user
        date = input("Enter a date (mm/dd/yyyy): ")
        # time from user
        time = input("Enter a start time (hh:mm): ")
        # duration from user
        duration = int(input("Enter the duration in minutes (int): "))
        # cal_type from meeting
        cal_type = \
            input("Enter event type ['meeting','event','appointment','other']: ")
        event = P11_Event(date,time,duration,cal_type)
        if event.valid == True and check_time(time,duration) == True:
            return event
            break
        else:
            print("Invalid event. Please try again.")
            continue
    
def main():
    # initialize calendar
    calendar = P11_Calendar()
    while True:
        print(MENU)
        # take input from the user
        user_input = input("Select an option: ").lower()
        # if user_input is a
        if user_input == "a":
            # event_prompt() function
            user_event = event_prompt()
            print("Add Event")
            if calendar.add_event(user_event) == False:
                print("Event was not added.")
            else:
                print("Event successfully added.")
        # if user_input is d
        if user_input == "d":
            print("Delete Event")
            # take date and time from the user
            date = input("Enter a date (mm/dd/yyyy): ")
            time = input("Enter a start time (hh:mm): ")
            # delete the event
            delete_event = calendar.delete_event(date,time)
            if delete_event == True:
                print("Event successfully deleted.")
            else:
                print("Event was not deleted.")
        # if user_input is l
        if user_input == "l":
            print("List Events")
            # take date from user
            date = input("Enter a date (mm/dd/yyyy): ")
            # day_schdeule function
            event_list = calendar.day_schedule(date)
            if len(event_list) != 0:
                for event in event_list:
                    print(event)
            else:
                print("No events to list on ",date)
        # if user_input is q
        if user_input == "q":
            break
        

if __name__ == '__main__':
     main()
