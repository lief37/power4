from board import Board
from controller import Controller
from interface import Interface


class Game:
    def __init__(self):
        self.interface = Interface()
        self.controller = Controller()
        self.board = Board()
        self.toPlay = 1
        self.players = [1, 2]
        self.winner = 0

    def run(self):
        while self.winner == 0 :
            self.interface.showGrid(self.board.getGrid())
            self.runTurn()
            self.toPlay = 3 - self.toPlay
        
        self.interface.showGrid(self.board.getGrid())
        self.interface.print('player_won', {'winner': self.winner})
        

    def runTurn(self):
        self.interface.print('player_turn', {'toPlay': self.toPlay})
        
        input_played = self.interface.input('player_choose_column')

        # Input Validation
        played = self.controller.validateAndConvertInput(input_played)
        if not played:
            self.interface.print('wrong_input', None)
            self.runTurn()
        
        # Position validation
        error = self.controller.validatePlayedPosition(played, self.board.getGrid())
        if error:
            self.interface.print(error, None)
            self.runTurn()

        self.board.play(played, self.toPlay)

        self.winner = self.board.checkVictory(int(played))
            
        
        
