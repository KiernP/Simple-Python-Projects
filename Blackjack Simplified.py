import random

def draw_card():
    return random.randint(1,11)


def play_blackjack(num_cards):
    
    card_val = 0
    for i in range(1, num_cards + 1): 
        card = draw_card()
        print(f"Card {i}: {card}")
        card_val += card

    if card_val > 21:
        print("Busted!")

    else:
        print(f"Total card value: {card_val}")

    return card_val

rounds = int(input("How many rounds do you want to play?\n"))
overall_total = 0


while rounds > 0:
    rounds -= 1
    num_cards = int(input("How many cards do you want to draw?\n"))
    round_total = play_blackjack(num_cards)
    overall_total += round_total

    
print(f"Overall total cards value across rounds: {overall_total}")






