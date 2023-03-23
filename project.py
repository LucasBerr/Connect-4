"""
Welcome!!
    This is my first personal project and I decide to build a game called
Connet 4, where i used 100% python! I Hope you enjoy it!
CONTACT:
github: https://github.com/LucasBerr
email: lucastberr@gmail.com
Linkedin: https://www.linkedin.com/in/lucasberr/
"""


"""
Importing Librarys
"""
# pip install pyfiglet
from pyfiglet import figlet_format
# pip install tabulate
import tabulate
# pip install termcolor
from termcolor import colored
import sys
import time
from classes import Game

"""
Start Code the functions
"""

def main():
    startprogram()
    option = get_options()
    if option == "1":
        one_v_one()
    elif option == "2":
        battle_royale()
    elif option == "r":
        rules()

def battle_royale():
    Players = get_players()
    battle_royale = Game(players= Players)
    battle_royale.start_game()

def one_v_one():
    print("Loading one Vs one game")
    one_v_one = Game()
    one_v_one.start_game()

def get_players():
    while True:
        try:
            players = get_input(Type=int ,frase="Numbers of players: ")
            if(players <= 6 and players >= 2):
                return players
            else:
                print("Min players: 2 // Max players: 6")
        except ValueError:
            continue

def get_input(Type=int, frase="PRESS: "):
    return(Type(input(frase)))

def get_options():
    print("PRESS:")
    print(colored(figlet_format("1", font= "smkeyboard"), "green"))
    print("TO: 1 Vs 1")
    print(colored(figlet_format("2", font= "smkeyboard"), "green"))
    print("TO: BATTLE ROYAL!")
    print(colored(figlet_format("R", font= "smkeyboard"), "green"))
    print("TO: RULES")
    print(colored(figlet_format("Q", font= "smkeyboard"), "green"))
    print("TO: Quit program")
    return get_number(["1","2","q", "r"])

def startprogram():
    start = figlet_format("Welcome to Connect", font = "small" )
    print(divider(80, "green"))
    print(colored(start, "green"), end="")
    print(colored(figlet_format("                                   4", font="small"), "green"), end="")
    print(divider(80, "green"))

def divider(length, color):
    return (colored("=" * length, color))

def get_number(numbers, side="PRESS: "):
    while True:
        number = get_input(Type=str)
        for num in numbers:
            if number == num:
                Quit(number)
                return number
        if number == "r":
            return "r"
        else:
            print(error_messege(*numbers))

def Quit(input):
    if(input == "q"):
        print("Quiting")
        time.sleep(1)
        sys.exit()

def error_messege(*numbers):
    error_messege = "Please insert "
    for i in range(len(numbers)):
        error_messege = error_messege +"["+ numbers[i] +"] "
    return error_messege


"""
The only propous of the function rules is to display
the rules of the game to the user
"""
def rules():
    print(colored("+==================", "green"), end="")
    print("RULES",end="")
    print(colored("==================+", "green"))
    side = colored("|", "green")

    # Explaining how to play
    print(side + "HOW TO PLAY:" )
    # Explaining the 2 modes
    print(side +"\t1- Choose your game mode.")
    print(side +"\tThere is 2 game modes: ")
    print(side +colored("\t\tOne Vs One.", "magenta", "on_magenta"))
    print(side +colored("\t\tPRESS 1 ", "magenta"))
    print(side)
    print(side +colored("\t\tBattle Royal.", "magenta", "on_magenta"))
    print(side +colored("\t\tPRESS 2 ", "magenta"))
    number = get_number(["1", "2", "q"], side+"PRESS: ")

    if number == "2":
        # Explaining Battle royale
        print(side +colored("Battle Royal:", "magenta", "on_magenta"))
        print(side +"\t   This mode will ask you to enter")
        print(side +"\tthe amout of players that will be")
        print(side +"\tplaying, like this:")
        print(side +colored("Numbers of players: ", "green"))
        print(side +"\t   Then you will need to insert a")
        print(side +"\tvalue between 2 and 6(included)")
        print(side +"\tOnce you did this")
    else:
        # Explaining One Vs One
        print(side +colored("One Vs One:", "magenta", "on_magenta"))

    # Explaining the game map "grid"
    print(side +"\tThis grid will be displayed: ")
    grid = [[" " for row in range(7)] for colum in range(6)]
    print(tabulate.tabulate(grid, headers=[i + 1 for i in range(7)],  tablefmt="double_grid"))
    print(side +"\t   Then each player will need to")
    print(side +"\tselect a colum and the correspondin")
    print(side +"\tpiece will \"fall\"")
    print(side +"\tJust like this:")

    # Explaining how to select colum
    print(side +colored("PLAYER x", "yellow", "on_yellow"))
    print(side +colored("Witch colum? ", "green") + colored("5", "magenta"))
    grid[5][4] = colored(" x ", "yellow", "on_yellow")
    print(tabulate.tabulate(grid, headers=[i + 1 for i in range(7)],  tablefmt="double_grid"))
    print(side +colored("PLAYER y", "cyan", "on_cyan"))
    print(side +colored("Witch colum? ", "green") + colored("5", "magenta"))
    grid[4][4] = colored(" y ", "cyan", "on_cyan")
    print(tabulate.tabulate(grid, headers=[i + 1 for i in range(7)],  tablefmt="double_grid"))

    # Explaining ways to win

    print(side +"HOW TO WIN:")
    print(side +"\tThere are 3 ways of winning this")
    print(side +"\tgame.")


    # Explaining Line
    print(side +colored("Line:", "green"))
    grid = [[" " for row in range(7)] for colum in range(6)]
    for i in range(4):
        grid[2][1+i] = colored("   ", "green", "on_green")
    print(tabulate.tabulate(grid, headers=[i + 1 for i in range(7)],  tablefmt="double_grid"))
    print(side +"\tWhere your task is to line 4 of your")
    print(side +"\tpieces on a line.")

    # Explaining colum
    print(side +colored("Colum:", "green"))
    grid = [[" " for row in range(7)] for colum in range(6)]
    for i in range(4):
        grid[2+i][1] = colored("   ", "green", "on_green")
    print(tabulate.tabulate(grid, headers=[i + 1 for i in range(7)],  tablefmt="double_grid"))
    print(side +"\tWhere your task is to line 4 of your")
    print(side +"\tpieces on a colum.")

    # Explaining Diagonal
    print(side +colored("Diagonal:", "green"))
    grid = [[" " for row in range(7)] for colum in range(6)]
    for i in range(4):
        grid[5-i][1+i] = colored("   ", "green", "on_green")
    print(tabulate.tabulate(grid, headers=[i + 1 for i in range(7)],  tablefmt="double_grid"))
    print(side +"\tWhere your task is to line 4 of your")
    print(side +"\tpieces on a diagonal.")
    time.sleep(10)
    main()

if __name__ == "__main__":
    main()