from miner.field import Field
from miner.view import View


class Controller:
    def __init__(self):
        self.field = Field()
        self.view = View(self.field)

    def start_game(self):
        self.field.open_cell(1, 1)
        self.view.display_field()

c = Controller()
c.start_game()







