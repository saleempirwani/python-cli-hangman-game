import random
from prettytable import from_csv
from msg import *


def hangman():
    words = []
    try:
        with open('animals.txt', 'r') as file:
            words = list(file.readlines())

        main_word = random.choice(words).strip().upper()

        word =  main_word
        guess = '_' * len(word)

        word = list(word)
        guess = list(guess)
        user_guess = []

        count = 1

        usr_letter = input('\nGuess Letter: ').upper()[0:1]

        cond = True

        while cond:

            if usr_letter in user_guess:
                usr_letter = ''
                print('Already Guess!')

                if count <= (len(word) + 4):
                    usr_letter = input('Guess Letter: ').upper()[0:1]
                    count += 1
                else:
                    gameover(main_word)
                    get_info('Lose', main_word)
                    cond = False
            else:
                print(''.join(guess))
                if usr_letter in word:
                    index = word.index(usr_letter)
                    guess[index] = usr_letter
                    word[index] = '_'
                else:
                    user_guess.append(usr_letter)
                    if count <= (len(word) + 4):
                        usr_letter = input('Guess Letter: ').upper()[0:1]
                        count += 1
                    else:
                        gameover(main_word)
                        get_info('Lose', main_word)
                        cond = False


            if '_' not in guess:
                print(''.join(guess))
                won()
                get_info('Won', main_word)
                cond = False


        if cond == False:

            usr_input = input(play_again).lower()[0:1]
            if usr_input == 'y':
                hangman()
            elif usr_input == 'n':
                main()


    except FileNotFoundError:
        print('Error: Animals Words File Not Found!')

username = ''

def main():

    while True:
        menu()
        usr_input = input('Enter your Choice: ')

        if '1' == usr_input:
            hangman()
            break
        elif '2' == usr_input:
            get_score()
        elif '3' == usr_input:
            print('\nExiting Hangman Game...')
            break
        else:
            print('Invalid command! Try again...')






def score(username, result, word):

    data = username.capitalize() +','+ word +','+ result +','+ date() +'\n'
    with open('results', 'a') as file:
        file.write(data)



def get_info(res, word):
    username = input('Enter username: ')
    score(username, res, word)



def get_score():

    print('\nScore Board\n***********', end='\n')
    with open('results.txt', 'r') as file:
        print(from_csv(file))


main()