###########################################################

    #  Project 5
    #
    #  open_file function
    #  opens file and returns file pointer
    #  get_month function
    #  returns 3 letter month string
    #  best_surf function
    #  returns the best day,hour,time,wavelength and DPD for surfing
    #   Algorithm for main:
    #       "Wave Data" is displayed
    #       9 variables are created
    #       open_file() function is called.
    #       readline is used to parse over headers
    #       for each line in the file
    #       check for 99.00 to skip over that line
    #       assign values and increment count and total wavelength
    #       call best_surf function to determine best day and time
    #       calculate average, min and max
    #       Display given average, min and max
    #       Use print and format statements to display all info
    #       get_month_str function is used in the print statement
    #  

    ###########################################################
def open_file():
    ''' Function to open the specified file.
        prompts from input from user for year
        uses while loop to loop until input is correct
        uses try and except to open the file
        input: year(str)
        output: file pointer'''
    while True:
        input_year = input("Input a year: ")
        file = "wave_data_" + input_year + ".txt"
        try:
            f_open = open(file,"r")
            break
        except:
            print("File does not exist. Please try again.")
            continue
    return f_open

def get_month_str(mm):
    ''' Function to convert a numeric string into a 3 character string month.
        uses 12 if statements for each month
        input: numeric string(str)
        output: 3 letter representation of months(str)
        '''
    if mm == "01":
        return "Jan"
    if mm == "02":
        return "Feb"
    if mm == "03":
        return "Mar"
    if mm == "04":
        return "Apr"
    if mm == "05":
        return "May"
    if mm == "06":
        return "Jun"
    if mm == "07":
        return "Jul"
    if mm == "08":
        return "Aug"
    if mm == "09":
        return "Sep"
    if mm == "10":
        return "Oct"
    if mm == "11":
        return "Nov"
    if mm == "12":
        return "Dec"
    
def best_surf(mm,dd,hr,wvht,dpd,best_mm,best_dd,best_hr,best_wvht,best_dpd):
    ''' Function to determine which day and time has the best surf.
        If time is too early or too late, current values are returned.
        If time is appropriate, then wvht is compared to determine which 
        day and time are better. if wvht and best_wvht are equal, dpd's are 
        compared.
        input=> mm - month(str)
                dd - day(str)
                hr - hour(int)
                wvht- waveheight(float)
                dpd- DPD(float)
                best_mm - best month(str)
                best_dd - best day(str)
                best_hr - best hour(int)
                best_wvht- best waveheight(float)
                best_dpd - best DPD(float)
        output=> mm - month(str)
                dd - day(str)
                hr - hour(int)
                wvht- waveheight(float)
                dpd- DPD(float)
                OR
                best_mm - best month(str)
                best_dd - best day(str)
                best_hr - best hour(int)
                best_wvht- best waveheight(float)
                best_dpd - best DOD(float)'''
    if hr < 6 or hr >= 19:
        return(best_mm,best_dd,best_hr,best_wvht,best_dpd)
    else:
        if wvht > best_wvht:
            return(mm,dd,hr,wvht,dpd)
        elif wvht < best_wvht:
            return(best_mm,best_dd,best_hr,best_wvht,best_dpd)
        elif wvht == best_wvht:
            if dpd > best_dpd:
                return (mm,dd,hr,wvht,dpd)
            else:
                return(best_mm,best_dd,best_hr,best_wvht,best_dpd)
            
def main():  
    # by convention "main" doesn't need a docstring
    print("Wave Data")
    total_wvht = 0
    count_wvht= 0
    max_wvht = 0
    min_wvht = 10**6
    best_mm = ""
    best_dd = ""
    best_wvht = 0
    best_dpd = 0
    best_hr = 0
    
    fp = open_file()
    
    fp.readline()
    fp.readline()
    
    for l in fp:
        if "99.00" in l[30:42]:
            continue
        mm = l[5:7].strip()
        dd = l[8:10].strip()
        hr = int(l[11:13].strip())
        wvht = float(l[30:36].strip())
        dpd = float(l[37:42].strip())
        
        total_wvht = total_wvht + wvht
        count_wvht = count_wvht + 1
        
        if wvht > max_wvht:
            max_wvht = wvht
        if wvht < min_wvht:
            min_wvht = wvht
        
        best_mm,best_dd,best_hr,best_wvht,best_dpd = best_surf\
        (mm, dd, hr, wvht, dpd, best_mm, best_dd, best_hr, best_wvht, best_dpd)
        
    wvht_average = total_wvht/count_wvht 
    print("\nWave Height in meters.")
    print("{:7s}: {:4.2f} m".format("average",wvht_average))
    print("{:7s}: {:4.2f} m".format("max",max_wvht))
    print("{:7s}: {:4.2f} m".format("min",min_wvht))
    print("\nBest Surfing Time:")
    print("{:3s} {:3s} {:2s} {:>6s} {:>6s}"\
          .format("MTH","DAY","HR","WVHT","DPD"))
    print("{:3s} {:>3s} {:2d} {:5.2f}m {:5.2f}s"\
          .format(get_month_str(best_mm),best_dd,best_hr,best_wvht,best_dpd))
        
        
        

# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main()
    
    
    
    

