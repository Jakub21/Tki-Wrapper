from TkiWrapper.Logger import *
from TkiWrapper.RootBase import RootBase

class Root(RootBase):
  def __init__(self, windowName):
    super().__init__(windowName)
    self.upperFrame = self.lowerFrame

  # Programming interface

  def setColWeights(self, *weights):
    for i, weight in enumerate(weights):
      self.upperFrame.columnconfigure(i, weight=weight)

  def setRowWeights(self, *weights):
    for i, weight in enumerate(weights):
      self.upperFrame.rowconfigure(i, weight=weight)

  # Internal methods

  def getParentFrame(self, *args):
    return self.upperFrame

  def showFrame(self, frame, slot=None):
    if slot is None: slot = frame.defaultSlot
    if slot is None:
      raise ValueError('No frame slot specified')
    try:
      slave = self.getSlave(slot)
      slave.lowerFrame.grid_forget()
      self.delSlave(slot)
    except KeyError: pass
    self.addSlave(slot, frame)
    config = {}
    config['column'] = slot.x; config['row'] = slot.y
    config['columnspan'] = slot.spanX; config['rowspan'] = slot.spanY
    frame.lowerFrame.grid(**config, sticky='nsew')

  def hideFrame(self, frame):
    frame.lowerFrame.grid_forget()
