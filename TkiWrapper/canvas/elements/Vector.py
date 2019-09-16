from TkiWrapper.canvas.element import Element
from TkiWrapper.canvas.point import Point
import tkinter as tk
from math import sqrt, sin, cos, atan2, degrees, radians, pi as PI

class Vector(Element):
  def __init__(self, canvas, anchor, ptB):
    super().__init__(canvas)
    self.anchor = Point(*anchor)
    self.term = Point(*ptB)
    self.recalcPolar()
    self.initLines()

  def initLines(self):
    self.lines = [Line(self.cnv, (0, 0), (0, 0)) for i in range(3)]

  def recalcLines(self):
    ARR_ANGLE = conf.CANVAS.VECTOR_ARROW_ANGLE
    ARR_MAX = conf.CANVAS.VECTOR_ARROW_MAXLEN
    ARR_RATIO = conf.CANVAS.VECTOR_ARROW_RATIO
    mag = min(self.mag*ARR_RATIO, ARR_MAX)
    canvasPersState = self.cnv.PERSISTENT
    self.cnv.persistent(False)
    self.lines[0].moveTo(self.anchor, self.term)
    self.lines[1].moveToPolar(self.term, self.angle-PI+ARR_ANGLE, mag)
    self.lines[2].moveToPolar(self.term, self.angle-PI-ARR_ANGLE, mag)
    for line in self.lines:
      line.stroke = self.stroke
    self.cnv.persistent(canvasPersState)

  @classmethod
  def polar(cls, canvas, anchor, angle, magnitude):
    self = cls.__new__(cls)
    self.copyCanvasData(canvas)
    self.anchor = Point(*anchor)
    self.angle = angle
    self.mag = magnitude
    self.recalcTerm()
    self.copyCanvasData(canvas)
    self.initLines()
    return self

  def draw(self):
    self.recalcLines()
    for line in self.lines:
      line.draw()

  def recalcPolar(self):
    dx = self.anchor.x - self.term.x
    dy = self.anchor.y - self.term.y
    self.angle = (-atan2(dx, dy) - (PI/2)) % (PI*2)
    self.mag = sqrt(pow(dx, 2) + pow(dy, 2))

  def recalcTerm(self):
    dx = cos(self.angle) * self.mag
    dy = sin(self.angle) * self.mag
    self.term = Point(self.anchor.x + dx, self.anchor.y + dy)
