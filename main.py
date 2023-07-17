import art
import random
import os

should_continue = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_cards = []
computer_cards = []

def get_card():
    my_value = sum(my_cards)
    computer_value = sum(computer_cards)
    print(f"\nYour hand {my_cards}, current score = {my_value}")
    print(f"Dealers hand [{computer_cards[0]}, ?]\n")
    another_card = input("Type 'y' to Hit or type anything to Stand: ").lower()

    if another_card == 'y':
        my_cards.append(random.choice(cards))
        my_value = sum(my_cards)
        if my_value <= 21:
            get_card()
        elif my_value > 21:
            if 11 in my_cards:
               my_cards.pop(my_cards.index(11))
               my_cards.append(1)
               get_card()
            else:
                print_scores("BUST!\nDEALER WINS!")
    else:
        while computer_value < 17:
            computer_cards.append(random.choice(cards))
            computer_value = sum(computer_cards)

            if computer_value > 21:
                if 11 in computer_cards:
                    computer_cards.pop(computer_cards.index(11))
                    computer_cards.append(1)
                    computer_value = sum(computer_cards)    

        if computer_value > 21:    
            print_scores("DEALER BUSTS\nYOU WIN!")
            
        elif computer_value == my_value:
            print_scores("PUSH!")

        elif computer_value < my_value:    
            print_scores("YOU WIN!")

        elif computer_value > my_value:    
            print_scores("DEALER WINS!")

def print_scores(status):
    my_value = sum(my_cards)
    computer_value = sum(computer_cards)
    print(f"Your hand {my_cards}. Your final score = {my_value}")
    print(f"Dealers hand {computer_cards}. Dealers final score = {computer_value}\n")
    print(status)

while should_continue:
    play = input("Type 'y' to play a game of Blackjack or type anything to pass: ").lower()

    if not play == 'y':
        break
    os.system('cls')
    print(art.logo)
    my_cards = random.sample(cards, 2)
    computer_cards = random.sample(cards, 2)
    my_value = sum(my_cards)
    computer_value = sum(computer_cards)

    if my_value == 21 and computer_value == 21:
        print_scores("You both have Blackjack\nPUSH!")

    elif my_value == 21:
        print_scores("You have Blackjack\nYOU WIN!")

    elif computer_value == 21:
        print_scores("Computer have Blackjack\nDEALER WINS!")

    else:
        get_card()