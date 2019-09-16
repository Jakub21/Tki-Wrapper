from TkiWrapper.canvas.element import Element
from TkiWrapper.canvas.point import Point
import tkinter as tk
from PIL import ImageTk, Image as PImage

class Image(Element):
  def __init__(self, canvas, anchor, size, image):
    super().__init__(canvas)
    self.anchor = Point(*anchor)
    self.pilImage = image
    if size == (None, None):
      raise ValueError('Define at least one dimension of image size')
    self.size = Point(*size)

  def draw(self):
    ptA = self.trp(self.anchor)
    ptB = self.trp(self.size)
    revAnchor = ptA.clone()
    revAnchor.mult(-1)
    size = ptB.shiftedClone(revAnchor)
    targetSize = int(size.x), int(size.y)
    anchor = self.trp(self.anchor)
    anchorShift = size
    anchorShift.mult(0.5)
    anchor.shift(anchorShift)
    resized = self.pilImage.resize(targetSize)
    self.tkImage = ImageTk.PhotoImage(image=resized)
    self.cnv.canvas.create_image(anchor.get(), image=self.tkImage)
