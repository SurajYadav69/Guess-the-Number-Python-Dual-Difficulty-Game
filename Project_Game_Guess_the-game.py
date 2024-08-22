print('''  ____     _   _ U _____ u ____    ____          _____    _   _  U _____ u      _   _       _   _   __  __     ____  U _____ u   ____     
U /"___|uU |"|u| |\| ___"|// __"| u/ __"| u      |_ " _|  |'| |'| \| ___"|/     | \ |"|   U |"|u| |U|' \/ '|uU | __")u\| ___"|/U |  _"\ u  
\| |  _ / \| |\| | |  _|" <\___ \/<\___ \/         | |   /| |_| |\ |  _|"      <|  \| |>   \| |\| |\| |\/| |/ \|  _ \/ |  _|"   \| |_) |/  
 | |_| |   | |_| | | |___  u___) | u___) |        /| |\  U|  _  |u | |___      U| |\  |u    | |_| | | |  | |   | |_) | | |___    |  _ <    
  \____|  <<\___/  |_____| |____/>>|____/>>      u |_|U   |_| |_|  |_____|      |_| \_|    <<\___/  |_|  |_|   |____/  |_____|   |_| \_\   
  _)(|_  (__) )(   <<   >>  )(  (__))(  (__)     _// \\_  //   \\  <<   >>      ||   \\,-.(__) )(  <<,-,,-.   _|| \\_  <<   >>   //   \\_  
 (__)__)     (__) (__) (__)(__)    (__)         (__) (__)(_") ("_)(__) (__)     (_")  (_/     (__)  (./  \.) (__) (__)(__) (__) (__)  (__) 
 
 ''')

print('''Game Rules:

The computer will randomly generate a number.
You will have a limited number of chances to guess the number based on the chosen difficulty level:
Easy Level: You will have 10 guesses.
Hard Level: You will have 5 guesses.
Good luck and have fun!
''')

EASY_LEVEL = 10
HARD_LEVEL = 5

# function to check the user's guess
def check_guess(answer, guess):
    if guess > answer: 
        print("Too High")
    elif guess < answer: 
        print("Too Low")
    else: 
        print(f"You Guessed Right! The Answer Is: {answer}")

# Set Difficulty
def set_diff():
    user = input("Please select 'easy' or 'hard' level of difficulty: ").lower()
    if user == 'easy':
        return EASY_LEVEL
    elif user == 'hard':
        return HARD_LEVEL
    else:
        print("Invalid input! Defaulting to easy level.")
        return EASY_LEVEL

import random

def game():
    no = range(1, 11)
    answer = random.choice(no)
    turns = set_diff()

    guess = -1
    while guess != answer and turns > 0:
        guess = int(input("Your Guess: "))
        check_guess(answer, guess)
        turns -= 1
        if guess != answer:
            print(f"You have {turns} guesses left.")

    if guess != answer:
        print(f"You've run out of guesses. The correct answer was {answer}.")


game()
