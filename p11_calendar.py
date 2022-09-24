
###########################################################
    #   Project 11_calendar file
    #   This .py file contains the P11_Calendar() class. 
    #   Functions in the class:
    #   __init__() : Initialize function
    #   add_event : checks if the function can be added to calendar and adds
    #   it to calendar if valid.
    #   delete_event(): Function is used to delete event at the specified date 
    #   and time
    #   day_schedule() :sorts the list for the date by time
    #   __str__() : Function is used to provide output to the user.
    #   __repr__(): Function was provided
    #   __eq__() : Function was provided and makes use of the equal sign
###########################################################

class P11_Calendar():
    def __init__(self):
        '''
        Initialize the public attribute event_list (which is a list of events)
        to an empty list.
        parameters: self
        displays: nothing
        returns nothing
        '''
        # creates an event_list 
        self.event_list = []
        
    def add_event(self,e):
        '''
        Append event e to the list of events attribute if the
        event doesn’t conflict with any events already in the list.
        parameters: self,event
        displays: nothing
        returns: Boolean values based on whether event was added or not. 
        '''
        # add event if event_list is empty
        if len(self.event_list) == 0:
            self.event_list.append(e)
            return True
        else:
        # if event_list is not empty, check if event can be added
            for i in self.event_list:
                start_time, end_time = i.get_time_range()
                start_time1, end_time1  = e.get_time_range()
                if start_time1 >= start_time and start_time1 <= end_time\
                    and i.get_date() == e.get_date():
                    return False
                if end_time1 >= start_time and end_time1 <= end_time \
                    and i.get_date() == e.get_date():
                    return False
            else:
                self.event_list.append(e)
                return True
                    

    def delete_event(self,date,time):
        '''
        Delete the event at the specified date and time.
        parameters: self,date, time
        displays: nothing
        returns: Boolean values based on whether event was deleted or not. 
        '''
        for event in self.event_list:
            event_date = event.get_date()
            event_time = event.get_time()
            # checks if date and time given by user are in the event list 
            # and deletes it.
            if event_date == date and event_time == time:
                index_of_event = self.event_list.index(event)
                del self.event_list[index_of_event]
                return True
            else:
                continue
                return False
        
    
    def day_schedule(self,date):
        '''
        Return a sorted list of events on the date in the date parameter 
        by time in ascending order.Uses list.sort to sort list 
        makes use of tuples inside a list to sort through by time. 
        parameters: self,date
        displays: nothing
        returns: list of sorted events
        '''
        day_list = []
        temp_list = []
        # go through event_list to find date and sort by time
        for event in self.event_list:
            if event.get_date() == date:
                time = event.get_time()
                time_list = time.split(":")
                hh = int(time_list[0])
                mm = int(time_list[1])
                day_time = hh*60+mm
                temp_t = (day_time,event)
                day_list.append(temp_t)
        day_list.sort()
        for i in day_list:
            temp_list.append(i[1])
        return temp_list
           
    def __str__(self):
        '''
        Return a string that has an event on each line. Have one header line:
        'Events in Calendar:\n'
        parameters: self
        displays: nothing
        returns: string of all events 
        '''
        string = 'Events in Calendar:\n'
        for event in self.event_list:
        # add each event to the string and return it
            string = string + event.__str__() +"\n"
        return string
    
    def __repr__(self):
        s = ''
        for e in self.event_list:
            s += e.__repr__() + ";"
        return s[:-1]
    
    def __eq__(self,cal):
        '''PROVIDED: returns True if all events are the same.'''
        if not isinstance(cal,P11_Calendar):
            return False
        if len(self.event_list) != len(cal.event_list):
            return False
        L_self = sorted(self.event_list)
        L_e = sorted(cal.event_list)
        for i,e in enumerate(L_self):
            if e != L_e[i]:
                return False
        return True
        
