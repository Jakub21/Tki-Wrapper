import tkinter as tk
from tkinter import ttk
from TkiWrapper.Logger import *
from TkiWrapper.FrameBase import FrameBase

class FrameScrollable(FrameBase):
  def __init__(self, parent, defaultSlot=None, scrollAxes='Y', positioner=None, **kwargs):
    super().__init__(parent, defaultSlot, positioner)
    self.lowerFrame.columnconfigure(0, weight=1)
    self.lowerFrame.rowconfigure(0, weight=1)

    self.scrollAxes = scrollAxes.upper()
    self.canvas = tk.Canvas(self.lowerFrame, highlightthickness=0, **kwargs)
    self.canvas.grid(column=0, row=0, sticky='nsew')
    self.upperFrame = ttk.Frame(self.canvas)
    self.windowID = self.canvas.create_window((0,0), window=self.upperFrame, anchor='nw')
    # Vertical scroll bar
    if 'Y' in self.scrollAxes:
      self.barY = ttk.Scrollbar(self.lowerFrame, orient='vertical',
        command=self.canvas.yview)
      self.canvas.config(yscrollcommand=self.barY.set)
      self.barY.grid(column=1, row=0, sticky='ns')
    # Horizontal scroll bar
    if 'X' in self.scrollAxes:
      self.barX = ttk.Scrollbar(self.lowerFrame, orient='horizontal',
        command=self.canvas.xview)
      self.canvas.config(xscrollcommand=self.barX.set)
      self.barX.grid(column=0, row=1, sticky='ew')
    # Handle window resizing
    self.canvas.bind('<Configure>', self.onResizeCanvas)
    self.upperFrame.bind('<Configure>', self.onResizeUpper)

  def onResizeCanvas(self, event):
    if 'X' not in self.scrollAxes: self.canvas.itemconfig(self.windowID, width=event.width)
    if 'Y' not in self.scrollAxes: self.canvas.itemconfig(self.windowID, height=event.height)

  def onResizeUpper(self, event):
    self.canvas.configure(scrollregion=self.canvas.bbox('all'))


  def getParentFrame(self, slot):
    return self.upperFrame

  def setRowWeights(self, *weights):
    for index, weight in enumerate(weights):
      self.upperFrame.rowconfigure(index, weight=weight)

  def setColWeights(self, *weights):
    for index, weight in enumerate(weights):
      self.upperFrame.columnconfigure(index, weight=weight)
