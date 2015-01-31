
class SimulateGame:
    def __init__(self, player1, player2):
        self.game = Morpion()
        self.player1 = player1
        self.player2 = player2
        self.player = 1
    def play(self):
        freeSpaces = self.game.getFreeSpaces()
        if self.player == 1:
            choice = self.player1.getMove(freeSpaces, self.game.board)
        else:
            choice = self.player2.getMove(freeSpaces, self.game.board)
        moveResult = self.game.play(self.player,choice)
        self.player = self.player * (-1)
        return moveResult
    def run(self):
        gameEnd = self.play()
        while gameEnd == -10:
            gameEnd = self.play()
        return gameEnd

class RandomPlayer:
    def __init__(self):
        self.name = "Random Player"
    def getMove(self, freeSpaces, board):
        return random.choice(freeSpaces)

class StupidPlayer:
    def __init__(self):
        self.name = "Random Player"
    def getMove(self, freeSpaces, board):
        return freeSpaces[0]

player1 = RandomPlayer()
player2 = StupidPlayer()

result = []
for x in range(1000):
    morp = SimulateGame(player1, player2)
    gameResult = morp.run()
    result.append(gameResult)

win = 100.0*sum([1 for x in result if x == 1])/len(result)
tie = 100.0*sum([1 for x in result if x == -1])/len(result)
lose = 100.0*sum([1 for x in result if x == 0])/len(result)

print(str(win) + "/100 player1 wins")
print(str(tie) + "/100 ties")
print(str(lose) + "/100 player2 wins")
