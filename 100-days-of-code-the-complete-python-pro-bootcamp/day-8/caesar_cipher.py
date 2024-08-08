################ Project: Caesar Cipher ################

def caesar(method, word, shift_count):
    if method == "decrypt":
        shift_count = 0 - shift_count
    ciphered = ""
    for letter in word:
        ciphered += chr(ord(letter) + shift_count)
    return ciphered

quit = False

print("""
    ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
    a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
    8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
    "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
    '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
                88             88                                 
            ""             88                                 
                            88                                 
    ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
    8b         88 88       d8 88       88 8PP""""""" 88          
    "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
    '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
                88                                             
                88        
""")

while not quit:
    method = input("Type 'en' to encrypt, type 'de' to decrypt:\n").lower()
    message = input("Type your message\n")
    shift_count = int(input("Type the shift number\n"))
    result = caesar(f"{method}crypt", message, shift_count)
    print(f"Here is the {method}crypted result: {result}")
    quit = True if input("Type 'yes' if you want to go again. Otherwise type 'no'.\n") == "no" else False
