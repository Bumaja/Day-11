 ############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os

from gamelogic import game_logic
from art import logo, cards
from addCard import hit
from computerlogic import comp_logic

clear = lambda: os.system("clear")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = random.choices(cards, k=2)
user_score = sum(user_cards)

dealer_cards = random.choices(cards, k=1)
dealer_score = sum(dealer_cards)

flag = True
while flag:
    print(logo)
    print(f"Your cards: {user_cards}, points: {sum(user_cards)}.")
    print(f"Dealer cards: {dealer_cards}, points: {sum(dealer_cards)}")

    dobrac = input ("Do you want next card? Type 'y' or 'n': ")
    if dobrac == 'n':
        comp_logic(user_score, dealer_cards)
        print(f"Your cards: {user_cards}, points: {sum(user_cards)}.")
        print(f"Dealer cards: {dealer_cards}, points: {sum(dealer_cards)}")
        print(game_logic(user_score, dealer_score))
    elif dobrac == 'y':
        while dobrac == 'y':
            hit(user_cards)
            print(f"Your cards: {user_cards}, points: {sum(user_cards)}.")
            if sum(user_cards) > 21:
                dealer_cards.append(random.choice(cards))
                print(f"Dealer cards: {dealer_cards}, points: {sum(dealer_cards)}")
                print(game_logic(sum(user_cards), sum(dealer_cards)))
                break
            print(f"Dealer cards: {dealer_cards}, points: {sum(dealer_cards)}")
            dobrac = input ("Do you want next card? Type 'y' or 'n': ")  
        user_score = sum(user_cards)
        dealer_score = sum(dealer_cards)
        comp_logic(user_score, dealer_cards)
        print(f"Your cards: {user_cards}, points: {user_score}.")
        print(f"Dealer cards: {dealer_cards}, points: {dealer_score}")
        print(game_logic(user_score, dealer_score))
    else:
        print("Type 'y' or 'n'.")
    flag = False
    