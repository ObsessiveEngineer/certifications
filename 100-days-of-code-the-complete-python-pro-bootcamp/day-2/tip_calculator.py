################ Project: Tip Calculator ################

print("Welcome to the Tip Calculator!")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? (%10, %12 or %15) %")) / 100
split_count = int(input("How many people to split the bill? "))
bill_per_person = round(total_bill * (1 + tip_percentage) / split_count, 2)

print(f"Each person should pay ${bill_per_person}")