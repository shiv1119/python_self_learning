#get clues
import random


def get_guess():
    return list(input("What is your guess-"))

#generate computer code
def generate_code():
    digits = [str(num) for num in range(10)]
    
    #shuffle the digit
    random.shuffle(digits)
    # grab the first three
    return digits[:3]

#generate the clues


def generate_clue(code,user_guess):
    if user_guess == code:
        return "Code Cracked!"
    
    clues = []
    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("Matched")
        elif num in code:
            clues.append("You are pretty close")
    if clues == []:
        return ["NOPE, nAHI hO rAHA kYA!"]
    else:
        return clues
            


#run the game logic
print("Welcome to code breaker!")
secret_code = generate_code()
clue_report = []

while clue_report != "Code Cracked!":
    guess = get_guess()
    clue_report = generate_clue(guess,secret_code)
    print("Here is the result of your guess:-")
    for clue in clue_report:
        print(clue)