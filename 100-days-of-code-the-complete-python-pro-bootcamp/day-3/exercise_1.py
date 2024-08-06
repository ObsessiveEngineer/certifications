################ Exercise 1: BMI Calculator with Interpretations ################

######## Task ########
# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
# If the bmi is under 18.5 (not including), print out "underweight"
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
# If the bmi is 25 (including) or over, print out "overweight"

######## Solution ########
weight = 85
height = 1.85
bmi = weight / (height ** 2)
result = ""

if bmi < 18.5:
    result = "underweight"
elif bmi < 25:
    result = "normal weight"
else:
    result = "overweight"

print(result)