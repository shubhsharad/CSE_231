
import cards

# Create the deck of cards

my_deck = cards.Deck()
my_deck.shuffle()

player1_list=[]
player2_list=[]
for i in range( 5 ):
    player1_list.append( my_deck.deal() )
    player2_list.append( my_deck.deal() )
    
print("hand1:",player1_list)
print("hand2:",player2_list)


while True:
    player1_card = player1_list.pop( 0 )

    


    # First card dealt to Player #2

    player2_card = player2_list.pop( 0 )

    


    # Compare the ranks of the two cards

    print()
    if player1_card.rank() == player2_card.rank():
        print( f"Battle was 1: {player1_card}, 2: {player2_card}. Battle was a draw." )
        player1_list.append(player1_card)
        player2_list.append(player2_card)
    elif player1_card.rank() > player2_card.rank():
        print( f"Battle was 1: {player1_card}, 2: {player2_card}. Player 1 wins battle.")
        player1_list.append(player1_card)
        player1_list.append(player2_card)
    else:
        print( f"Battle was 1: {player1_card}, 2: {player2_card}. Player 2 wins battle.")
        player2_list.append(player1_card)
        player2_list.append(player2_card)
    print()
    print("hand1:",player1_list)
    print("hand2:",player2_list)
    
    

    if len(player1_list)==0:
        print("Player 2 wins!!!")
        break
    if len(player2_list)==0:
        print("Player 1 wins!!!")
        break
    
    x = input("Keep Going: (Nn) to stop:")
    if x == "n":
        if len(player1_list)> len(player2_list):
            print("Player 1 wins!!!")
        if len(player1_list)< len(player2_list):
            print("Player 2 wins!!!")
        if len(player1_list) ==  len(player2_list):
            print("Tie")
        break
