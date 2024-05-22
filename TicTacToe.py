import os

class TicTacToe:
    """
        A python program to emulate a cli-based version of
        the classical TicTacToe game.
        
        Bugs:
            ...
            
        Planned features:
        - Pick between PvP and PvE mode
        - PvE mode: play vs the environment
        - Scoreboard
    """
    def __init__(self, player_one="X", player_two="O"):
        # Class constructor
        self.player_one = player_one
        self.player_two = player_two
        self.user_choice = ""
        
        self.grid_dict = {
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
        }

    def clear_screen(self):
        # Clears the screen, supports nt and unix
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


    def display_grid(self):
        # Displays the current TicTacToe grid
        player_map = f"""
┌───┬───┬───┐
│ {self.grid_dict["1"]} │ {self.grid_dict["2"]} │ {self.grid_dict["3"]} │
│───┼───┼───│
│ {self.grid_dict["4"]} │ {self.grid_dict["5"]} │ {self.grid_dict["6"]} │
│───┼───┼───│
│ {self.grid_dict["7"]} │ {self.grid_dict["8"]} │ {self.grid_dict["9"]} │
└───┴───┴───┘
    """
        print(player_map)

    
    def current_game_status(self):
        # A tuple with all winning combinations
        winning_combinations = [
            ("1", "2", "3"),
            ("4", "5", "6"),
            ("7", "8", "9"),
            ("1", "4", "7"),
            ("2", "5", "8"),
            ("3", "6", "9"),
            ("1", "5", "9"),
            ("3", "5", "7"),
        ]
        
        # Check both X and O
        for symbol in ["X", "O"]:
            # Check each winning_combination
            for combination in winning_combinations:
                # if all the values are either X or O, a winning condition is met
                if all(self.grid_dict[pos] == symbol for pos in combination):
                    self.display_winner(winning_player=symbol)
                    return

    def display_scoreboard(self):
        """
            Create a /tmp json file to store the scoreboard in
        """
        pass
    
    def display_winner(self, winning_player):
        # Clear screen and display result
        if winning_player == "X":
            winning_player = self.player_one
        else:
            winning_player = self.player_two
            
        self.clear_screen()
        print(f"{winning_player} was victorious!")
        print("Well played.")
        print("Hit [Enter] to play again. Type [q] and hit enter to quit.")
        self.display_grid()

        # return grid_dict to original state
        self.grid_dict = {
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
        }

        self.user_choice = input("Your choice: ")
        self.clear_screen()
        print("Well, here we go again!\nGood luck and have fun.")
    
    def game_menu(self):
        tictactoe_ascii = r"""
Welcome to

 ______  ____   __        ______   ____    __        ______   ___     ___ 
|      ||    | /  ]      |      | /    |  /  ]      |      | /   \   /  _]
|      | |  | /  / _____ |      ||  X  | /  / _____ |      ||     | /  [_ 
|_|  |_| |  |/  / |     ||_|  |_||     |/  / |     ||_|  |_||  O  ||    _]
  |  |   |  /   \_|_____|  |  |  |  _  /   \_|_____|  |  |  |     ||   [_ 
  |  |   |  \     |        |  |  |  |  \     |        |  |  |     ||     |
  |__|  |____\____|        |__|  |__|__|\____|        |__|   \___/ |_____|
"""
        print(tictactoe_ascii)
        print("1. New Game")
        print("2. Player Selection")
        print("3. Exit")
        user_input = input("Enter menu selection (1-3): ")
        
        if user_input == "3" or user_input == "q":
            self.user_choice = "q"
        if user_input == "2":
            self.player_one = input("Player 1 (X) set name: ")
            self.player_two = input("Player 2 (O) set name: ")
        
    def start_game(self):
        self.clear_screen()
        self.game_menu()
        player_two_bad_choice = "local variable"
        while self.user_choice != "q":
            
            # Player 1 turn
            self.clear_screen()
            print("enter 'q' to quit")
            if player_two_bad_choice == "local variable":
                print(f"First round! Good look and have fun.")
            
            if player_two_bad_choice == 1:
                print("Number is already taken.")
            elif player_two_bad_choice == 0:
                print(f"{self.player_two} picked {self.user_choice}.")
                self.grid_dict[f"{self.user_choice}"] = "O"
                # Eval game status after player 2 turn
                self.current_game_status()
                if self.user_choice == "q":
                    self.clear_screen()
                    break
            
            print(f"{self.player_one}'s turn.")
            self.display_grid()
            
            self.user_choice = input("Place your X: ")
            if self.user_choice == "q":
                self.clear_screen()
                print("Game ended.")
                self.display_grid()
                break

            # Player 2 turn
            self.clear_screen()
            print("enter 'q' to quit")
            
            if self.grid_dict[f"{self.user_choice}"] == "X" or self.grid_dict[f"{self.user_choice}"] == "O":
                print("Number is already taken.")
            else:
                print(f"{self.player_one} picked {self.user_choice}.")
                self.grid_dict[f"{self.user_choice}"] = "X"

            # Eval game status after player 1 turn
            self.current_game_status()
            if self.user_choice == "q":
                break
            
            print(f"{self.player_two}'s turn.")
            self.display_grid()
            self.user_choice = input("Place your O: ")
            
            if self.user_choice == "q":
                self.clear_screen()
                print("Game ended.")
                self.display_grid()
                break
            
            if self.grid_dict[f"{self.user_choice}"] == "X" or self.grid_dict[f"{self.user_choice}"] == "O":
                player_two_bad_choice = 1
            else:
                player_two_bad_choice = 0

            self.display_grid()