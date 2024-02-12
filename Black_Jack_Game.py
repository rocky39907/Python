############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import BlackJack_Ascii_Logo
import random
print(BlackJack_Ascii_Logo.logo)

def get_new_card():
    """Return a random card from the Deck when called"""
    card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(card)

def compare(sys_deck, user_deck):
    """Takes 2 set of cards and compare their total to find out possible Blackjack, else return False"""
    if sum(sys_deck) == 21 or sum(user_deck) == 21:
        if sum(sys_deck) == sum(user_deck):
            print("\n!BLACKJACK ! You WIN!")
            print(f"Your Deck: {user_deck}")
            print(f"Dealer Deck: {sys_deck}")
        elif sum(sys_deck) == 21:
            print("\n!BLACKJACK ! Dealer WIN!")
            print(f"Your Deck: {user_deck}")
            print(f"Dealer Deck: {sys_deck}")
        else:
            print("\n!BLACKJACK ! You WIN!")
            print(f"Your Deck: {user_deck}")
            print(f"Dealer Deck: {sys_deck}")
        return True
    elif sum(sys_deck) > sum(user_deck) and sum(sys_deck) > 21:
        print("\n!! You WIN BUT NO BLACKJACK !!")
        print(f"Your Deck: {user_deck}")
        print(f"Dealer Deck: {sys_deck}")
        return True
    elif sum(user_deck) > sum(sys_deck) and sum(user_deck) > 21:
        print("\n!! Dealer WIN but no blackjack !!")
        print(f"Your Deck: {user_deck}")
        print(f"Dealer Deck: {sys_deck}")
        return True
    else:
        return False

is_game_over = False
sys_deck = []
user_deck = []

# Assign 2 initial cards to both system and user
for _ in range(2):
    sys_deck.append(get_new_card())
    user_deck.append(get_new_card())

# This block compares initial User and System picked card to check if there is a Blackjack
if sum(sys_deck) == 21 or sum(user_deck) == 21:
    is_game_over = True
    if sum(sys_deck) == sum(user_deck):
        print("\n!BLACKJACK ! You WIN!")
    elif sum(sys_deck) == 21:
        print("\n!BLACKJACK ! Dealer WIN!")
    else:
        print("\n!BLACKJACK ! You WIN!")

while not is_game_over:
    print(f"Cards in your Deck: {user_deck} and total score: {sum(user_deck)}")
    print(f"First Card in Dealer's Deck: {sys_deck[0]} and total score: {sum(sys_deck)}")
    user_option = input("You want to pick a new card? 'y' for yes and 'n' to pass.\n")
    if user_option.lower() == 'y':
        user_deck.append(get_new_card())
        if sum(user_deck) > 21 and 11 in user_deck:
            user_deck.remove(11)
            user_deck.append(1)
    sys_deck.append(get_new_card())
    is_game_over = compare(sys_deck, user_deck)
