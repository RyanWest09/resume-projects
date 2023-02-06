print("hello")

class Board:
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
  def __init__(self, height,width):
    self.width = width
    self.height = height
    #I Map all potential input co-ordinates into a dictionary of tuples containing x,y coords
    self.coord_mapping = {}
    #this portion builds the grid
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

  def print_grid(self):
    for rows in self.grid:
      print(rows)  
        
  def change_symbol(self,coord, hit):
    x,y = self.coord_mapping[coord]
    if hit:
      self.grid[x][y] = 'X'
    else:
      self.grid[x][y] = 'M'

  def add_boat(self,boat_coords):
    for coords in boat_coords:
       self.change_symbol(coords,True)




class Boats:
  def __init__(self):
    self.all_boats = []

  def create_patrol(self):
    coords = input("Please input 2 Coordinates in the form 'A1,A2,A3,etc' : ")
    coord_list = coords.split(',')
    self.all_boats.append(coord_list)
    print(coord_list)
    return coord_list

  def create_carrier(self):
    coords = input("Please input 5 Coordinates in the form 'A1,A2,A3,etc' : ")
    coord_list = coords.split(',')
    self.all_boats.append(coord_list)
    print(coord_list)
    return coord_list




board = Board(10,10)
# board.print_grid()
player1_boats = Boats()
board.add_boat(player1_boats.create_patrol())
board.add_boat(player1_boats.create_carrier())



board.change_symbol('F0',False)
board.change_symbol('F1',True)
board.print_grid()

