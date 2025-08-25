import json
from pathlib import Path
from ..data_structures import HashMap

LIB_PATH = Path(__file__).parent / "library.json" #conveniently pulls path to current file for adding new json file to folder

def load_library():
    hm = HashMap()
    if LIB_PATH.exists():
        with open(LIB_PATH, "r") as f: #opens file in read(r) mode
            data = json.load(f) #loads the file into data variable,
        for name, attrs in data.items(): #for each pair in the json. items is from python dictionary
            hm[name] = attrs #the name is the key and the attrs are the values
    return hm #returns the library

def save_library(hm):
    data = {k: v for k, v in hm.items()} #converts hashmap to a normal python dict b/c json doesnt understand my hashmap
    with open(LIB_PATH, "w") as f: #w for write mode
        json.dump(data, f, indent = 4)

def add_game():
    hm = load_library()
    name = input("Enter the game name: ").strip()#strip removes extra spaces
    while True:
        try:
            attention = int(input("What level of attention does this take? " \
            "1(Turn based/can pause), " \
            "2(Not devastating to walk away), " \
            "3(Full attention reqd): "))            
            if attention in [1, 2, 3]:
                break
            else:
                print("Please enter a 1, 2, or 3")
        except ValueError:
            print ("Invalid input, please enter a number (1, 2, or 3).")


    hm[name] = {"attention level": attention}
    save_library(hm)
    print(f"Game '{name}' added/updated!")

def view_library():
    #code here
    pass

def remove_duplicate():
#code here
    pass

if __name__ == "__main__":
    add_game()
