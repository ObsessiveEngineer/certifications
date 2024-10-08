################ Project: Calculator ################
import os

title_art = """
_____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

            """

operations = {
    "+": lambda a, b : a + b,
    "-": lambda a, b : a - b,
    "*": lambda a, b  : a * b,
    "/": lambda a, b  : a / b,
}

choice = "n"
while True:
    os.system("clear")
    print(title_art)
    first = float(input("What's the first number?: ")) if choice == "n" else result
    operation = input(f"+\n-\n*\n/\nPick an operation: ")
    second = float(input("What's the second number?: "))
    result = operations[operation](first, second)
    choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
