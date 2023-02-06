print("hello")

class Board:
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
  def __init__(self, height,width):
    self.width = width
    self.height = height
    #I Map all potential input co-ordinates into a dictionary of tuples contain
    self.coord_mapping = {}
    for letter in self.alphabet:
      for i in range(self.height): 
        self.coord_mapping[letter + str(i)] = (i+1,self.alphabet.index(letter) + 1)
    grid = []
    row1 = ["  "]
    for i in range(width):
      row1.append(self.alphabet[i])
    grid.append(row1)
    for i in range(height):
      temp_row = []
      if i < 10:
        temp_row.append("0" + str(i) + "")
      else:
        temp_row.append(str(i))
      for i in range(width):
        temp_row.append("0")
      grid.append(temp_row)
    self.grid = grid

  def get_width(self):
    print(self.width)

  def print_grid(self):
    for rows in self.grid:
      print(rows)  
    print(self.coord_mapping)
        
  def change_symbol(self,coord):
    x,y = self.coord_mapping[coord]
    self.grid[x][y] = 'X'



board = Board(10,10)
# board.print_grid()
board.change_symbol('F0')
board.print_grid()

