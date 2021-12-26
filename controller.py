class Controller:
    def validateAndConvertInput(self, input):
        try:
            val = int(input)
            return val
        except: 
            return None

    def validatePlayedPosition(self, played, grid):
        if played < 0 or played > 6:
            return 'wrong_input'

        if 0 not in grid[:,played]:
            return 'full_column'