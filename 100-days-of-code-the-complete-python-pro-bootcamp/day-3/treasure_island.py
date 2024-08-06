################ Project: Treasure Island ################

greeting = "Welcome to Treasure Island!\nYour mission is to find the treasure."
print(greeting)

first_choice = input("You are at a cross road. Where do you want to go?\n(Type \"left\" or \"right\")\n")
if first_choice != "left":
    print("Oh no! A 20 feet king kobra bit you.\nGame over.")
    quit()

second_choice = input("You've come across a river. Would you like to swim to the other side or wait?\n(Type \"swim\" or \"wait\")\n")
if second_choice != "wait":
    print("Oh you fool! Did you not see the piranhas?\nGame over.")
    quit()

third_choice = input("""After an hour looking around and waiting, you have seen a three mysterious doors.\n
                     Which one woud you like to pick?\n
                     (Type \"red\", \"blue\" or \"yellow\")\n""")
if third_choice == "red":
    print("Oh no, you fool! Did you not feel the hot door handle? You're burned alive.\nGame over.")
elif third_choice == "blue":
    print("Oh really fool?! This time you didn't even notice the frostburn? You're freezed to death.\nGame over.")
elif third_choice == "yellow":
    print("You finally saw the shining gold.\nYou win!.")
else:
    print("Oh my fucking god! You can't even choose a door correctly, damn it!.\nGame over.")