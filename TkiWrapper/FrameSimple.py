from TkiWrapper.FrameBase import FrameBase
from tkinter import ttk

class FrameSimple(FrameBase):
  def __init__(self, parent, defaultSlot=None, positioner=None, **kwargs):
    super().__init__(parent, defaultSlot, positioner, **kwargs)
    self.lowerFrame.columnconfigure(0, weight=1)
    self.lowerFrame.rowconfigure(0, weight=1)
    self.upperFrame = ttk.Frame(self.lowerFrame)
    self.upperFrame.grid(column=0, row=0, sticky='nsew')

  def getParentFrame(self, slot):
    return self.upperFrame

  def setRowWeights(self, *weights):
    for index, weight in enumerate(weights):
      self.upperFrame.rowconfigure(index, weight=weight)

  def setColWeights(self, *weights):
    for index, weight in enumerate(weights):
      self.upperFrame.columnconfigure(index, weight=weight)
