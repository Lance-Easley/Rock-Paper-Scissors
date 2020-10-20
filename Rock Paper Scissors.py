import random
import time
from os import system, name

def clear():
    if name == 'nt': 
        _ = system('cls') 

#initiate score variables
player_score = 0
comp_score = 0

while 1 == 1:
    #randomly chooses rock, paper, or scissors for the computer
    comp = random.choice([1, 2, 3])
    #prompt the user to choose rock, paper, or scissors
    choice = input('Rock, Paper, Scissors\t\tPlayer:' + str(player_score) \
             +'\tComputer:' + str(comp_score) + '\n')
    #Makes the first letter lowercase and checks to see what the first letter is
    if choice[0].lower() == 'r':
        player = 1
    elif choice[0].lower() == 'p':
        player = 2
    elif choice[0].lower() == 's':
        player = 3
    elif choice[0].lower() == 'e':
        exit()
    #if the player chooses rock, determine the result for every computer choice
    if player == 1 and comp == 1:
        print('Rock')
    elif player == 1 and comp == 2:
        print('Paper')
        comp_score += 1
    elif player == 1 and comp == 3:
        print('Scissors')
        player_score += 1
    #if the player chooses paper, determine the result for every computer choice
    elif player == 2 and comp == 1:
        print('Rock')
        player_score += 1
    elif player == 2 and comp == 2:
        print('Paper')
    elif player == 2 and comp == 3:
        print('Scissors')
        comp_score += 1
    #if the player chooses scissors, determine the result for every computer choice
    elif player == 3 and comp == 1:
        print('Rock')
        comp_score += 1
    elif player == 3 and comp == 2:
        print('Paper')
        player_score += 1
    elif player == 3 and comp == 3:
        print('Scissors')
#wait 1.5 seconds, then clear the screen
    time.sleep(1)
    clear()
else:
    exit()