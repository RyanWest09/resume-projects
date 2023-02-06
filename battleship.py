print("hello")

class Board:
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
  def __init__(self, height,width):
    self.width = width
    self.height = height
    grid = []
    row1 = [" "]
    for i in range(width):
      row1.append(self.alphabet[i])
    grid.append(row1)
    for i in range(height):
      temp_row = []
      temp_row.append(i)
      for i in range(width):
        temp_row.append("O")
      grid.append(temp_row)
    self.grid = grid

  def get_width(self):
    print(self.width)

  def print_grid(self):
    for rows in self.grid:
      print(rows)
      

board = Board(12,12)
board.print_grid()

