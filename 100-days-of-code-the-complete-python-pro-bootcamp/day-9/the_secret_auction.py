################ Project: The Secret Auction ################
import os

ascii_art = """
                         ___________
                                  /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
"""

bitting = True
bitters = {}
winner = ""
max_bid = 0

while bitting:
    os.system("clear")
    print(ascii_art)
    name = input("What's your name?: ")
    bid = int(input("What's your name?: $"))
    bitters[name] = bid
    bitting = True if input("Are there any other bidders? Type 'yes or 'no'.\n") == "yes" else False


for key in bitters:
    if bitters[key] >= max_bid:
        max_bid = bitters[key]
        winner = key

print(f"Winner is {winner} with a bid of ${max_bid}")