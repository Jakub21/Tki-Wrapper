from TkiWrapper.canvas.element import Element
from TkiWrapper.canvas.point import Point
import tkinter as tk
from math import sqrt, sin, cos

class Line(Element):
  def __init__(self, canvas, ptA, ptB):
    super().__init__(canvas)
    self.ptA = Point(*ptA)
    self.ptB = Point(*ptB)

  @classmethod
  def polar(cls, canvas, ptA, angle, mag):
    self = cls.__new__(cls)
    self.copyCanvasData(canvas)
    self.moveToPolar(Point(*ptA), angle, mag)
    return self

  def moveTo(self, ptA, ptB):
    self.ptA = ptA.clone()
    self.ptB = ptB.clone()

  def moveToPolar(self, ptA, angle, mag):
    self.ptA = ptA.clone()
    self.ptB = Point(cos(angle), sin(angle))
    self.ptB.mult(mag)
    self.ptB.shift(self.ptA)

  def draw(self):
    ptA = self.trp(self.ptA)
    ptB = self.trp(self.ptB)
    self.cnv.canvas.create_line([*ptA.get(), *ptB.get()], fill=self.stroke.get(),
      width=self.strokeWidth)
