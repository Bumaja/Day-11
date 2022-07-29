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
from os import system
from art import logo

def hit(user_set_cards, score):
    card = random.choice(cards)
    user_set_cards.append(card)
    user_score = sum(user_set_cards)
    return user_score
    

def game_logic(user_score, comp_score):
    # Logika gry.
    if user_score > 21:
        return "Bust! Dealer wins!"
    elif comp_score > 21:
        return "Bust! You win!"
    elif user_score == comp_score:
        return "Draw!"
    elif user_score > comp_score:
        return "You win!"    
    else: 
        return "You lose!"

def comp_logic(set_of_cards, user_score, computer_score):
    if user_score > 21:
        return set_of_cards
    elif user_score == 21:
        return hit(set_of_cards, computer_score)

def add_card (list_of_cards, available_cards):
    return list_of_cards.append(random.randint(available_cards))

def game_starter():
    user_cards = random.choices(cards, k=2)
    user_score = sum(user_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    
    comp_cards = random.choices(cards, k=1)
    comp_score = sum(comp_cards)
    print(f"Computer cards: {comp_cards}, current score: {comp_score}")

clear = lambda: system("clear")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = None
user_score = None
comp_score = None
comp_cards = None


starter = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
print(logo)

user_hit = 'y'


while starter == 'y':
    user_cards = random.choices(cards, k=2)
    user_score = sum(user_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")

    comp_cards = random.choices(cards, k=1)
    comp_score = sum(comp_cards)
    print(f"Computer cards: {comp_cards}, current score: {comp_score}")
    
    user_hit = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_hit == 'y':
        while user_hit == 'y':
            user_score = hit(user_cards, user_score)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer cards: {comp_cards}, current score: {comp_score}")
            print(game_logic(user_score, comp_score))
            user_hit = input("Type 'y' to get another card, type 'n' to pass: ")
            # if user_hit == 'n' or user_score > 21:
            #     print(game_logic(user_score, comp_score))
            #     clear()
    else:
        print(game_logic(user_score, comp_score))
    
        clear()
    
    