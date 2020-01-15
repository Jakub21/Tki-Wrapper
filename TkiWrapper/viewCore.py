import tkinter as tk
from tkinter import ttk
from TkiWrapper.namespace import Namespace
from TkiWrapper.logger import Logger
from TkiWrapper.config import conf
import TkiWrapper.positioners as tkp

STICKY_ALL = 'nsew'

class ViewCore(Logger):
  '''Contains core methods for views
  using this class in projects may work in some appliances but
  inherintents are recommended'''
  def __init__(self, root, key, viewType=0, positioner=None):
    super().__init__(__file__)
    self.root = root
    self.key = key
    if positioner is None:
      positionerClass = tkp.Register.get(conf.POSITIONER)
      positioner = positionerClass(self)
    self.positioner = positioner
    self.pst = self.positioner # alias
    self.holder = ttk.Frame(root.getHolder(viewType))
    self.viewType = viewType
    self.fixedSize = 0, 0
    self.dialogs = {}
    self.root._addView(self, viewType, key)
    self.setRowWeights(*conf.VIEW_ROW_WEIGHTS)
    self.setColWeights(*conf.VIEW_COL_WEIGHTS)
    self.shown = False

  def __enter__(self):
    return self

  def __exit__(self, *args):
    pass

  #----------------------------------------------------------------
  # User methods

  def setRowWeights(self, *weights):
    for row, weight in enumerate(weights):
      self.holder.rowconfigure(row, weight=weight)

  def setColWeights(self, *weights):
    for col, weight in enumerate(weights):
      self.holder.columnconfigure(col, weight=weight)

  def setFixedSize(self, width, height):
    self.fixedSize = width, height

  #----------------------------------------------------------------
  # Internal methods

  def add(self, widget):
    '''Adds widget to view'''
    self.root.addWidget(widget)

  def hide(self):
    '''Hide view'''
    self.holder.grid_forget()
    self.shown = False

  def show(self):
    '''Show view on screen'''
    slot = self.viewType
    if self.viewType in ('h', 'f'):
      self.holder.grid(row = 0 if self.viewType == 'h' else 2, sticky=STICKY_ALL)
    else:
      if self.root.isPaned: self._showMainPaned(slot)
      else: self._showMainNonPaned(slot)
    if self.fixedSize != (0, 0):
      self._applyFixedSize()
    self.shown = True

  def _showMainPaned(self, slot):
    try: slotFrame = self.root.panedSlots[slot]
    except IndexError:
      self.error('Invalid slot index')
      raise Exception('Invalid slot index')
    self.holder.grid(sticky=STICKY_ALL)

  def _showMainNonPaned(self, slot):
    self.holder.grid(column=slot, row=0, sticky=STICKY_ALL)

  def _applyFixedSize(self):
    '''Applies holder's fixed size (required after every self.show call)'''
    self.holder.grid_propagate(False)
    width, height = self.fixedSize
    self.holder.configure(width=width, height=height)
