from TkiWrapper.canvas.element import Element
from TkiWrapper.canvas.point import Point
import tkinter as tk

class Ellipse(Element):
  def __init__(self, canvas, center, radiusX, radiusY=None):
    super().__init__(canvas)
    self.center = Point(*center)
    self.radiusX = radiusX
    if radiusY is None: radiusY = radiusX
    self.radiusY = radiusY

  def draw(self):
    center = self.trp(self.center)
    radiusX = self.radiusX * self.cnv.SCALE.x
    radiusY = self.radiusY * self.cnv.SCALE.y
    boundA = center.shiftedClone(Point(-radiusX, -radiusY))
    boundB = center.shiftedClone(Point(radiusX, radiusY))
    self.cnv.canvas.create_arc(*boundA.get(), *boundB.get(), fill=self.fill.get(),
      width=self.strokeWidth, outline=self.stroke.get(), extent=359.99999,
      style=tk.CHORD)
