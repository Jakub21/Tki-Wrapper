from TkiWrapper.Logger import *
from TkiWrapper.RootBase import RootBase
import tkinter as tk
from tkinter import ttk

class RootPaned(RootBase):
  TYPE = 'PANED'
  def __init__(self, windowName, noOfSections, orient):
    super().__init__(windowName)
    if noOfSections < 2:
      Error(self, 'Number of sections in PanedRoot can not be less than 2')
    self.noOfSections = noOfSections
    self.orient = orient

    self.upperFrame = tk.PanedWindow(self.lowerFrame, bd=0)
    self.upperFrame.grid(column=0, row=0, sticky='nsew')
    self.panedSlots = [ttk.Frame(self.upperFrame) for i in range(noOfSections)]
    for subFrame in self.panedSlots:
      subFrame.columnconfigure(0, weight=1)
      subFrame.rowconfigure(0, weight=1)
      self.upperFrame.add(subFrame)

  # Programming interface


  # Internal methods

  def getParentFrame(self, slot):
    if slot is None:
      Error(self, 'Frame\'s default slot must be specified when using RootPaned')
      raise ValueError('No frame slot specified')
    return self.panedSlots[slot.x if self.orient == 'H' else slot.y]

  def showFrame(self, frame, *args):
    frame.lowerFrame.grid(column=0, row=0, sticky='nsew')

  def hideFrame(self, frame):
    frame.lowerFrame.grid_forget()
