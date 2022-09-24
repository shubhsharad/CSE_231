###########################################################
    #   Project 11_ event file
    #   This .py file contains the P11_Event() class. 
    #   Functions in the class:
    #   __init__() : Initialize function
    #   get_date() : returns the date
    #   get_time() : returns the time
    #   get_time_range() : returns the start and end time in a tuple
    #   __str__() : Function is used to provide output to the user.
    #   __repr__(): Function was provided
    #   __lt__() : Function compares the time of two events and returns True or
    #   False
    #   __eq__() : Function was provided and makes use of the equal sign
###########################################################
CAL_TYPE = ['meeting','event','appointment','other']

class P11_Event():
    def __init__(self,date=None,time='9:00',duration=60,cal_type='meeting'):
        '''
        All parameters are strings except duration (int) and self.
        Initialize the public attributes: date, time, duration, cal_type, valid
        If a time is not well formed, assign None.
        If a date is not well formed, assign None.
        If duration is not a positive integer, assign None.
        If cal_type is not in CAL_TYPE, assign None.
        If any attributeabove is None, valid is False, otherwise it is True
        Parameters: Date, time, duration, cal_type
        displays: nothing
        returns : nothing
        '''
        # initialize valid
        self.valid = True
        # initialize date
        self.date = date
        if self.date == None:
            self.date = None
            self.valid = False
        elif self.date != None:
            date_list = self.date.split("/")
            if len(date_list) != 3:
                self.date = None
                self.valid = False
            else:
                mm = int(date_list[0])
                dd = int(date_list[1])
                yyyy = int(date_list[2])
                if mm >= 1 and  mm<= 12 and dd>= 1 and dd <= 31 \
                    and yyyy >= 0000 and yyyy <= 9999:
                    self.date = date
                else:
                    self.date = None
                    self.valid = False
        # initialize time
        self.time = time
        if self.time == None:
            self.time = None
            self.valid = False
        
        elif self.time != None:
            if self.time.isalpha():
                self.time = None
                self.valid = False
            else:
                time_list = self.time.split(":")
                if len(time_list) != 2:
                    self.time = None
                    self.valid = False
                else:
                    hh = int(time_list[0])
                    mm = int(time_list[1])
                    if hh >= 0 and hh <= 23 and mm >= 0 and mm <= 59:
                        self.time = time
                    else:
                        self.time = None
        # initialize duration
        self.duration = duration
        if type(self.duration) == str:
            self.duration= None
            self.valid = False
        elif self.duration >= 0:
            self.duration = duration
        else:
            self.duration = None
            self.valid = False
        # initialize cal_type
        self.cal_type = cal_type
        if self.cal_type not in CAL_TYPE:
            self.cal_type = None
            self.valid = False
        else:
            self.cal_type = cal_type
        
    def get_date(self):
        '''
        Returns the date.
        Parameters: self
        displays: Nothing
        returns: date
        '''
        # returns the date
        return self.date
    def get_time(self):
        '''
        returns the time.
        Parameters: self
        displays: Nothing
        returns: time
        '''
        # returns the time
        return self.time    
    
    def get_time_range(self):
        '''
        Calculate the end time and return a tuple: (start_time, end_time).
        The start time and end time are in minutes.
        parameters: self
        displays: nothing
        returns: tuple
        '''
        # make a list with hh and mm
        time_list = self.time.split(":")
        hh = int(time_list[0])
        mm = int(time_list[1])
        # start time in minutes
        start_time = hh*60 + mm
        end_time =  start_time + self.duration
        # make a tuple
        t = (start_time,end_time)
        return t
    
    def __str__(self):
        '''
        Return a string formatted as: 01/01/0101: start: 9:00; duration: 60
        If any attributes are False, return None as a string
        parameters: self
        displays: nothing
        returns: string
        '''
        if self.valid == True:
            string = self.date +": "+"start: "+\
                self.time+"; duration: "+str(self.duration)
        else:
            string = "None"
        return string
    
    def __repr__(self):
        if self.date and self.time and self.duration:
            return self.date + ';' + self.time + '+' + str(self.duration)
        else:
            return 'None'

    def __lt__(self,e):
        '''
        Return True if self’s time is less than e’s time; False otherwise.
        If either time is None, return False.
        Function is used to check which time is greater.
        parameters: self
        displays: nothing
        returns: None or True or False
        '''
        if self.time == None:
            return False
        else:
            time_list = self.time.split(":")
            hh = int(time_list[0])
            mm = int(time_list[1])
            self_time = hh*60 + mm
        if e.time == None:
            return False
        else:
            time_list1 = e.time.split(":")
            hh1 = int(time_list1[0])
            mm1 = int(time_list[1])
            e_time = hh1*60 +mm
        if self_time >= e_time:
            return False
        if self_time < e_time:
            return True
    
    def __eq__(self,e):
        '''PROVIDED'''
        return self.date == e.date and self.time == e.time and self.duration == e.duration and self.cal_type == e.cal_type # and self.status == e.status

        
