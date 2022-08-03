def game_logic(user_score, dealer_score):
    if user_score > 21:
        return "Bust! Dealer wins!"
    elif user_score <= 21 and user_score == dealer_score:
        return "Draw!"
    elif user_score < 21 and user_score > dealer_score:
        return "User win!"
    elif user_score < 21 and dealer_score > 21:
        return "Bust! User win!"
    elif user_score < 21 and user_score < dealer_score:
        return "Dealer wins!"
