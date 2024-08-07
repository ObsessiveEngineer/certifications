################ Project: Password Generator ################

import random

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
           "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
symbols = ["(",")","!", "#", "$", "%", "*", "+"]
numbers = [0,1,2,3,4,5,6,7,8,9]
pool = []

print("Welcome to the Password Generator!")
letter_count = int(input("How many letters would you like in your password?\n"))
symbol_count = int(input("How many symbols would you like?\n"))
number_count = int(input("How many numbers would you like?\n"))
password = ""

for i in range(letter_count):
    pool.append(random.choice(letters))
for i in range(symbol_count):
    pool.append(random.choice(symbols))
for i in range(number_count):
    pool.append(str(random.choice(numbers)))

random.shuffle(pool)
password = "".join(pool)
print(f"Your brand new password is: {password}")