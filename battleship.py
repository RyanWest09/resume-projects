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

#prints the grid
  def print_grid(self):
    for rows in self.grid:
      print(rows)  
        
#changes a selected symbol
  def change_symbol(self,coord, hit):
    x,y = self.coord_mapping[coord]
    if hit:
      self.grid[x][y] = 'X'
    else:
      self.grid[x][y] = 'M'

#adds a boat to the grid
  def add_boat(self,list_coords):
    for coord in list_coords:
      x,y = self.coord_mapping[coord]
      self.grid[x][y] = 'B'
    self.print_grid()





class Boat:
  #dictionary containing all coords of all boats
  all_coords = {}
  def __init__(self,lives,name):
    self.name = name
    self.lives = lives
    string_coords = input("Please Input {} co-ordinates in the following fashion A1,A2,A3 or B1,C1,D1: ".format(lives))
    list_coords = string_coords.split(',')
    invalid = True
    if self.all_coords == {}:
      self.all_coords[name] = list_coords
      invalid = False
    else:
      while(invalid):
        invalid, list_coords = self.check_valid(list_coords)
        continue
    self.all_coords[name] = list_coords
    self.own_coords = list_coords

#determines if any boat coordinates will overlap
  def check_valid(self,list_coords):
    for coords in list_coords:
      for valid_coords in self.all_coords.values():
        if coords in valid_coords or len(list_coords) != self.lives:
          print("invalid coordinates try again")
          string_coords = input("Please Input {} co-ordinates in the following fashion A1,A2,A3 or B1,C1,D1: ".format(self.lives))
          list_coords = string_coords.split(',')
          return True, list_coords
        else:
          return False, list_coords
          
          
      
      
     
  
        




board = Board(10,10)
# board.print_grid()
patrol1 = Boat(2,"patrol1")
board.add_boat(patrol1.own_coords)
carrier1 = Boat(5,"Carrier")
board.add_boat(carrier1.own_coords)


print(carrier1.all_coords)


