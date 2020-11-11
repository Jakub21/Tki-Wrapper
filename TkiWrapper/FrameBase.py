from TkiWrapper.Logger import *
from TkiWrapper.Point import Point
from Positioners.SimpleGrid import SimpleGrid
from TkiWrapper.Holder import Holder
from tkinter import ttk

class FrameBase(Holder, LogIssuer):
  '''Properties and methods common for all Frame variants'''
  def __init__(self, parent, defaultSlot=None, positioner=None, **kwargs):
    super().__init__()
    self.setIssuerData()
    Info(self, 'Frame created')
    self.parent = parent
    self.defaultSlot = defaultSlot if defaultSlot is not None else Point()
    self.slot = Point('auto')
    self.isShown = False
    self.alive = True
    self.lowerFrame = ttk.Frame(self.parent.getParentFrame(defaultSlot), **kwargs)
    if positioner is None:
      self.pst = SimpleGrid(self)
    else: self.pst = positioner
    self.callbacks = Namespace()

  # Context manager

  def __enter__(self):
    return self

  def __exit__(self, *args):
    pass

  # Programming interface

  def show(self, slot=None):
    self.parent.hideFrame(self)
    slot = slot if slot is not None else self.defaultSlot
    if not isinstance(slot, Point):
      Error(self, 'Frame slot must be object of class TkiWrapper.Point')
    if slot is None and self.defaultSlot is None:
      Error(self, 'When showing frame with no default slot, you must specify one')
      raise ValueError('No frame slot specified')
    self.parent.showFrame(self, slot)
    self.isShown = True
    Debug(self, 'Frame shown')
    if 'onShow' in self.callbacks.keys(): self.callbacks.onShow()

  def hide(self):
    self.parent.hideFrame(self)
    self.isShown = False
    Debug(self, 'Frame hidden')
    if 'onHide' in self.callbacks.keys(): self.callbacks.onHide()

  def isAlive(self):
    '''Alive checker for external use'''
    return self.alive

  def checkAlive(self):
    '''Internal alive checker with auto warn'''
    if not self.alive:
      Warn(self, 'Attempted to call method of a deleted widget')
    return self.alive

  def delete(self):
    self.alive = False
    self.lowerFrame.destroy()
    self.upperFrame.destroy()
    del self

  def showOnKey(self, key):
    Debug(self, 'Binding frame to key')
    self.getRoot().tk.bind(key, lambda evt: self.show())

  def onShow(self, callback):
    self.callbacks.onShow = callback

  def onHide(self, callback):
    self.callbacks.onHide = callback

  # Internal methods

  def showFrame(self, frame, slot):
    if slot.isAuto:
      frame.lowerFrame.grid(**self.pst.get('LRH'))
    else:
      config = {}
      config['column'] = slot.x; config['row'] = slot.y
      config['columnspan'] = slot.spanX; config['rowspan'] = slot.spanY
      frame.lowerFrame.grid(**config, sticky='nsew')

  def hideFrame(self, frame):
    frame.lowerFrame.grid_forget()

  def getRoot(self):
    return self.parent.getRoot()
