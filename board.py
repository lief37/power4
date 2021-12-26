import numpy as np

def checkVictoryOnLine(list):
    consec = 0
    player = 0
    for elem in list: 
        if (elem != player):
            player = elem
            consec = 1
        else:
            consec+=1
        if (consec >= 4):
            return player
    return 0

def getAllLinesInvolved(grid, positionPlayed):
    column = grid[:,positionPlayed]
    for idx in range(len(column)):
        if column[idx] == 0:
            return [column, grid[idx-1,:], getDiagAsc(grid, positionPlayed, idx-1), getDiagDesc(grid, positionPlayed, idx-1)]
    
def getDiagAsc(grid, x, y):
    min = np.min([x,y])
    max = np.max([x,y])

    diagAsc = []
    for i in range(-min, 7-max):
        diagAsc.append(grid[x+i,y+i])

    return diagAsc
    
def getDiagDesc(grid, x, y):
    min = np.min([x,6-y])
    max = np.max([x,6-y])

    diagDesc = []
    for i in range(-min, 7-max):
        diagDesc.append(grid[x+i,y-i])

    return diagDesc

class Board:
    def __init__(self):
        self.grid = np.zeros((7,7))

    def getGrid(self):
        return self.grid

    def play(self, positionToPlay, player):
        # Update Board
        column = self.grid[:,positionToPlay]
        for idx in range(len(column)):
            if column[idx] == 0:
                self.grid[idx, positionToPlay]= player
                break
        
    def checkVictory(self, positionPlayed):
        linesInvolved = getAllLinesInvolved(self.grid, positionPlayed)
        linesVictory = map(checkVictoryOnLine, linesInvolved)

        for elem in linesVictory:
            if elem != 0:
                return elem
        
        return 0
