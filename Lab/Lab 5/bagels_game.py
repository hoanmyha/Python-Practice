'''
Name(s): My, Lomax
CSC 201
Lab 5

This program plays the game of "Bagels" where the user tries to guess a number.
After each guess the user is given clues:
    "fermi" for correct digit in the correct position
    "pico" for correct digit is the wrong position
    "bagels" when every digit is incorrect
When the user guesses the number, the user is asked whether they want to play again.

Did you complete this lab file during the class period (yes or no)? No

    I completed bagels_game.py without my partner from class.

    Document any assistance you get if you complete the lab after the class period:

'''
import random
NUM_DIGITS = 4    # number of digits in the number to be guessed

def intro():
    '''
    Introduces the game and explains the clues
    '''
    print('Welcome to Bagels!')
    print()
    print(f"I'm thinking of a {NUM_DIGITS} digit number. Each digit is between")
    print("1 and 9. Try to guess my number.")
    print()
    print("I'll say \"fermi\" for each correct digit in the correct position.")
    print("I'll say \"pico\" for each correct digit in the wrong position.")
    print("I'll say \"bagels\" if all of the digits are wrong.")
  
  
def get_clues(secret_string, guess_string):
    """
    Creates the clues for the user depending on how of the user's guess match
    the secret number to be guessed.
    
    Params:
    secret_string: The number to be guessed as a string
    guess_string: The number guessed by the user as a string
    
    Returns:
    a string of clues
    """
    # create lists to cleverly use to determine the clues
    secret_list = list(secret_string)
    guess_list = list(guess_string)
    clues = ''
    
    # check for any correct digits in the correct position
    for index in range(NUM_DIGITS):
        if guess_list[index] == secret_list[index]:
            clues = clues + 'fermi '
            guess_list[index] = 'X'
            secret_list[index] = 'Y'
    
    # check for any correct digits in the wrong position
    for index in range(NUM_DIGITS):
        for index2 in range(NUM_DIGITS):
            if secret_list[index] == guess_list[index2]:
                clues = clues + 'pico '
                secret_list[index] = 'Y'
                guess_list[index2] = 'X'
   
    # if clues is '' then there were no correct digits
    if clues == '':
        clues = 'bagels'
        
    return clues


def get_secret_number():
    '''
    Randomly generates the number the user will guess stored as a string
    Each digit must be 1-9 inclusive
    
    Returns:
    the secret number as a string of digits each digit 1-9
    '''
    number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    secret_number = []
    for count in range(4):
        number = random.choice(number_list)
        secret_number.append(number)
    secret_number = ''.join(secret_number)
    return secret_number

def is_guess_valid(guess):
    """
    Determines if the guess is valid. To be valid, it must have NUM_DIGITS characters,
    each character must be a digit, and none of the characters can be a '0'.
    
    Param:
    guess (str): the guess made by the user
    Returns:
    True if the guess is valid; False otherwise
    """
    if len(guess) == NUM_DIGITS and guess.isdigit() and '0' not in guess:
        return True
    else:
        return False


def get_user_guess():
    '''
    This function repeatedly asks the user to make a guess until the guess is valid.
    
    Returns:
    The valid guess entered by the user as a string
    '''
    user_guess = input('Your guess? ')
    while not is_guess_valid(user_guess):
        print('You must enter 4 digits with no zeros. Try again.')
        user_guess = input('Your guess? ')
    return user_guess


def play_one_round():
    """
    Plays one round from generating the number to be guessed until the user guesses the number.
    When the user guesses the number, the number of guesses it took is displayed.
    """
    num = 1
    secret = get_secret_number()
    print(f'Secret number is {secret}')
    guess = get_user_guess()
    
    while not guess == secret:
        clues = get_clues(secret, guess) #secret_string, guess_string
        print(clues)
        num = num + 1
        guess = get_user_guess()
        
    if num == 1:
        print(f'You got it in {num} guess.')
    else:
        print(f'You got it in {num} guesses.')
        
 
 
def play_again():
    """
    The function asks the user if they want to play again until
    the user answers 'y' or 'n', upper or lower case.
    
    Returns:
    the lowercase version of the user's y/n response lower case
    """
    response_list = ['y', 'n']
    response = input('Do you want to play again (y/n)? ')
    response = response.lower()
    while not response in response_list:
        print('You must answer y or n. Try again.')
        response = input('Do you want to play again (y/n)? ')
        response = response.lower()
    if response == 'y':
        return response
    if response == 'n':
        return response

def main():
    intro()  
    response = 'y'
    while response =='y':
        print()
        play_one_round()
        print()
        response = play_again()
main()     

    
    
    
    