import random

# A class for the well known Morpion game!
class Morpion:
    def __init__(self):
        self.board = [0 for x in range(9)]
    def play(self, player, position):
        if self.isAValidMove(position):
            self.board[position] = player
        return self.checkWin()

    def isAValidMove(self, position):
        if self.board[position] == 0:
            return True
        else:
            raise Exception("Move not autorized")

    def getFreeSpaces(self):
        return [i for i, x in enumerate(self.board) if x == 0]

    def checkWin(self):
        # check line
        for j in [0, 3, 6]:
            res = sum([self.board[i+j] for i in range(3)])
            if abs(res) == 3:
                return res/3
        # check row
        for j in range(3):
            res = sum([self.board[i+j] for i in [0, 3, 6]])
            if abs(res) == 3:
                return res/3
        # check diag 1
        res = self.board[0] + self.board[4] + self.board[8]
        if abs(res) == 3:
            return res/3
        # check diag 2
        res = self.board[2] + self.board[4] + self.board[6]
        if abs(res) == 3:
            return res/3
        if len(self.getFreeSpaces())==0:
            return 0
        return -10

    def printGame(self):
        outString = "" 
        for i,x in enumerate(self.board):
            if x == 1:
                outString = outString + " x "
            elif x == -1:
                outString = outString + " o "
            elif x == 0:
                outString = outString + "   "
            if i%3 == 2:
                outString = outString + "\n"
            else:
                outString = outString + " | "
        print(outString)

class SimulateGame:
    def __init__(self, player1, player2):
        self.game = Morpion()
        self.player1 = player1
        self.player2 = player2
        self.player = 1
    def play(self):
        freeSpaces = self.game.getFreeSpaces()
        if self.player == 1:
            choice = self.player1.getMove(freeSpaces, self.game)
        else:
            choice = self.player2.getMove(freeSpaces, self.game)
        moveResult = self.game.play(self.player,choice)
        self.player = self.player * (-1)
        return moveResult
    def run(self):
        gameEnd = self.play()
        while gameEnd == -10:
            gameEnd = self.play()
        return gameEnd