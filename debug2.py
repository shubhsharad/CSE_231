#################################
## CSE 231
## Debug exercise for Lab 2
## print() not allowed
## @amirootyet
#################################

go_again = 'y'

while go_again == 'y':
    
    algorithm = input("Enryption algorithm: ")
    
    if algorithm == 'AES':
        rating = 10
    elif algorithm == 'Caesar':
        rating = 2
    if algorithm == 'RSA':
        rating = 9
    else:
        rating = 'unknown'
        
    go_again = input('Go again? (y/n) ')
    
print('Exiting...')