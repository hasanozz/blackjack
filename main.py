import art
import random
import os

should_continue = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_cards = []
dealer_cards = []

def get_card():
    my_value = sum(my_cards)
    dealer_value = sum(dealer_cards)
    print(f"\nYour hand {my_cards}, current score = {my_value}")
    print(f"Dealers hand [{dealer_cards[0]}, ?]\n")
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
        while dealer_value < 17:
            dealer_cards.append(random.choice(cards))
            dealer_value = sum(dealer_cards)

            if dealer_value > 21:
                if 11 in dealer_cards:
                    dealer_cards.pop(dealer_cards.index(11))
                    dealer_cards.append(1)
                    dealer_value = sum(dealer_cards)    

        if dealer_value > 21:    
            print_scores("DEALER BUSTS\nYOU WIN!")
            
        elif dealer_value == my_value:
            print_scores("PUSH!")

        elif dealer_value < my_value:    
            print_scores("YOU WIN!")

        elif dealer_value > my_value:    
            print_scores("DEALER WINS!")

def print_scores(status):
    my_value = sum(my_cards)
    dealer_value = sum(dealer_cards)
    print(f"Your hand {my_cards}. Your final score = {my_value}")
    print(f"Dealers hand {dealer_cards}. Dealers final score = {dealer_value}\n")
    print(status)

while should_continue:
    play = input("Type 'y' to play a game of Blackjack or type anything to pass: ").lower()

    if not play == 'y':
        break
    os.system('cls')
    print(art.logo)
    my_cards = random.sample(cards, 2)
    dealer_cards = random.sample(cards, 2)
    my_value = sum(my_cards)
    dealer_value = sum(dealer_cards)

    if my_value == 21 and dealer_value == 21:
        print_scores("You both have Blackjack\nPUSH!")

    elif my_value == 21:
        print_scores("You have Blackjack\nYOU WIN!")

    elif dealer_value == 21:
        print_scores("Dealer have Blackjack\nDEALER WINS!")

    else:
        get_card()