################ Exercise 2: Love Calculator ################

######## Task ########
# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
# 2. Then check for the number of times the letters in the word LOVE occurs.   
# 3. Then combine these numbers to make a 2 digit number and print it out. 

######## Solution ########
def calculate_love_score(name1, name2):
    combined = (name1 + name2).upper()
    true_letters = ["T", "R", "U", "E"]
    love_letters = ["L", "O", "V", "E"]
    score = [0, 0]
    for letter in true_letters:
        for i in range(len(combined)):
            if letter == combined[i]:
                score[0] += 1
                
    for letter in love_letters:
        for i in range(len(combined)):
            if letter == combined[i]:
                score[1] += 1
    
    print(f"{score[0]}{score[1]}")