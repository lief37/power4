def playerTurnString(parameters):
    string = "It is time for player " + str(parameters['toPlay']) + " to play !"
    return string

def playerWonString(parameters):
    string = "Player " + str(parameters['winner']) + " won !"
    return string


STRINGS = {
    'player_turn': playerTurnString,
    'player_won': playerWonString,
    'wrong_input': 'Unvalid input',
    'full_column': 'This column is full'
}
INPUT_STRINGS= {
    'player_choose_column': 'Which column do you want to play ?'
}

class Interface:
    def print(self, key, params):
        if params:
            print(STRINGS[key](params))
        else:
            print(STRINGS[key])

    def input(self, key):
        return input(INPUT_STRINGS[key])

    def showGrid(self, grid):
        for row in range(len(grid)-1, -1, -1):
            for col in range (len(grid[row])):
                print("{:8.0f}".format(int(grid[row][col])), end = " ")
            print()