class Rectangle:
  def __init__(self, width = 0, height = 0) :
    self.geometry = 'Rectangle'
    self.width  = width
    self.height = height

  def set_width(self, width) : self.width = width
  def set_height(self,height) : self.height = height
  def get_area(self) : return (self.width) * (self.height)
  def get_perimeter(self) : return (2*self.width) + (2*self.height)
  def get_diagonal(self) : return ((self.width ** 2) + (self.height ** 2)) ** .5

  def get_picture(self) :
    calc = True; picture = ''
    if self.width > 50 or self.height > 50 : calc = False
    else :
      w = self.width; h = self.height
      for i in range(h) : picture += ''.join(['*' for j in range(w)]); picture += '\n'
    return picture if calc == True else "Too big for picture."

  def get_amount_inside(self, geo) : return int(self.get_area() / geo.get_area())

  def __repr__(self): return self.geometry
  def __str__(self): return f'{repr(self)}(width={self.width}, height={self.height})'
    
class Square(Rectangle):
  def __init__(self, side = 0) :
    self.geometry = 'Square'
    self.side     = int(side)
    self.set_super()

  def set_side(self, side = 0) :
    self.side = int(side)
    self.set_super()

  def set_super(self) :
    self.set_width(self.side)
    self.set_height(self.side)
    super().set_width(self.side)
    super().set_height(self.side)
    
  def __str__(self): return f'{repr(self)}(side={self.side})'
  
  