from miner.cell import Cell
import random

class Field:
    def __init__(self, size=7):
        self.data = [[Cell() for i in range(size)] for i in range(size)]
        self.size = size
        self.generete_field()

    def generete_field(self):
        n_mine = round(((self.size * 2) / 100) * random.randint(1, 50))
        print(n_mine)
        for i in range(1, n_mine+1):
            x = 0
            y = 0
            while self.data[x][y].mine_count == Cell.MINE:
                x = random.randint(0, self.size-1)
                y = random.randint(0, self.size-1)
            self.data[x][y].mine_count = Cell.MINE

        for i in range(self.size):
            for j in range(self.size):
                self.calc_mine_cout(i, j)

    def calc_mine_cout(self, i, j):
        current_cell = self.data[i][j]
        count = 0
        if current_cell.mine_count !=Cell.MINE:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    x = i + dx
                    y = j + dy
                    if 0 <= x < self.size and \
                        0 <= y < self.size and \
                        self.data[x][y].mine_count == Cell.MINE:
                        count += 1
            current_cell.mine_count = count

    def get_value(self, x, y):
        pass

    def open_cell(self, x, y):
        if self.data[x][y].mine_count == Cell.MINE:
            return Cell.MINE
        if self.data[x][y].mine_count > 0:
            return self.data[x][y].mine_count
        self.walk(x, y)

    def walk(self, x, y):
        self.data[x][y].is_open = True
        if self.data[x][y].mine_count > 0:
            return

        if x - 1 >= 0:
            self.walk(x - 1, y)
            if y + 1 < self.size:
                self.walk(x-1, y+1)
            if y - 1 > 0:
                self.walk(x - 1, y - 1)
        if x + 1 < self.size:
            self.walk(x + 1, y)
            if y + 1 < self.size:
                self.walk(x + 1, y + 1)
            if y - 1 >= 0:
                self.walk(x + 1, y -1)
        if y + 1 > self.size:
            self.walk(x, y + 1)
        if y - 1 >= 0:
            self.walk(x, y - 1)







#f = Field()
#f.generete_field()
#print(f.data)