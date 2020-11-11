
class Point:
  def __init__(self, x='auto', y=0, spanX=1, spanY=1):
    self.isAuto = x == 'auto'
    if not self.isAuto:
      self.x = x
      self.y = y
      self.spanX = spanX
      self.spanY = spanY

  def get(self):
    return self.x, self.y

  def dist(self, other):
    return Point(self.x-other.x, self.y-other.y)

  def toInts(self):
    self.x = int(self.x)
    self.y = int(self.y)
