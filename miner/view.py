from miner.cell import Cell
from miner.field import Field

class View:
    def __init__(self, field:Field):
        self.field = field

    def display_field(self):
        for row in self.field.data:
            for cell in row:
                if cell.is_open:
                    if cell.mine_count == Cell.MINE:
                        print('* ', end='')
                    else:
                        print(str(cell.mine_count), end=' ')
                else:
                    print('_ ', end='')


            print()

    def get_user_true(self):
        pass

