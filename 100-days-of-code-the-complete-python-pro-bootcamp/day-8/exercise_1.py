################ Exercise 1: Life in Weeks ################

######## Task ########
# Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

######## Solution ########
def life_in_weeks(age):
    weeks_left = (90 - age) * 52
    msg = f"You have {weeks_left} weeks left."
    print(msg)