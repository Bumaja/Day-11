import random

from art import cards

def comp_logic(user_points, dealer_deck):
    if user_points == 21:
        while dealer_deck < 21:
            dealer_deck.append(random.choice(cards))
        return dealer_deck
    elif user_points > 21:
        return dealer_deck.append(random.choice(cards))
    else:
        dealer_deck.append(random.choice(cards))
        if sum(dealer_deck) > 16:
            return dealer_deck
        elif sum(dealer_deck) <= 16:
            dealer_score = sum(dealer_deck)
            while sum(dealer_deck) <= 16 or dealer_score < user_points:
                dealer_deck.append(random.choice(cards))
            return dealer_deck