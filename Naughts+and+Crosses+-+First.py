
# coding: utf-8

# In[2]:


def game_start():
    
    global p1_name
    global p1_marker
    global p2_name
    global p2_marker
    global board 
    
    print ("Welcome!")
    print ()
    player_info(players,markers,p1_name,p1_marker,'1')
    p1_name = p_n
    p1_marker = p_m

    player_info(players,markers,p2_name,p2_marker,'2')
    p2_name = p_n
    p2_marker = p_m                

    print ("\nLet's Get Started! Take turns placing your Markers. The First to make a line of 3 wins!\n")

    print(p1_name+" your marker is '"+p1_marker+"'.")
    print(p2_name+" your marker is '"+p2_marker+"'.")
    
    print ()

    heads_tails = input(p1_name+", do you choose 'Heads' or 'Tails'?: ")
    while heads_tails != 'Heads' and heads_tails != 'Tails':
        print ("Sorry, please type 'Heads' or 'Tails':")
        heads_tails = input("'Heads' or 'Tails'? ")
    
    
    import random
    coinflip = random.choice(['Heads', 'Tails'])
    print("\nFlipping the coin... "+coinflip+"!")
    if coinflip == heads_tails:
        turn = 1
        print ("Congratz! "+p1_name+" goes first!")
    else:
        turn = 2
        print ("Sorry! "+p2_name+" goes first!")
    
    realturn = 0
    print ()
    # create the gameboard
    board = {'A':[0,0,0],'B':[0,0,0],'C':[0,0,0]}
    
    board_disp = ('Game! , 1 , 2 , 3 '),('A', board['A']),('B', board['B']),('C',board['C'])
    for row in board_disp:
        print (row)
    
    print()
    
    while realturn < 9 and wincheck(p1_marker) == 0 and wincheck(p2_marker) == 0:
        
        if turn % 2 == 0:
            turn += 1
            realturn += 1
            
            choose_coord(p2_name,p1_marker,p2_marker)
                    
            board[marker_place[0]][int (marker_place[1])-1] = p2_marker                    
            print ()
            for row in board_disp:
                print (row)
            print ()
            
            
        else:
            
            turn += 1
            realturn += 1
            
            choose_coord(p1_name,p1_marker,p2_marker)
                    
                
            board[marker_place[0]][int (marker_place[1])-1] = p1_marker                                
            print ()
            for row in board_disp:
                print (row)
            print ()

            
def wincheck(p_marker):
    if (p_marker == board['A'][0] == board['A'][1] == board['A'][2]):
        return 1
    elif (p_marker == board['B'][0] == board['B'][1] == board['B'][2]):
        return 1
    elif (p_marker == board['C'][0] == board['C'][1] == board['C'][2]):
        return 1
    elif (p_marker == board['A'][0] == board['B'][0] == board['C'][0]):
        return 1
    elif (p_marker == board['A'][1] == board['B'][1] == board['C'][1]):
        return 1
    elif (p_marker == board['A'][2] == board['B'][2] == board['C'][2]):
        return 1
    elif (p_marker == board['A'][0] == board['B'][1] == board['C'][2]):
        return 1
    elif (p_marker == board['A'][2] == board['B'][1] == board['C'][0]):
        return 1
    else:
        return 0

    
def fanfare(p_name):
            print("=================================================")
            print("Congratulations "+p_name+", you are the Winner!!!")
            print("=================================================")


def choose_coord(p_n,p1_m,p2_m):
    global marker_place
    while True:
        try:
            marker_place = input(p_n+", place your marker on the grid!: ")
            marker_place = marker_place.upper() 
            while board[marker_place[0]][int (marker_place[1])-1] in (p1_m,p2_m):
                print ("Choose an empty position from A1 to C3.")
                marker_place = input("Position: ")
            board[marker_place[0]][int (marker_place[1])-1] = p2_m  
                
        except (KeyError,IndexError):
            print("\nYou must choose an empty spot in the range A1 to C3!")
            continue
                
        else:
            break

def player_info(players,markers,n,m,v):
    
    global p_n
    global p_m
    
    n = input("\nPlayer "+v+", please enter your name: ")
    while n in players:
        n = input("\nPlayer "+v+", please choose a unique name: ")
    players.append(n)
    
    m = input(n+", please choose a single-letter marker: ")
    while len(m) > 1 or m.isnumeric() or m in markers:
        print (n+", '"+m+"' is too long, a number, or not unique.")
        m = input(n+". Please choose again: ")
    markers.append(m)
    
    p_n = n
    p_m = m
    

            
# Functions above this line
            
players = []
markers = []
p1_name = []
p1_marker = []
p2_name = []
p2_marker = []
p_n = []
p_m = []
board = {}    

game_start()

if wincheck(p1_marker) == 1:

        fanfare(p1_name)

elif wincheck(p2_marker) == 1:

        fanfare(p2_name)

else:
        print ("\nGame Over! This One Was A Draw!")



go_again = input("\nWould you like to play again? Yes or No: ")
go_again = go_again.lower()
while go_again not in ('yes','no'):
    go_again = input("Play again? 'Yes' or 'No': ")
    
if go_again == "yes":
    game_start()

else:
    print ("\nThanks for playing! Bye :)")

