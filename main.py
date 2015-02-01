from morpion import SimulateGame
from defaultPlayers import HumanPlayer, RandomPlayer

def printResults(result):
    win = 1.0*sum([1 for x in result if x == 1])/len(result)
    tie = 1.0*sum([1 for x in result if x == -1])/len(result)
    lose = 1.0*sum([1 for x in result if x == 0])/len(result)
    print(str(win) + "/100 player1 wins")
    print(str(tie) + "/100 ties")
    print(str(lose) + "/100 player2 wins")


###################################
#                                 #
#   Main Class, running the Game  # 
#                                 #
###################################

player1 = RandomPlayer()
player2 = HumanPlayer()

result = []
for x in range(1000):
    morp = SimulateGame(player1, player2)
    gameResult = morp.run()
    result.append(gameResult)
    morp.game.printGame()            # comment if no human player
    print("---------------")     # comment if no human player

printResults(result)

