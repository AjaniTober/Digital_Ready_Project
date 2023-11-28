import time
import random
# from colorama 

random.choice(list[:])
currnet_input = input

def go():
     while True:
        currnet_input = input()
        if currnet_input == "quit" or "q":
             return

current_time = time.time
print("current time in seconds since the epoch:", current_time)
start_time = time.time()
time.sleep(2)
end_time = time.time()
elapsed_time = end_time - start_time

print("Now presenting, Ajani and Kevens card game: War")
print("Rules; Each player starts with 26 cards (Half of the deck), \nWhoever puts down the higher value card, takes both cards Whoever has the deck at the end of the game wins. \nIn this game Aces are considered 1")


random_num = random.randint(1,52)
print(random_num)
class Card: 
    def __init__(self, suit: str,  random_num: int) -> list:
            self.random_num = random_num 
            self.suit = suit
    def __repr__(self) -> str: 
        return self.suit +" " + self.random_num 
    


# i = 0
player1 = []
player2 = [] 
class Deck_Shuffle:
    def __init__(self) -> list:
          def shuffle():
               while player1.__len__ <=26:
                   pass
                  
                # make a loop that runs 26 times and randomly takes a card each time and appends it in a new list
                #  for player 1s acess, and deletes those cards from the old list, player 2 gets the old list 
 
if __name__ == "__main__":
    go()