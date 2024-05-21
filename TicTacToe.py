import os

"""
    TODO:
    - Fix "hit enter or q to quit or rerun" logic
    - Encapsulate more in the loop
    - Convert construct functions into class methods
"""

class TicTacToe:
    """
        A python program to emulate a cli-based version of
        the classical TicTacToe game.
    """
    def __init__(self, player_one, player_two):
        # Class constructor
        self.player_one = player_one
        self.player_two = player_two
        self.user_choice = ""
        
        grid_dict = {
            "x1": "x1",
            "x2": "x2",
            "x3": "x3",
            "y1": "y1",
            "y2": "y2",
            "y3":"y3",
            "z1": "z1",
            "z2": "z2",
            "z3": "z3",
        }
        
        def clear_screen():
            os.system('clear')
            
        
        def display_grid(grid_dict):
            # The player map
            player_map = f"""
    ┌────┬────┬────┐
    │ {grid_dict["x1"]} │ {grid_dict["x2"]} │ {grid_dict["x3"]} │
    │────┼────┼────│
    │ {grid_dict["y1"]} │ {grid_dict["y2"]} │ {grid_dict["y3"]} │
    │────┼────┼────│
    │ {grid_dict["z1"]} │ {grid_dict["z2"]} │ {grid_dict["z3"]} │
    └────┴────┴────┘
        """
            
            print(player_map)
        
        def current_game_status(grid_dict, player_one="", player_two=""):
            # Player one ruleset
            if grid_dict["x1"] == " X" and grid_dict["x2"] == " X" and grid_dict["x3"] == " X":
                display_winner(grid_dict, player_one)

            if grid_dict["y1"] == " X" and grid_dict["y2"] == " X" and grid_dict["y3"] == " X":
                display_winner(grid_dict, player_one)
            
            if grid_dict["z1"] == " X" and grid_dict["z2"] == " X" and grid_dict["z3"] == " X":
                display_winner(grid_dict, player_one)
            
            if grid_dict["x1"] == " X" and grid_dict["y1"] == " X" and grid_dict["z1"] == " X":
                display_winner(grid_dict, player_one)
            
            if grid_dict["x2"] == " X" and grid_dict["y2"] == " X" and grid_dict["z2"] == " X":
                display_winner(grid_dict, player_one)
                
            if grid_dict["x3"] == " X" and grid_dict["y3"] == " X" and grid_dict["z3"] == " X":
                display_winner(grid_dict, player_one)
            
            if grid_dict["x1"] == " X" and grid_dict["y2"] == " X" and grid_dict["z3"] == " X":
                display_winner(grid_dict, player_one)
            
            if grid_dict["x3"] == " X" and grid_dict["y2"] == " X" and grid_dict["z1"] == " X":
                display_winner(grid_dict, player_one)
            
            # Player two ruleset
            if grid_dict["x1"] == " O" and grid_dict["x2"] == " O" and grid_dict["x3"] == " O":
                display_winner(grid_dict, player_two)

            if grid_dict["y1"] == " O" and grid_dict["y2"] == " O" and grid_dict["y3"] == " O":
                display_winner(grid_dict, player_two)
            
            if grid_dict["z1"] == " O" and grid_dict["z2"] == " O" and grid_dict["z3"] == " O":
                display_winner(grid_dict, player_two)
            
            if grid_dict["x1"] == " O" and grid_dict["y1"] == " O" and grid_dict["z1"] == " O":
                display_winner(grid_dict, player_two)
            
            if grid_dict["x2"] == " O" and grid_dict["y2"] == " O" and grid_dict["z2"] == " O":
                display_winner(grid_dict, player_two)
                
            if grid_dict["x3"] == " O" and grid_dict["y3"] == " O" and grid_dict["z3"] == " O":
                display_winner(grid_dict, player_two)
            
            if grid_dict["x1"] == " O" and grid_dict["y2"] == " O" and grid_dict["z3"] == " O":
                display_winner(grid_dict, player_two)
            
            if grid_dict["x3"] == " O" and grid_dict["y2"] == " O" and grid_dict["z1"] == " O":
                display_winner(grid_dict, player_two)
        
        def display_winner(grid_dict, player):
            # Clear screen and display result
            clear_screen()
            display_grid(grid_dict)
            
            # Call the user choice
            global user_choice
            
            # Congratulate
            print(f"{player.title()} was victorious!")

            
            user_choice = input("Hit [Enter] to play again. Hit [q] to quit")
            
            if user_choice != "q":
                clear_screen()
        
        print("Welcome to TicTacToe!")
        
        while self.user_choice != "q":
            
            # Player 1 turn
            clear_screen()
            print(f"{self.player_one} starts.")
            print("enter 'q' to quit")
            
            display_grid(grid_dict)
            
            if self.user_choice != "q":
                self.user_choice = input("Place your X: ")
            else:
                clear_screen()
                print("Game ended.")
                display_grid(grid_dict)
                
            grid_dict[f"{self.user_choice}"] = " X"
            
            # Eval game status after player 1 turn
            current_game_status(grid_dict, self.player_one)

            # Player 2 turn
            clear_screen()
            print(f"{self.player_two} turn.")
            print("enter 'q' to quit")
            display_grid(grid_dict)
            
            if self.user_choice != "q":
                self.user_choice = input("Place your O: ")
            else:
                clear_screen()
                print("Game ended.")
                display_grid(grid_dict)
            
            grid_dict[f"{self.user_choice}"] = " O"
            display_grid(grid_dict)
            
            # Eval game status after player 2 turn
            current_game_status(grid_dict, self.player_two)
        

ask_player_one = input("Enter Name - Player One: ")
ask_player_two = input("Enter Name - Player Two: ")

start_game = TicTacToe(player_one=ask_player_one, player_two=ask_player_two)