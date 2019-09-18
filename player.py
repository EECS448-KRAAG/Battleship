##Player
from board import Board

class Player():
    def __init__(self, name, num_of_ships):
        self.name = name
        self.num_of_ships = num_of_ships
        self.lost = False
        self.total_ship_blocks = self.get_ship_blocks(num_of_ships)
        self.board = Board()


    def be_attacked(self):
        if self.total_ship_blocks > 0:
            self.total_ship_blocks-=1

    def has_lost(self):
        self.lost = True
        print(self.name + "has lost")

    def get_ship_blocks(self, num_of_ships):
        sum = 0
        for i in range(1, num_of_ships+1):
            sum+=i
        return sum