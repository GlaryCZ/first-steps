class Game():
    def __init__(self):
        self.turn = 'O'
        self.winner = None
        self.tiles = ["1", "2", "3",
                      "4", "5", "6",
                      "7", "8", "9"]

    def play(self):
        inp = input(f"Choose where to put {self.turn}\n>>")
        while inp not in {"1", "2", "3", "4", "5", "6", "7", "8", "9"} or self.tiles[int(inp)-1] in {"X", "O"}:
            print("Invalid input :( ")
            inp = input(f"Choose where to put {self.turn}\n>>")
        inp = int(inp)
        self.tiles[inp-1] = self.turn
        if self.turn == "O":
            self.turn = "X"
        else:
            self.turn = "O"

    def print_tiles(self):
        tiles = "\n"
        tiles += " S │ S │ S\n"
        tiles += " ──┼───┼──\n"
        tiles += " S │ S │ S\n"
        tiles += " ──┼───┼──\n"
        tiles += " S │ S │ S\n"
        i = 0
        for tile in self.tiles:
            tiles = tiles.replace("S", tile, 1)
        print(tiles)
        

    def check_win(self):
        if self.tiles[0] == self.tiles[1] and self.tiles[0] == self.tiles[2]: # rows
            self.winner = self.tiles[0]
        elif self.tiles[3] == self.tiles[4] and self.tiles[3] == self.tiles[5]:
            self.winner = self.tiles[3]
        elif self.tiles[6] == self.tiles[7] and self.tiles[6] == self.tiles[8]:
            self.winner = self.tiles[6]
        elif self.tiles[0] == self.tiles[3] and self.tiles[0] == self.tiles[6]: # columns
            self.winner = self.tiles[0]
        elif self.tiles[1] == self.tiles[4] and self.tiles[1] == self.tiles[7]:
            self.winner = self.tiles[1]
        elif self.tiles[2] == self.tiles[5] and self.tiles[2] == self.tiles[8]:
            self.winner = self.tiles[2]
        elif self.tiles[0] == self.tiles[4] and self.tiles[0] == self.tiles[8]: # diagonals
            self.winner = self.tiles[0]
        elif self.tiles[2] == self.tiles[4] and self.tiles[2] == self.tiles[6]:
            self.winner = self.tiles[2]

game = Game()
game.print_tiles()
while not game.winner:
    game.play()
    game.check_win()
    game.print_tiles()
print(f"Player {game.winner} won!")
