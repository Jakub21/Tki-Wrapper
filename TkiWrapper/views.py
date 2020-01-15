from TkiWrapper.viewCore import ViewCore
import tkinter as tk
from tkinter import ttk

STICKY_ALL = 'nsew'


class HeaderView(ViewCore):
  '''View to use as header'''
  def __init__(self, root, key, positioner=None):
    super().__init__(root, key, 'h', positioner)
    self.show()


class FooterView(ViewCore):
  '''View to use as footer'''
  def __init__(self, root, key, positioner=None):
    super().__init__(root, key, 'f', positioner)
    self.show()


class View(ViewCore):
  '''View to place in main frame'''
  def __init__(self, root, key, slot, positioner=None, showKey=None):
    super().__init__(root, key, slot, positioner)
    if showKey is not None:
      self.root.root.bind(showKey, lambda evt: self.root.show(self.key))

  def changeSlot(self, slot):
    if self.shown:
      raise Exception('Only can change view\'s slot when it is not shown')
    self.viewType = slot


class ScrollableView(View):
  '''View to place in main frame, includes scrolls'''
  def __init__(self, root, key, slot, positioner=None, showKey=None):
    super().__init__(root, key, slot, positioner, showKey)
    self.superHolder = self.holder
    self.superHolder.columnconfigure(0, weight=1)
    self.superHolder.rowconfigure(0, weight=1)
    self.canvas = tk.Canvas(self.superHolder, highlightthickness=0, bg='#000')
    self.scrollbar = ttk.Scrollbar(self.superHolder, orient='vertical',
      command=self.canvas.yview)
    self.canvas.configure(yscrollcommand=self.scrollbar.set)
    self.canvas.grid(column=0, row=0, sticky='nsew')
    self.scrollbar.grid(column=1, row=0, sticky='ns')

    self.holder = ttk.Frame(self.canvas)
    self.holder.bind('<Configure>',
      lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))
    self.canvas.bind('<Configure>',
      lambda e: self.canvas.itemconfig(self.windowID, width=e.width))
    self.windowID = self.canvas.create_window((0,0), window=self.holder, anchor='nw')

  def hide(self):
    self.superHolder.grid_forget()
    self.shown = False

  def show(self):
    '''Show view on screen'''
    slot = self.viewType
    if self.viewType in ('h', 'f'):
      self.superHolder.grid(row = 0 if self.viewType == 'h' else 2, sticky=STICKY_ALL)
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
    self.superHolder.grid(sticky=STICKY_ALL)

  def _showMainNonPaned(self, slot):
    self.superHolder.grid(column=slot, row=0, sticky=STICKY_ALL)
