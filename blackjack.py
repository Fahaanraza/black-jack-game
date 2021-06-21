import random
import os
print(""" _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/                 """)


def start():

    ace1 = [1, 11]
    ace = random.choice(ace1)
    card = [ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_set = random.sample(card, 2)
    print("Player's cards: ", player_set)
    comp_set = random.sample(card, 2)
    print("computers first card: ", comp_set[0])
    print("computers first card: ", comp_set)
    compare = [ace, 10]
    player_set.sort
    comp_set.sort
    compare.sort
    player_sum = 0
    comp_sum = 0
    player_sum = sum(player_set)
    comp_sum = sum(comp_set)

    if(comp_sum <= 16):
        comp_set.append(random.choice(card))
    choose = input("Enter Y to draw a card or N to stay back:  ")
    if(choose == "y"):
        player_set.append(random.choice(card))
    else:
        exit

    print("Player's final cards: ", player_set)
    print("computers final card: ", comp_set)

    player_sum = sum(player_set)
    comp_sum = sum(comp_set)

    if (player_set == compare):
        print("YOU Won by Blackjack")
    elif (comp_set == compare):
        print("COMP WON by Blackjack")
    elif((comp_sum > 21)):
        print("YOU WIN BRUH")
    elif((player_sum > 21)):
        print("YOU losss BRUH")
    elif((ace in player_set == 1) and (player_sum > 21)):
        print("you lose by passing over 21..")
    elif((comp_sum > player_sum)):
        print("YOU loss BRUH")
    elif((player_sum > comp_sum)):
        print("YOU WIN BRUH...")
    elif((player_sum == comp_sum)):
        print("Draw yaar")
    else:
        print("you lose by passing over 21")
    global flag
    flag = True


flag = True
while flag == True:
    Restart = input("Enter Y to play Game or N to Exit: ")
    if(Restart == "y"):
        os.system('cls')
        start()
    else:
        flag = False
