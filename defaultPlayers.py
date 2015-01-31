import random

# A simple human input player. Will ask until the answer 
# is in the freespaces.
class HumanPlayer:
    def __init__(self):
        self.name = "Random Player"
    def getMove(self, freeSpaces, game):
        game.printGame()    
        print("\nWhere do you want to play: "+str(freeSpaces))
        input_var = -1
        while input_var not in freeSpaces:
        	input_var = input("Your move: ")
        return input_var

# Two Examples of stupid AI players. 
# The first one will randomly chose from the free spaces,
# while the other one selects the first empty space.
class RandomPlayer:
    def __init__(self):
        self.name = "Random Player"
    def getMove(self, freeSpaces, game):
        return random.choice(freeSpaces)

class StupidPlayer:
    def __init__(self):
        self.name = "Random Player"
    def getMove(self, freeSpaces, game):
        return freeSpaces[0]