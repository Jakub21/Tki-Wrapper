
class Point:
  '''2D Point class used to calculate canvas geometry'''
  def __init__(self, x, y):
    self.x, self.y = x, y

  def __repr__(self):
    return f'Point({round(self.x, 3)}, {round(self.y, 3)})'

  def get(self):
    return self.x, self.y

  # Modifiers

  def transpose(self, anchor, scale, reversed=False):
    '''Scale coordinates and add anchor'''
    if reversed:
      x = (self.x - anchor.x) / scale.x
      y = (self.y - anchor.y) / scale.y
    else:
      x = self.x * scale.x + anchor.x
      y = self.y * scale.y + anchor.y
    self.x, self.y = x, y

  def shift(self, other):
    self.x, self.y = self.x + other.x, self.y + other.y

  def mult(self, scalar):
    self.x *= scalar
    self.y *= scalar

  # Cloners

  def clone(self):
    return Point(self.x, self.y)

  def transposedClone(self, anchor, scale, reversed=False):
    c = self.clone()
    c.transpose(anchor, scale, reversed)
    return c

  def shiftedClone(self, other):
    c = self.clone()
    c.shift(other)
    return c
