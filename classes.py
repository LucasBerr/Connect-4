"""
Import Librarys
"""
import tabulate
from termcolor import colored
from pyfiglet import figlet_format

import sys

"""
Start code the Game Class, where will happen all the game
"""

class Game:
    def __init__(self, players=2):
        # Setting the widht and heigh of the grid game
        self.players = players
        self._width = 7
        self._height = 6
        # Setting grid
        self.grid = [[" " for row in range(self._width)] for colum in range(self._height)]

    def load_game(self):
        print(tabulate.tabulate(self.grid, headers=[i + 1 for i in range(self._width)],  tablefmt="double_grid"))

    def start_game(self):
        # Creating a list of players. max number of players = 6
        players = self.create_players()
        players = list(players)
        self.load_game()

        # Asking where do the player want to put his peace
        p=0
        while True:
            if(p == self.players):
                p = 0
            while True:
                print(colored("PLAYER "+ str(players[p]["number"]), players[p]["color"]))
                # Validate input
                place = self.get_input(range(self._width))
                self.Quitting(place)
                place = int(place)
                if place in range(self._width):
                    # Put peace in the correct colum in grid
                    height = self._height -1
                    try:
                        while(self.grid[height][int(place)] != " "):
                            height = height - 1
                    except IndexError:
                        print("There is no more space in this colum")
                        break
                    self.grid[height][int(place)] = colored(str(players[p]["number"]), players[p]["color"], players[p]["background"])
                    self.load_game()
                    self.check_winner(players[p])
                    # Another player
                    p = p + 1
                    break
                else:
                    self.error_messege(range(self._width))
                    continue

    # Checking if there is a Winner

    def check_winner(self, player):
        streek = 0
        check_player = colored(str(player["number"]), player["color"], player["background"])

        # Checking for colum
        for i in range(self._width):
            for y in range(self._height):
                if(self.grid[y][i] == check_player):
                    streek = streek + 1
                else:
                    streek = 0
                if(streek == 4):
                    print(colored(figlet_format("WINNER IS PLAYER " + str(player["number"]) , font = "small"), player["color"], player["background"]))
                    sys.exit()

        # Checking for row
        for i in range(self._height):
            for y in range(self._width):
                if(self.grid[i][y] == check_player):
                    streek = streek + 1
                else:
                    streek = 0
                if(streek == 4):
                    print(colored(figlet_format("WINNER IS PLAYER " + str(player["number"]) , font = "small"), player["color"], player["background"]))
                    sys.exit()

        # Checking for diagonal

        # Check diagonal lines starting from the bottom-left corner
        for i in range(self._height - 3):
            for j in range(self._width - 3):
                if (self.grid[i][j] == check_player and
                    self.grid[i+1][j+1] == check_player and
                    self.grid[i+2][j+2] == check_player and
                    self.grid[i+3][j+3] == check_player):
                    print(colored(figlet_format("WINNER IS PLAYER " + str(player["number"]) , font = "small"), player["color"], player["background"]))
                    sys.exit()

        # Check diagonal lines starting from the top-left corner
        for i in range(3, self._height):
            for j in range(self._width - 3):
                if (self.grid[i][j] == check_player and
                    self.grid[i-1][j+1] == check_player and
                    self.grid[i-2][j+2] == check_player and
                    self.grid[i-3][j+3] == check_player):
                    print(colored(figlet_format("WINNER IS PLAYER " + str(player["number"]) , font = "small"), player["color"], player["background"]))
                    sys.exit()

    # Creating players
    def create_players(self):
        players = [
            {"number": " 1 ", "color": "red", "background": "on_red"},
            {"number": " 2 ", "color": "blue", "background": "on_blue"},
            {"number": " 3 ", "color": "green", "background": "on_green"},
            {"number": " 4 ", "color": "yellow", "background": "on_yellow"},
            {"number": " 5 ", "color": "cyan", "background": "on_cyan"},
            {"number": " 6 ", "color": "magenta", "background": "on_magenta"},
        ]
        for i in range(self.players):
            yield players[i]


    #Checking the input
    def get_input(self, valid):
        while True:
            try:
                Input = input("Wich colum? ")
                if(Input == "q"):
                    self.Quitting(Input)
                Input = int(Input) - 1
                if int(Input) in valid:
                    return Input
                else:
                    self.error_messege(*valid)
            except ValueError:
                self.error_messege(*valid)
                continue

    # Quitting game
    def Quitting(self, input):
        if input == "q":
            print("Quitting")
            sys.exit()

    # Displays the error messege
    def error_messege(self, *numbers):
        error_messege = "Please insert "
        for i in range(len(numbers)):
            error_messege = error_messege +"["+ str(numbers[i]+1) +"] "
        print(error_messege + "([q] for quitting)")