import random
from art import cards

def hit(lista_kart):
    # Dodanie jednej karty do decku gracza/dealera
    return lista_kart.append(random.choice(cards))
    
    