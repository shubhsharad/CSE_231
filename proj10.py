###########################################################
    #   Project 10
    #   CARD GAME OF STREETS AND ALLEYS
    #   initialize() function
    #   display(tableau, foundation) function
    #   valid_tableau_to_tableau(tableau,s,d) function
    #   move_tableau_to_tableau(tableau,s,d) function
    #   valid_foundation_to_tableau(tableau,foundation,s,d) function
    #   move_foundation_to_tableau(tableau,foundation,s,d) function
    #   valid_tableau_to_foundation(tableau,foundation,s,d) function
    #   move_tableau_to_foundation(tableau, foundation, s,d) function
    #   check_for_win(foundation) function
    #   get_option() function
    #   main() function
    #           Intialze function is called
    #           display function is called
    #           print MENU to user
    #           check if user_input is U,R,H,Q or Mxx
    #           take appropriate action according to user_input
    #           check for win if move is played. 
    #           if user wins, restart game 
    #           user enters Q, quit game
    #       display end message
    #   end of program
###########################################################

#DO NOT DELETE THESE LINES
import cards, random
random.seed(100) #random number generator will always generate 
                 #the same 'random' number (needed to replicate tests)

MENU = '''     
Input options:
    MTT s d: Move card from Tableau pile s to Tableau pile d.
    MTF s d: Move card from Tableau pile s to Foundation d.
    MFT s d: Move card from Foundation s to Tableau pile d.
    U: Undo the last valid move.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game       
'''
CORRECTION_LIST1 = ["MTT","MTF","MFT"]
CORRECTION_LIST2 = ["U","R","H","Q"]

                
def initialize():
    '''
    That function has no parameters. It creates and initializes the tableau 
    and foundation, and then returns them as a tuple, in that order.
    All fifty-two cards are then dealt from the stock as 
    specified above into the tableau.
    parameters: None
    returns: a tuple with tableau and foundation lists
    displays: nothing
    '''
    # Initialize an empty lists of lists for tableau and foundation
    foundation = [[],[],[],[]]
    tableau = [[],[],[],[],[],[],[],[]]
    # commands to shuffle cards
    deck = cards.Deck()
    deck.shuffle()
    # for loop to access each list inside the main list.
    for i in range(0,len(tableau)):
        # to check if even or odd
        if i % 2 == 0:
            # for even indexed
            for j in range(0,7):
                # adding a card to each list
                tableau[i].append(deck.deal())
        else:
            # for odd indexed
            for j in range(0,6):
                # adding a card to each list
                tableau[i].append(deck.deal())
    # tuple with tableau and foundation
    t = (tableau,foundation)
    return t
       
    
def display(tableau, foundation):
    '''Each row of the display will have
       tableau - foundation - tableau
       Initially, even indexed tableaus have 7 cards; odds 6.
       The challenge is the get the left vertical bars
       to line up no matter the lengths of the even indexed piles.'''
    
    # To get the left bars to line up we need to
    # find the length of the longest even-indexed tableau list,
    #     i.e. those in the first, leftmost column
    # The "4*" accounts for a card plus 1 space having a width of 4
    max_tab = 4*max([len(lst) for i,lst in enumerate(tableau) if i%2==0])
    # display header
    print("{1:>{0}s} | {2} | {3}".format(max_tab+2,"Tableau","Foundation","Tableau"))
    # display tableau | foundation | tableau
    for i in range(4):
        left_lst = tableau[2*i] # even index
        right_lst = tableau[2*i + 1] # odd index
        # first build a string so we can format the even-index pile
        s = ''
        s += "{}: ".format(2*i)  # index
        for c in left_lst:  # cards in even-indexed pile
            s += "{} ".format(c)
        # display the even-indexed cards; the "+3" is for the index, colon and space
        # the "{1:<{0}s}" format allows us to incorporate the max_tab as the width
        # so the first vertical-bar lines up
        print("{1:<{0}s}".format(max_tab+3,s),end='')
        # next print the foundation
        # get foundation value or space if empty
        found = str(foundation[i][-1]) if foundation[i] else ' '
        print("|{:^12s}|".format(found),end="")
        # print the odd-indexed pile
        print("{:d}: ".format(2*i+1),end="") 
        for c in right_lst:
            print("{} ".format(c),end="") 
        print()  # end of line
    print()
    print("-"*80)
          
def valid_tableau_to_tableau(tableau,s,d):
    '''
    Checks whether move entered by user is valid to move the card from tableau
    to tableau. 
    parameters: Tableau, source, destination
    returns : Boolean values, True and False
    displays: nothing
    '''
    #check if there are cards in the source
    if len(tableau[s]) == 0:
        return False
    # check if there are cards in the destination
    if len(tableau[d]) == 0:
        return True
    # checking whether source and destination are within limits
    if s <= 7 and s >= 0 and d <= 7 and d >= 0:
        #commands to find out rank of the cards
        d_card = cards.Card.rank(tableau[d][-1])
        s_card = cards.Card.rank(tableau[s][-1])
        # checking whether difference of destination card and source card is 1
        if d_card - s_card == 1:
            # returns boolean statements
            return True
        else:
            return False
    else:
        return False
    
    
def move_tableau_to_tableau(tableau,s,d):
    '''
    performs the card move that was found valid in the valid_tableau_to_tableau
    function. 
    parameters: Tableau,source, destination
    returns: Boolean values, True and False
    displays: Nothing
    '''
    # calls valid_tableau_to_tableau function
    if valid_tableau_to_tableau(tableau,s,d):
        # pops the source card
        x = tableau[s].pop(-1)
        # appends the source card to the destination card list
        tableau[d].append(x)
        # returns boolean statements
        return True
    else:
        return False

def valid_foundation_to_tableau(tableau,foundation,s,d):
    '''
    Checks whether move entered by user is valid to move the card from 
    foundation to tableau. 
    parameters: Tableau, foundation , source, destination
    returns : Boolean values, True and False
    displays: nothing
    '''
    # check if there are cards in the destination
    if len(tableau[d]) == 0:
        return True
    # check if there are cards in the source
    if len(foundation[s]) == 0:
        return False
    # check whether source and destination are within limits
    if s <= 3 and s >= 0 and d <= 7 and d >= 0:
        d_card = cards.Card.rank(tableau[d][-1])
        s_card = cards.Card.rank(foundation[s][-1])
        # difference of destination - source 
        if d_card - s_card == 1:
            return True
        else:
            # return boolean statements
            return False
    else:
        return False
    

def move_foundation_to_tableau(tableau,foundation,s,d):
    '''
    performs the card move that was found valid in the 
    valid_foundation_to_tableau function. 
    parameters: Tableau,foundation,source, destination
    returns: Boolean values, True and False
    displays: Nothing
    '''
    # calls valid_foundation_to_tableau function to check
    if valid_foundation_to_tableau(tableau,foundation,s,d):
        # removes source card
        x = foundation[s].pop(-1)
        # appends it to the destination
        tableau[d].append(x)
        # returns boolean statements
        return True
    else:
        return False
        

def valid_tableau_to_foundation(tableau,foundation,s,d):
    '''
    Checks whether move entered by user is valid to move the card from tableau
    to foundation. 
    parameters: Tableau,foundation , source, destination
    returns : Boolean values, True and False
    displays: nothing
    '''
    # check if destination is empty and rank is of an ace
    if len(foundation[d]) == 0 and tableau[s][-1].rank() == 1:
        return True
    # check if destionation if emoty and rank is not an ance
    if len(foundation[d]) == 0 and tableau[s][-1].rank() != 1:
        return False
    # check if source is empty
    if len(tableau[s]) == 0:
        return False
    # check whether the source and destination are within limits.
    if s <= 7 and s >= 0 and d <= 3 and d >= 0:
        #functions to call rank of the cards
        d_card = cards.Card.rank(foundation[d][-1])
        s_card = cards.Card.rank(tableau[s][-1])
        # checking whether suit of the cards in source and destiination are same
        if cards.Card.suit(tableau[s][-1]) == cards.Card.suit(foundation[d][-1]) \
            and s_card - d_card == 1 :
            # returns boolean statements
            return True
        else:
            return False
    else:
        return False
    
            
def move_tableau_to_foundation(tableau, foundation, s,d):
    '''
    performs the card move that was found valid in the 
    valid_tableau_to_foundation function. 
    parameters: Tableau,foundation,source, destination
    returns: Boolean values, True and False
    displays: Nothing
    '''
    # calls valid_tableau_to_foundation function
    if valid_tableau_to_foundation(tableau,foundation,s,d):
        # removes card from source
        x = tableau[s].pop(-1)
        # appends source card to destination card
        foundation[d].append(x)
        # boolean statements
        return True
    else:
        return False

def check_for_win(foundation):
    '''
    checks to see if the user playing has won the game or not. 
    parameters: Foundation
    returns: Boolean values, True and False
    displays: Nothing
    '''
    # counter
    x = 0
    # for loop to go through each list in the foundation
    for i in range(0,len(foundation)):
        y = len(foundation[i])
        #incrementing the counter
        x = y + x
    # check if foundation had 52 cards
    if x == 52:
        # return boolean statements
        return True
    else:
        return False
        

def get_option():
    '''
    That function takes no parameters. It prompts the user for an option 
    and checks that the input supplied by the user is of the form 
    requested in the menu.
    parameters: No parameters
    returns: A list or None
    displays: Error messages and input checks
    '''
    # taking inout from the user
    user_input = input("\nInput an option (MTT,MTF,MFT,U,R,H,Q): ")
    upper_user_input = user_input.upper()
    # check if input is correct
    if upper_user_input[0:3] in CORRECTION_LIST1 \
        or upper_user_input in CORRECTION_LIST2 :
        #check if input is a single character
        if upper_user_input in CORRECTION_LIST2:
            # goes through correction_list2
            for i in CORRECTION_LIST2:
                if upper_user_input == i:
                    # returns list of a single character
                    return list(upper_user_input)
        # check if input is of the type Mxx 
        if upper_user_input[0:3] in CORRECTION_LIST1:
            # try to find move
            try:
                move = upper_user_input[0:3]
            
            except:
                # error message
                print("Error in option:",user_input)
                return None
            try:
                # try to find source 
                source = int(upper_user_input[4:5])
                
            except:
                # error message
                print("Error in option:",user_input)
                return None
            try:
                # try to find destination
                destination = int(upper_user_input[6:7])
                
            except:
                # error message
                print("Error in option:",user_input)
                return None
            # check to see if move is MTT
            if move == 'MTT':
                # check whether source and destination are within limits.
                if source <= 7 and source >=0 and \
                    destination <= 7 and destination >= 0:
                    temp_list = [move,source,destination]
                    # returns list as required
                    return temp_list
                else:
                    # error in input check
                    if source >= 7 or source <= 0:
                        # error message
                        print("Error in Source.")
                        return None
                    # error in input check
                    if destination >= 7 or destination <= 0:
                        #error message
                        print("Error in Destination")
                        return None
            # check to see if move is MTF
            if move == 'MTF':
                # check whether source and destination are within limits.
                if source <= 7 and source >=0 and \
                    destination <= 3 and destination >= 0:
                    temp_list = [move,source,destination]
                    # returns list as required
                    return temp_list
                else:
                    # error in input check
                    if source >= 7 or source <= 0:
                        # error message
                        print("Error in Source.")
                        return None
                    # error in input check
                    if destination >= 3 or destination <= 0:
                        # error message
                        print("Error in Destination")
                        return None
            # check to see if move is MTF
            if move == 'MFT':
                # check whether source and destination are within limits.
                if source <= 3 and source >=0 and \
                    destination <= 7 and destination >= 0:
                    temp_list = [move,source,destination]
                    # returns list as required
                    return temp_list
                else:
                    # error in input check
                    if source >= 3 or source <= 0:
                        # error message
                        print("Error in Source.")
                        return None
                    # error in input check
                    if destination >= 7 or destination <= 0:
                        # error message
                        print("Error in Destination")
                        return None        
    else:
        # error message
        print("Error in option:",user_input)
        return None
    
    

       
        
def main():  
    # welcome message
    print("\nWelcome to Streets and Alleys Solitaire.\n")
    # initialize function to start the game
    tableau, foundation = initialize()
    #display the board
    display(tableau,foundation)
    # display MENU to the user
    print(MENU)
    # create a temporary_list
    temp_list = []
    # while loop 
    while True:
        # get_option function
        x = get_option()
        # check if get_option is None
        if x == None:
            continue
        # if first element of the list is Q
        if x[0] == "Q":
            break
        # if first element of the list is R
        if x[0] == "R":
            tableau,foundation = initialize()
            display(tableau, foundation)
        # if first element of the list is H
        if x[0] == "H":
            print(MENU)
        # if first element of the list is MTT
        if x[0] =="MTT":
            # calls valid_tableau_to_tableau function
            if valid_tableau_to_tableau(tableau,x[1], x[2]):
                temp_list.append(x)
                # calls move_tableau_to_tableau function
                move_tableau_to_tableau(tableau,x[1],x[2])
                #display(tableau, foundation)
                # check for win function
                if check_for_win(foundation):
                    print("You won!\n")
                    #display(tableau, foundation)
                    # initialize again
                    tableau,foundation = initialize()
                    print("\n- - - - New Game. - - - -\n")
                    # display function
                    display(tableau, foundation)
                    print(MENU)
                else:
                    display(tableau, foundation)
            else:
                print("Error in move: {} , {} , {}".format(x[0],x[1],x[2]))
        if x[0] =="MTF":
            # calls valid_tableau_to_foundation()
            if valid_tableau_to_foundation(tableau,foundation,x[1], x[2]):
                temp_list.append(x)
                # calls move_tableau_to_tableau function
                move_tableau_to_foundation(tableau,foundation,x[1],x[2])
                #display(tableau, foundation)
                # check for win() function
                if check_for_win(foundation):
                    print("You won!\n")
                    display(tableau, foundation)
                    # initialize again
                    tableau,foundation = initialize()
                    print("\n- - - - New Game. - - - -\n")
                    # display function
                    display(tableau, foundation)
                    print(MENU)
                else:
                    display(tableau, foundation)
            else:
                print("Error in move: {} , {} , {}".format(x[0],x[1],x[2]))
        
        if x[0] =="MFT":
            # calls valid_foundation_to_tableau()
            if valid_foundation_to_tableau(tableau,foundation,x[1], x[2]):
                temp_list.append(x)
                # calls move_foundation_to_tableau function
                move_foundation_to_tableau(tableau,foundation,x[1],x[2])
                #display(tableau, foundation)
                # check for win function
                if check_for_win(foundation):
                    print("You won!\n")
                    display(tableau, foundation)
                    # intialize again 
                    tableau,foundation = initialize()
                    print("\n- - - - New Game. - - - -\n")
                    # display function
                    display(tableau, foundation)
                    print(MENU)
                else:
                    display(tableau, foundation)
            else:
                # error message
                print("Error in move: {} , {} , {}".format(x[0],x[1],x[2]))
                
        if x[0] == "U":
            #print(temp_list)
            # check if temp_list is empty
            if len(temp_list) == 0:
                print("No moves to undo.")
            else:
                # removes last move from temp_list
                i = temp_list.pop()
                # if input was MFT
                if i[0] == "MFT":
                    # poping card that was appended
                    x = tableau[i[2]].pop()
                    # appedning it to where it was popped from
                    foundation[i[1]].append(x)
                    # error message
                    print("Undo:",i[0],i[1],i[2])
                    display(tableau, foundation)
                elif i[0] == "MTF":
                    # poping card that was appended
                    x = foundation[i[2]].pop()
                    # appedning it to where it was popped from
                    tableau[i[1]].append(x)
                    # error message
                    print("Undo:",i[0],i[1],i[2])
                    display(tableau, foundation)
                elif i[0] == "MTT":
                    # poping card that was appended
                    x = tableau[i[2]].pop()
                    # appedning it to where it was popped from
                    tableau[i[1]].append(x)
                    # error message
                    print("Undo:",i[0],i[1],i[2])
                    display(tableau, foundation)
    # end message       
    print("Thank you for playing.")

if __name__ == '__main__':
     main()

