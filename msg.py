import datetime
from prettytable import PrettyTable

play_again = 'Play Again? Press "y" for YES or "n" for NO: '

def menu():
    m = ["Press '1' for Start Game ", "Press '2' for Score Board", "Press '3' for Exit Game   "]
    x = PrettyTable()
    x.field_names = ['The Hangman Game']
    print()
    for r in m:
        x.add_row([r])
    print(x)
    print()


def gameover(word):

    game = [f'The word was: {word}']
    x = PrettyTable()
    x.field_names = ['Game Over']
    x.add_row(game)
    print()
    print(x)
    print()


def won():
    game = ['You won']
    x = PrettyTable()
    x.field_names = ['Congrats']
    x.add_row(game)
    print()
    print(x)
    print()


def date():
    return datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')


if __name__ == '__main__':
    print(gameover('Cat'))
    print(play_again)
    menu()
    won()



