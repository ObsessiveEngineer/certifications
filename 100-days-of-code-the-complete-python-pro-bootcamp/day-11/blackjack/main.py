################ Project: Blackjack ################

import os
import blackjack as bk

title_art ="""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
      |  \/ K|                            _/ |                
      '------'                           |__/    
"""

def game_over(value, hand, dealer_hand):
    print(f"\nYour final hand: {hand}, final score: {sum(hand)}")
    print(f"Computer's final hand: {dealer_hand}, final score: {sum(dealer_hand)}")
    print(f"IT'S A DRAW" if value == "draw" else f"YOU {value.upper()}!")

def who_wins(hand, dealer_hand):
    if sum(hand) > sum(dealer_hand):
        return 1
    elif sum(hand) < sum(dealer_hand):
        return -1
    else:
        return 0


end = False
while not end:
    if input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "n":
        end = True
    else:
        draw = True
        deck = bk.create_deck(bk.base)
        hand = []
        hand.append(bk.draw_card(deck))
        dealer_hand = []
        dealer_hand.append(bk.draw_card(deck))
        dealer_hand.append(bk.draw_card(deck))

        while draw:
            hand.append(bk.draw_card(deck))
            if sum(bk.hand(hand)) > 21:
                game_over("lose", bk.hand(hand), bk.hand(dealer_hand))
                break
            elif sum(bk.hand(hand)) == 21:
                game_over("win", bk.hand(hand), bk.hand(dealer_hand))
                break
            os.system("clear")
            print(title_art)
            print(f"Your cards: {bk.hand(hand)}, current score: {sum(bk.hand(hand))} {len(deck)}")
            print(f"Computer's first card: {bk.hand(dealer_hand)[0]}")
            draw = True if input("\nType 'y' to get another card, type 'n' to pass:") == "y" else False
            if not draw:
                while sum(bk.hand(dealer_hand)) < 17:
                    dealer_hand.append(bk.draw_card(deck))
                if sum(bk.hand(dealer_hand)) > 21:
                    game_over("win", bk.hand(hand), bk.hand(dealer_hand))
                    break
                if who_wins(bk.hand(hand), bk.hand(dealer_hand)) == 1:
                    game_over("win", bk.hand(hand), bk.hand(dealer_hand))
                elif who_wins(bk.hand(hand), bk.hand(dealer_hand)) == -1:
                    game_over("lose", bk.hand(hand), bk.hand(dealer_hand))
                else:
                    game_over("draw", bk.hand(hand), bk.hand(dealer_hand))