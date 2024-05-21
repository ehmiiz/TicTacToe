import os

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
        
        self.grid_dict = {
            "x1": "x1",
            "x2": "x2",
            "x3": "x3",
            "y1": "y1",
            "y2": "y2",
            "y3": "y3",
            "z1": "z1",
            "z2": "z2",
            "z3": "z3",
        }

    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')



    def display_grid(self):
        # The player map
        player_map = f"""
┌────┬────┬────┐
│ {self.grid_dict["x1"]} │ {self.grid_dict["x2"]} │ {self.grid_dict["x3"]} │
│────┼────┼────│
│ {self.grid_dict["y1"]} │ {self.grid_dict["y2"]} │ {self.grid_dict["y3"]} │
│────┼────┼────│
│ {self.grid_dict["z1"]} │ {self.grid_dict["z2"]} │ {self.grid_dict["z3"]} │
└────┴────┴────┘
    """
        print(player_map)

    
    def current_game_status(self):
        # Player one ruleset
        if self.grid_dict["x1"] == " X" and self.grid_dict["x2"] == " X" and self.grid_dict["x3"] == " X":
            self.display_winner(winning_player="X")

        if self.grid_dict["y1"] == " X" and self.grid_dict["y2"] == " X" and self.grid_dict["y3"] == " X":
            self.display_winner(winning_player="X")
        
        if self.grid_dict["z1"] == " X" and self.grid_dict["z2"] == " X" and self.grid_dict["z3"] == " X":
            self.display_winner(winning_player="X")
        
        if self.grid_dict["x1"] == " X" and self.grid_dict["y1"] == " X" and self.grid_dict["z1"] == " X":
            self.display_winner(winning_player="X")
        
        if self.grid_dict["x2"] == " X" and self.grid_dict["y2"] == " X" and self.grid_dict["z2"] == " X":
            self.display_winner(winning_player="X")
            
        if self.grid_dict["x3"] == " X" and self.grid_dict["y3"] == " X" and self.grid_dict["z3"] == " X":
            self.display_winner(winning_player="X")
        
        if self.grid_dict["x1"] == " X" and self.grid_dict["y2"] == " X" and self.grid_dict["z3"] == " X":
            self.display_winner(winning_player="X")
        
        if self.grid_dict["x3"] == " X" and self.grid_dict["y2"] == " X" and self.grid_dict["z1"] == " X":
            self.display_winner(winning_player="X")
        
        # Player two ruleset
        if self.grid_dict["x1"] == " O" and self.grid_dict["x2"] == " O" and self.grid_dict["x3"] == " O":
            self.display_winner(winning_player="O")

        if self.grid_dict["y1"] == " O" and self.grid_dict["y2"] == " O" and self.grid_dict["y3"] == " O":
            self.display_winner(winning_player="O")
        
        if self.grid_dict["z1"] == " O" and self.grid_dict["z2"] == " O" and self.grid_dict["z3"] == " O":
            self.display_winner(winning_player="O")
        
        if self.grid_dict["x1"] == " O" and self.grid_dict["y1"] == " O" and self.grid_dict["z1"] == " O":
            self.display_winner(winning_player="O")
        
        if self.grid_dict["x2"] == " O" and self.grid_dict["y2"] == " O" and self.grid_dict["z2"] == " O":
            self.display_winner(winning_player="O")
            
        if self.grid_dict["x3"] == " O" and self.grid_dict["y3"] == " O" and self.grid_dict["z3"] == " O":
            self.display_winner(winning_player="O")
        
        if self.grid_dict["x1"] == " O" and self.grid_dict["y2"] == " O" and self.grid_dict["z3"] == " O":
            self.display_winner(winning_player="O")
        
        if self.grid_dict["x3"] == " O" and self.grid_dict["y2"] == " O" and self.grid_dict["z1"] == " O":
            self.display_winner(winning_player="O")
    
    
    def display_winner(self, winning_player):
        # Clear screen and display result
        if winning_player == "X":
            winning_player = self.player_one
        else:
            winning_player = self.player_two
            
        self.clear_screen()
        print(f"{winning_player} was victorious!")
        print("Hit [Enter] to play again. Type [q] and hit enter to quit.")
        self.display_grid()

        # return grid_dict to original state
        self.grid_dict = {
            "x1": "x1",
            "x2": "x2",
            "x3": "x3",
            "y1": "y1",
            "y2": "y2",
            "y3": "y3",
            "z1": "z1",
            "z2": "z2",
            "z3": "z3",
        }

        user_prior_choice = self.user_choice
        self.user_choice = input("Your choice: ")
        
        if self.user_choice == user_prior_choice:
            print(self.user_choice)
        
        if self.user_choice != "q":
            pass

    def start_game(self):
        print("Welcome to TicTacToe!")
    
        while self.user_choice != "q":
            
            # Player 1 turn
            self.clear_screen()
            print(f"{self.player_one}'s turn.")
            print("enter 'q' to quit")
            
            self.display_grid()
            
            self.user_choice = input("Place your X: ")
            if self.user_choice == "q":
                self.clear_screen()
                print("Game ended.")
                self.display_grid()
                break
            
            self.grid_dict[f"{self.user_choice}"] = " X"
            
            # Eval game status after player 1 turn
            self.current_game_status()
            if self.user_choice == "q":
                break

            # Player 2 turn
            self.clear_screen()
            print(f"{self.player_two} turn.")
            print("enter 'q' to quit")
            self.display_grid()
            
            self.user_choice = input("Place your O: ")
            
            if self.user_choice == "q":
                self.clear_screen()
                print("Game ended.")
                self.display_grid()
                break

            self.grid_dict[f"{self.user_choice}"] = " O"
            self.display_grid()
            
            # Eval game status after player 2 turn
            self.current_game_status()
            if self.user_choice == "q":
                break

ask_player_one = input("Enter Name - Player One: ")
ask_player_two = input("Enter Name - Player Two: ")

game_of_tictactoe = TicTacToe(player_one=ask_player_one, player_two=ask_player_two)
game_of_tictactoe.start_game()