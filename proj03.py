print("2021 MSU Undergraduate Tuition Calculator.\n")
###########################################################
    #  Computer Project #3
    #
    #  Algorithm
    #    prompt from user for year in college
    #    depending on prompt, different approaches are taken
        #    if year is freshman or sophomore, ask if in engineering or
        #    James Madison College
        #    calculate tuition total depending on freshman or sophomore
        #    dispaly total tuiton and ask for further calculations
        #    if year is junior or senior, ask if in engineering or
        #    sciences,health or business
        #       if not in these, ask if in james Madison college
        #    calculate tuition total depending on junior or senior
        #    dispaly total tuiton and ask for further calculations
    #   Display final message.
###########################################################
t_cost = 0
all_tax = 24
jmc_tax = all_tax + 7.5
"Invalid input. Try again."
program_continue = "yes"

#while loop to continue program
while program_continue == "yes":
    year_college = (input("Enter Level as freshman, sophomore, junior, senior: ")).lower()
    
    if year_college != "freshman" and year_college != "sophomore" and \
    year_college != "junior" and year_college !="senior":
        print("Invalid input. Try again.")
    # year of college is freshman
    if year_college =="freshman":
        col_eng = (input("Are you admitted to the College of Engineering \
(yes/no): ")).lower()
        if col_eng == "yes":
            
            #code to check if credits is 0,a string or in decimals
            while True:
                no_of_credits = input("Credits: ")
                if no_of_credits.isdigit() == False:
                    print("Invalid input. Try again.")
                    continue 
                elif int(no_of_credits) <= 0:
                    print("Invalid input. Try again.")
                    continue 
                else:
                    break
                
            # calculating cost for college of engineering
            if int(no_of_credits) <= 11 and int(no_of_credits) <=4 :
                t_cost = int(no_of_credits)*482 + 402 + all_tax
                #print(t_cost)
                if int(no_of_credits) >= 6:
                    t_cost = t_cost + 5
                    print("Tuition is ${:,.2f}.".format(t_cost))
                else:
                    print("Tuition is ${:,.2f}.".format(t_cost))
            elif int(no_of_credits) <= 11 and int(no_of_credits) >4 :
                t_cost = int(no_of_credits)*482 + 670 + all_tax
                #print(t_cost)
                if int(no_of_credits) >= 6:
                    t_cost = t_cost + 5
                    print("Tuition is ${:,.2f}.".format(t_cost))
                else:
                    print("Tuition is ${:,.2f}.".format(t_cost))
            elif int(no_of_credits) >11 and int(no_of_credits) <= 18:
                t_cost = 7230+670 + all_tax
                #print(t_cost)
                if int(no_of_credits) >= 6:
                    t_cost = t_cost + 5
                    print("Tuition is ${:,.2f}.".format(t_cost))
                else:
                    print("Tuition is ${:,.2f}.".format(t_cost))
            elif int(no_of_credits) >18:
                t_cost = 7230+(int(no_of_credits)-18)*482 + 670 + all_tax
                #print(t_cost)
                if int(no_of_credits) >= 6:
                    t_cost = t_cost + 5
                    print("Tuition is ${:,.2f}.".format(t_cost))
                else:
                    print("Tuition is ${:,.2f}.".format(t_cost))
                #code to ask to continue program or not
            program_continue = input("Do you want to do another calculation \
(yes/no): ").lower()
        #code to check if in JMC or not
        if col_eng =="no":
             col_jmc = input("Are you in the James Madison College (yes/no): ")
             if col_jmc == "yes":
                 
                 while True:
                     no_of_credits = input("Credits: ")
                     if no_of_credits.isdigit() == False:
                         print("Invalid input. Try again.")
                         continue 
                     elif int(no_of_credits) <= 0:
                         print("Invalid input. Try again.")
                         continue 
                     else:
                         break         
                 #calculating cost for james madison college
                 if no_of_credits == 0 or no_of_credits.isalpha() == True:
                     print("Invalid input. Try again.")
                 elif int(no_of_credits) <= 11 and int(no_of_credits) <=4 :
                     t_cost = int(no_of_credits)*482 + jmc_tax
                     #print(t_cost)
                     if int(no_of_credits) >= 6:
                         t_cost = t_cost + 5
                         print("Tuition is ${:,.2f}.".format(t_cost))
                     else:
                         print("Tuition is ${:,.2f}.".format(t_cost))
                 elif int(no_of_credits) <= 11 and int(no_of_credits) >4 :
                     t_cost = int(no_of_credits)*482 + jmc_tax
                     #print(t_cost)
                     if int(no_of_credits) >= 6:
                         t_cost = t_cost + 5
                         print("Tuition is ${:,.2f}.".format(t_cost))
                     else:
                         print("Tuition is ${:,.2f}.".format(t_cost))
                 elif int(no_of_credits) >11 and int(no_of_credits) <= 18:
                     t_cost = 7230 + jmc_tax
                     #print(t_cost)
                     if int(no_of_credits) >= 6:
                         t_cost = t_cost + 5
                         print("Tuition is ${:,.2f}.".format(t_cost))
                 elif int(no_of_credits) >18:
                     t_cost = 7230+(int(no_of_credits)-18)*482 + jmc_tax()
                     if int(no_of_credits) >= 6:
                         t_cost = t_cost + 5
                         print("Tuition is ${:,.2f}.".format(t_cost))
                     else:
                         print("Tuition is ${:,.2f}.".format(t_cost))
                 program_continue = input("Do you want to do another calculation \
(yes/no): ").lower()
            # if not in engineering and JMC
             if col_jmc == "no":
                 while True:
                     no_of_credits = input("Credits: ")
                     if no_of_credits.isdigit() == False:
                         print("Invalid input. Try again.")
                         continue 
                     elif int(no_of_credits) <= 0:
                         print("Invalid input. Try again.")
                         continue 
                     else:
                         break
                 if no_of_credits == 0 or no_of_credits.isalpha() == True:
                     print("Tuition is ${:,.2f}.".format(t_cost))
                 elif int(no_of_credits) <= 11 and int(no_of_credits) <=4 :
                     t_cost = int(no_of_credits)*482 + all_tax
                     #print(t_cost)
                     if int(no_of_credits) >= 6:
                         t_cost = t_cost + 5
                         print("Tuition is ${:,.2f}.".format(t_cost))
                     else:
                         print("Tuition is ${:,.2f}.".format(t_cost))
                 elif int(no_of_credits) <= 11 and int(no_of_credits) >4 :
                     t_cost = int(no_of_credits)*482 + all_tax
                     #print(t_cost)
                     if int(no_of_credits) >= 6:
                         t_cost = t_cost + 5
                         print("Tuition is ${:,.2f}.".format(t_cost))
                     else:
                         print("Tuition is ${:,.2f}.".format(t_cost))
                 elif int(no_of_credits) >11 and int(no_of_credits) <= 18:
                     t_cost = 7230 + all_tax
                     #print(t_cost)
                     if int(no_of_credits) >= 6:
                         t_cost = t_cost + 5
                         print("Tuition is ${:,.2f}.".format(t_cost))
                     else:
                         print("Tuition is ${:,.2f}.".format(t_cost))
                 elif int(no_of_credits) >18:
                     t_cost = 7230+(int(no_of_credits)-18)*482 + all_tax
                     if int(no_of_credits) >= 6:
                         t_cost = t_cost + 5
                         print("Tuition is ${:,.2f}.".format(t_cost))
                     else:
                         print("Tuition is ${:,.2f}.".format(t_cost))
                 program_continue = input("Do you want to do another calculation \
(yes/no): ").lower()
    #check for sophomore    
    if year_college == "sophomore":
        col_eng = (input("Are you admitted to the College of Engineering \
(yes/no): ")).lower()
        #if in college of engineering
        if col_eng == "yes":
            #print(type(no_of_credits))
            while True:
                no_of_credits = input("Credits: ")
                if no_of_credits.isdigit() == False:
                    print("Invalid input. Try again.")
                    continue 
                elif int(no_of_credits) <= 0:
                    print("Invalid input. Try again.")
                    continue 
                else:
                    break
            # calculating tuition
            if no_of_credits == 0 or no_of_credits.isalpha() == True:
                print("Invalid input. Try again.")
            elif int(no_of_credits) <= 11 and int(no_of_credits) <=4 :
                t_cost = int(no_of_credits)*494 + 402 + all_tax
                #print(t_cost)
                if int(no_of_credits) >= 6:
                    t_cost = t_cost + 5
                    print("Tuition is ${:,.2f}.".format(t_cost))
                else:
                    print("Tuition is ${:,.2f}.".format(t_cost))
            elif int(no_of_credits) <= 11 and int(no_of_credits) >4 :
                t_cost = int(no_of_credits)*494 + 670 + all_tax
                #print(t_cost)
                if int(no_of_credits) >= 6:
                    t_cost = t_cost + 5
                    print("Tuition is ${:,.2f}.".format(t_cost))
                else:
                    print("Tuition is ${:,.2f}.".format(t_cost))
            elif int(no_of_credits) >11 and int(no_of_credits) <= 18:
                t_cost = 7410+670 + all_tax
                #print(t_cost)
                if int(no_of_credits) >= 6:
                    t_cost = t_cost + 5
                    print("Tuition is ${:,.2f}.".format(t_cost))
                else:
                    print("Tuition is ${:,.2f}.".format(t_cost))
            elif int(no_of_credits) >18:
                t_cost = 7410+(int(no_of_credits)-18)*494 + 670 + all_tax
                #print(t_cost)
                if int(no_of_credits) >= 6:
                    t_cost = t_cost + 5
                    print("Tuition is ${:,.2f}.".format(t_cost))
                else:
                    print("Tuition is ${:,.2f}.".format(t_cost))
       
            
            program_continue = input("Do you want to do another calculation \
(yes/no): ").lower()
        # to check whether in JMC
        if col_eng =="no":
            col_jmc = input("Are you in the James Madison College (yes/no): ")
            if col_jmc == "yes":
             #print(type(no_of_credits))
             while True:
                 no_of_credits = input("Credits: ")
                 if no_of_credits.isdigit() == False:
                     print("Invalid input. Try again.")
                     continue 
                 elif int(no_of_credits) <= 0:
                     print("Invalid input. Try again.")
                     continue 
                 else:
                     break
                
              #calculating cost   
             if no_of_credits == 0 or no_of_credits.isalpha() == True:
                 print("Invalid input. Try again.")
             elif int(no_of_credits) <= 11 and int(no_of_credits) <=4 :
                 t_cost = int(no_of_credits)*494 + jmc_tax
                 #print(t_cost)
                 if int(no_of_credits) >= 6:
                     t_cost = t_cost + 5
                     print("Tuition is ${:,.2f}.".format(t_cost))
                 else:
                     print("Tuition is ${:,.2f}.".format(t_cost))
             elif int(no_of_credits) <= 11 and int(no_of_credits) >4 :
                 t_cost = int(no_of_credits)*494 + jmc_tax
                 #print(t_cost)
                 if int(no_of_credits) >= 6:
                     t_cost = t_cost + 5
                     print("Tuition is ${:,.2f}.".format(t_cost))
                 else:
                     print("Tuition is ${:,.2f}.".format(t_cost))
             elif int(no_of_credits) >11 and int(no_of_credits) <= 18:
                 t_cost = 7410 + jmc_tax
                 #print(t_cost)
                 if int(no_of_credits) >= 6:
                     t_cost = t_cost + 5
                     print("Tuition is ${:,.2f}.".format(t_cost))
                 else:
                     print("Tuition is ${:,.2f}.".format(t_cost))
             elif int(no_of_credits) >18:
                 t_cost = 7410+(int(no_of_credits)-18)*494 + jmc_tax()
                 if int(no_of_credits) >= 6:
                     t_cost = t_cost + 5
                     print("Tuition is ${:,.2f}.".format(t_cost))
                 else:
                     print("Tuition is ${:,.2f}.".format(t_cost))
             program_continue = input("Do you want to do another calculation \
(yes/no): ").lower()
                # if not in JMC
             if col_jmc == "no":
                 #print(type(no_of_credits))
                 while True:
                     no_of_credits = input("Credits: ")
                     if no_of_credits.isdigit() == False:
                         print("Invalid input. Try again.")
                         continue 
                     elif int(no_of_credits) <= 0:
                         print("Invalid input. Try again.")
                         continue 
                     else:
                         break
                     # calculating cost
                 if no_of_credits == 0 or no_of_credits.isalpha() == True:
                     print("Invalid input. Try again.")
                 elif int(no_of_credits) <= 11 and int(no_of_credits) <=4 :
                     t_cost = int(no_of_credits)*494 + all_tax
                     #print(t_cost)
                     if int(no_of_credits) >= 6:
                         t_cost = t_cost + 5
                         print("Tuition is ${:,.2f}.".format(t_cost))
                     else:
                         print("Tuition is ${:,.2f}.".format(t_cost))
                 elif int(no_of_credits) <= 11 and int(no_of_credits) >4 :
                     t_cost = int(no_of_credits)*494 + all_tax
                     #print(t_cost)
                     if int(no_of_credits) >= 6:
                         t_cost = t_cost + 5
                         print("Tuition is ${:,.2f}.".format(t_cost))
                     else:
                         print("Tuition is ${:,.2f}.".format(t_cost))
                 elif int(no_of_credits) >11 and int(no_of_credits) <= 18:
                     t_cost = 7410 + all_tax
                     #print(t_cost)
                     if int(no_of_credits) >= 6:
                         t_cost = t_cost + 5
                         print("Tuition is ${:,.2f}.".format(t_cost))
                     else:
                         print("Tuition is ${:,.2f}.".format(t_cost))
                 elif int(no_of_credits) >18:
                     t_cost = 7410+(int(no_of_credits)-18)*494 + all_tax
                     if int(no_of_credits) >= 6:
                         t_cost = t_cost + 5
                         print("Tuition is ${:,.2f}.".format(t_cost))
                     else:
                         print("Tuition is ${:,.2f}.".format(t_cost))
                 program_continue = input("Do you want to do another calculation \
(yes/no): ").lower()
             
              
       # checking whether year of college is junior and senior          
    if year_college == "junior" or year_college == "senior":
        college = input("Enter college as business, engineering, health, \
sciences, or none: ")
        #checking to see if college is business
        if college == "business":
            
            while True:
                no_of_credits = input("Credits: ")
                if no_of_credits.isdigit() == False:
                    print("Invalid input. Try again.")
                    continue 
                elif int(no_of_credits) <= 0:
                    print("Invalid input. Try again.")
                    continue 
                else:
                    break
                #calculating cost
            if no_of_credits == 0 or no_of_credits.isalpha() == True:
                print("Invalid input. Try again.")
            elif int(no_of_credits) <= 11 and int(no_of_credits) <=4 :
                t_cost = int(no_of_credits)*573 + all_tax + 113
                #print(t_cost)
                if int(no_of_credits) >= 6:
                    t_cost = t_cost + 5
                    print("Tuition is ${:,.2f}.".format(t_cost))
                else:
                    print("Tuition is ${:,.2f}.".format(t_cost))
            elif int(no_of_credits) <= 11 and int(no_of_credits) >4 :
                t_cost = int(no_of_credits)*573 + all_tax + 226
                #print(t_cost)
                if int(no_of_credits) >= 6:
                    t_cost = t_cost + 5
                    print("Tuition is ${:,.2f}.".format(t_cost))
                else:
                    print("Tuition is ${:,.2f}.".format(t_cost))
            elif int(no_of_credits) >11 and int(no_of_credits) <= 18:
                t_cost = 8595 + all_tax + 226
                #print(t_cost)
                if int(no_of_credits) >= 6:
                    t_cost = t_cost + 5
                    print("Tuition is ${:,.2f}.".format(t_cost))
                else:
                    print("Tuition is ${:,.2f}.".format(t_cost))
            elif int(no_of_credits) >18:
                t_cost = 8595+(int(no_of_credits)-18)*573 + all_tax + 226
                if int(no_of_credits) >= 6:
                    t_cost = t_cost + 5
                    print("Tuition is ${:,.2f}.".format(t_cost))
                else:
                    print("Tuition is ${:,.2f}.".format(t_cost))
            program_continue = input("Do you want to do another calculation \
(yes/no): ").lower()
            

        # checking whether college is health or business
        if college == "health" or college == "science" :
            #print(type(no_of_credits))
            while True:
                no_of_credits = input("Credits: ")
                if no_of_credits.isdigit() == False:
                    print("Invalid input. Try again.")
                    continue 
                elif int(no_of_credits) <= 0:
                    print("Invalid input. Try again.")
                    continue 
                else:
                    break
                #calculating tuition
            if no_of_credits == 0 or no_of_credits.isalpha() == True:
                print("Invalid input. Try again.")
            elif int(no_of_credits) <= 11 and int(no_of_credits) <=4 :
                t_cost = int(no_of_credits)*555 + all_tax + 50
                #print(t_cost)
                if int(no_of_credits) >= 6:
                    t_cost = t_cost + 5
                    print("Tuition is ${:,.2f}.".format(t_cost))
                else:
                    print("Tuition is ${:,.2f}.".format(t_cost))
            elif int(no_of_credits) <= 11 and int(no_of_credits) >4 :
                t_cost = int(no_of_credits)*555 + all_tax + 100
                #print(t_cost)
                if int(no_of_credits) >= 6:
                    t_cost = t_cost + 5
                    print("Tuition is ${:,.2f}.".format(t_cost))
                else:
                    print("Tuition is ${:,.2f}.".format(t_cost))
            elif int(no_of_credits) >11 and int(no_of_credits) <= 18:
                t_cost = 8325 + all_tax + 100
                #print(t_cost)
                if int(no_of_credits) >= 6:
                    t_cost = t_cost + 5
                    print("Tuition is ${:,.2f}.".format(t_cost))
                else:
                    print("Tuition is ${:,.2f}.".format(t_cost))
            elif int(no_of_credits) >18:
                t_cost = 8325+(int(no_of_credits)-18)*555 + all_tax + 100
                if int(no_of_credits) >= 6:
                    t_cost = t_cost + 5
                    print("Tuition is ${:,.2f}.".format(t_cost))
                else:
                    print("Tuition is ${:,.2f}.".format(t_cost))
            program_continue = input("Do you want to do another calculation \
(yes/no): ").lower()    
            

        #checking whether college is engineering
        if college == "engineering":
            #print(type(no_of_credits))
            while True:
                no_of_credits = input("Credits: ")
                if no_of_credits.isdigit() == False:
                    print("Invalid input. Try again.")
                    continue 
                elif int(no_of_credits) <= 0:
                    print("Invalid input. Try again.")
                    continue 
                else:
                    break
                # calculating tuition
            if no_of_credits == 0 or no_of_credits.isalpha() == True:
                print("Invalid input. Try again.")
            elif int(no_of_credits) <= 11 and int(no_of_credits) <=4 :
                t_cost = int(no_of_credits)*573 + 402 + all_tax
                #print(t_cost)
                if int(no_of_credits) >= 6:
                    t_cost = t_cost + 5
                    print("Tuition is ${:,.2f}.".format(t_cost))
                else:
                    print("Tuition is ${:,.2f}.".format(t_cost))
            elif int(no_of_credits) <= 11 and int(no_of_credits) >4 :
                t_cost = int(no_of_credits)*573 + 670 + all_tax
                #print(t_cost)
                if int(no_of_credits) >= 6:
                    t_cost = t_cost + 5
                    print("Tuition is ${:,.2f}.".format(t_cost))
                else:
                    print("Tuition is ${:,.2f}.".format(t_cost))
            elif int(no_of_credits) >11 and int(no_of_credits) <= 18:
                t_cost = 8595 + 670 + all_tax
                #print(t_cost)
                if int(no_of_credits) >= 6:
                    t_cost = t_cost + 5
                    print("Tuition is ${:,.2f}.".format(t_cost))
                else:
                    print("Tuition is ${:,.2f}.".format(t_cost))
            elif int(no_of_credits) >18:
                t_cost = 8595+(int(no_of_credits)-18)*573 + 670 + all_tax
                #print(t_cost)
                if int(no_of_credits) >= 6:
                    t_cost = t_cost + 5
                    print("Tuition is ${:,.2f}.".format(t_cost))
                else:
                    print("Tuition is ${:,.2f}.".format(t_cost))
            program_continue = input("Do you want to do another calculation \
(yes/no): ").lower()

        # checking if not in any of these colleges, then whether in JMC or not
        if college != "health" and college != "engineering" and \
college != "science" and college != "business":
    
            col_jmc = input("Are you in the James Madison College (yes/no): ")
            if col_jmc == "yes":
                #print(type(no_of_credits))
                while True:
                    no_of_credits = input("Credits: ")
                    if no_of_credits.isdigit() == False:
                        print("Invalid input. Try again.")
                        continue 
                    elif int(no_of_credits) <= 0:
                        print("Invalid input. Try again.")
                        continue 
                    else:
                        break
                    #calculating tuition
                if int(no_of_credits) == 0 or no_of_credits.isalpha() == True:
                    print("Invalid input. Try again.")
                #no_of_credits = input("Credits: ")
                elif int(no_of_credits) <= 11 and int(no_of_credits) <=4 :
                    t_cost = int(no_of_credits)*555 + jmc_tax
                    #print(t_cost)
                    if int(no_of_credits) >= 6:
                        t_cost = t_cost + 5
                        print("Tuition is ${:,.2f}.".format(t_cost))
                    else:
                        print("Tuition is ${:,.2f}.".format(t_cost))
                elif int(no_of_credits) <= 11 and int(no_of_credits) >4 :
                    t_cost = int(no_of_credits)*555 + jmc_tax
                    #print(t_cost)
                    if int(no_of_credits) >= 6:
                        t_cost = t_cost + 5
                        print("Tuition is ${:,.2f}.".format(t_cost))
                    else:
                        print("Tuition is ${:,.2f}.".format(t_cost))
                elif int(no_of_credits) >11 and int(no_of_credits) <= 18:
                    t_cost = 8325 + jmc_tax
                    #print(t_cost)
                    if int(no_of_credits) >= 6:
                        t_cost = t_cost + 5
                        print("Tuition is ${:,.2f}.".format(t_cost))
                    else:
                        print("Tuition is ${:,.2f}.".format(t_cost))
                elif int(no_of_credits) >18:
                    t_cost = 8325+(int(no_of_credits)-18)*555 + jmc_tax
                    if int(no_of_credits) >= 6:
                        t_cost = t_cost + 5
                        print("Tuition is ${:,.2f}.".format(t_cost))
                    else:
                        print("Tuition is ${:,.2f}.".format(t_cost))
                program_continue = input("Do you want to do another calculation \
(yes/no): ").lower()
            #checking if in James Madison College or not
            if col_jmc == "no":
                #print(type(no_of_credits))
                while True:
                    no_of_credits = input("Credits: ")
                    if no_of_credits.isdigit() == False:
                        print("Invalid input. Try again.")
                        continue 
                    elif int(no_of_credits) <= 0:
                        print("Invalid input. Try again.")
                        continue 
                    else:
                        break
                    #calculating tuition
                if int(no_of_credits) == 0 or no_of_credits.isalpha() == True:
                    print("Invalid input. Try again.")
                elif int(no_of_credits) <= 11 and int(no_of_credits) <=4 :
                    t_cost = int(no_of_credits)*555 + all_tax  
                    #print(t_cost)
                    if int(no_of_credits) >= 6:
                        t_cost = t_cost + 5
                        print("Tuition is ${:,.2f}.".format(t_cost))
                    else:
                        print("Tuition is ${:,.2f}.".format(t_cost))
                elif int(no_of_credits) <= 11 and int(no_of_credits) >4 :
                    t_cost = int(no_of_credits)*555 + all_tax 
                    #print(t_cost)
                    if int(no_of_credits) >= 6:
                        t_cost = t_cost + 5
                        print("Tuition is ${:,.2f}.".format(t_cost))
                    else:
                        print("Tuition is ${:,.2f}.".format(t_cost))
                elif int(no_of_credits) >11 and int(no_of_credits) <= 18:
                    t_cost = 8325 + all_tax  
                    #print(t_cost)
                    if int(no_of_credits) >= 6:
                        t_cost = t_cost + 5
                        print("Tuition is ${:,.2f}.".format(t_cost))
                    else:
                        print("Tuition is ${:,.2f}.".format(t_cost))
                elif int(no_of_credits) >18:
                    t_cost = 8325+(int(no_of_credits)-18)*555 + all_tax 
                    if int(no_of_credits) >= 6:
                        t_cost = t_cost + 5
                        #print(t_cost)
                        print("Tuition is ${:,.2f}.".format(t_cost))
                    else:
                        print("Tuition is ${:,.2f}.".format(t_cost))
                program_continue = input("Do you want to do another calculation \
(yes/no): ").lower()

