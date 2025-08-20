import random
import json
from pathlib import Path

LIB_PATH = Path(__file__).parent / "library.json" #use path to path the terminal to the folder that this script is in, not working directory

with open(LIB_PATH, "r") as file:
    games = json.load(file)



def game_select(user_level):
    matching_games = []
    for game_name, attributes in games.items(): #attention level is a key, and int is the value. 
        if attributes["attention level"] == user_level:
            matching_games.append(game_name)
    if not matching_games:
        print("No games match that attention level.")
        return        
    selected_game = random.choice(matching_games)
    print(f"You should play {selected_game}.")
    if not matching_games:
        print("No games match that attention level.")
        return


if __name__ == "__main__":
    user_level = int(input("What attention level do you have right now? "))
    game_select(user_level)
