################ Project: Rock Paper Scissors ################
import random

choices = ["Rock", "Paper", "Scissors"]
result_msg = ""
draw = "It's a draw"
win = "You win"
lose = "You lose"

ascii_sprites = [
"""             
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)   
"""
]
player_choice = choices[int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))]
computer_choice = random.choices(choices)[0]


if player_choice == computer_choice:
    result_msg = draw
elif player_choice == "Rock":
    if computer_choice == "Scissors":
        result_msg = win
    else:
        result_msg = lose
elif player_choice == "Paper":
    if computer_choice == "Rock":
        result_msg = win
    else:
        result_msg = lose
elif player_choice == "Scissors":
    if computer_choice == "Paper":
        result_msg = win
    else:
        result_msg = lose


print(f"""{ascii_sprites[choices.index(player_choice)]}\n
          Computer chose:\n
          {ascii_sprites[choices.index(computer_choice)]}\n
          {result_msg}
""")


