# Tic Tac Toe
Hi this respository is a little contest. We want to make the best machine learning tic tac toe possible. To participate, please fork the branch and create you very own AI Player. It should follow this model:

````Python
class RandomPlayer:
    def __init__(self):
        self.name = "Random Player"
    def getMove(self, freeSpaces, game):
        return random.choice(freeSpaces)
````

Lets consider this game as an example:
````
x | x |  
  | o |  
  |   |  o
```

`getMove(self, freeSpaces, game)`

**Input:**
- `freeSpaces` is a list of the index of freespaces where your player is allowed to play. In the previous example it would be `[2, 3, 5, 6, 7]`.
- `game` is the board layout. A array of length 9. (example: `[1,1,0,-1,0,0,0,0,-1]`).  1 for player 1 and -1 for player 2.

**Return:**
- `Integer`: the function should return an element of the freeSpaces. If the return value is not in the array, the script will throw an exception.
