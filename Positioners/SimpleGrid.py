from TkiWrapper.Positioner import Positioner
from TkiWrapper.Point import Point

class SimpleGrid(Positioner):
  def __init__(self, frame):
    self.frame = frame
    self.slot = Point(0, 0)
    self.span = Point(1, 1)
    self.wrap = 1 # columns

  def setWrap(self, columns):
    self.wrap = columns

  def jumpTo(self, x, y):
    self.slot = Point(x, y)

  def setSpan(self, x=1, y=1):
    self.span = Point(x, y)

  def nextRow(self):
    self.slot = Point(0, self.slot.y + 1)

  def shift(self, amount):
    self.slot.x += amount
    self.normalizeSlot()

  def get(self, sticky=''):
    result = {
      'column': self.slot.x, 'row': self.slot.y,
      'columnspan': self.span.x, 'rowspan': self.span.y,
      'sticky': 'n'
    }
    if sticky:
      sticky = sticky.upper()
      if 'H' in sticky: result['sticky'] += 's'
      if 'R' in sticky: result['sticky'] += 'e'
      if 'L' in sticky: result['sticky'] += 'w'
    self.increment()
    return result

  def increment(self):
    self.slot.x += self.span.x
    self.span = Point(1, 1)
    self.normalizeSlot()

  def normalizeSlot(self):
    while self.slot.x >= self.wrap:
      self.slot.x -= self.wrap
      self.slot.y += 1
