import tkinter as tk
from TkiWrapper.namespace import Namespace
from TkiWrapper.logger import Logger
from TkiWrapper.config import conf

class Grid(Logger):
  DEFAULTS = Namespace(
    marginX = 0,
    marginY = 0,
    paddingX = 0,
    paddingY = 0,
  )
  def __init__(self, view):
    super().__init__(__file__)
    self.view = view
    self.debug('Grid initialized')
    self.pointer = Namespace(
      x = 0, y = 0,
      spanX = 1, spanY = 1,
    )
    self.colWrap = 1

  #----------------------------------------------------------------
  # Pointer auto-increment settings

  def setColWrap(self, width):
    '''Pointer auto increment only works if no element has spanY more than 1
    This may be repaired if project is not dumped'''
    self.colWrap = width

  #----------------------------------------------------------------
  # Widget pointer manipulation

  def resetPointer(self):
    self.pointer = Namespace(
      x = 0, y = 0,
      spanX = 1, spanY = 1,
    )

  def setPointer(self, x, y, spanX=1, spanY=1):
    self.pointer.x = x
    self.pointer.y = y
    self.pointer.spanX = spanX
    self.pointer.spanY = spanY

  def setSpan(self, spanX=1, spanY=1):
    self.pointer.spanX = spanX
    self.pointer.spanY = spanY

  def newLine(self):
    self.pointer.x = 0
    self.pointer.y += 1

  def shift(self, amount=1):
    self.pointer.x += amount
    if self.pointer.x >= self.colWrap:
      self.pointer.x = 0
      self.pointer.y += 1

  #----------------------------------------------------------------
  # Default margin settings

  def setMargin(self, x, y):
    self.DEFAULTS.marginX = x
    self.DEFAULTS.marginY = y

  def setPadding(self, x, y):
    self.DEFAULTS.paddingX = x
    self.DEFAULTS.paddingY = y

  #----------------------------------------------------------------
  # Class internal utilities

  def getPos(self, widget, sticky=None, **kwargs):
    result = {
      'column': self.pointer.x,
      'row': self.pointer.y,
      'columnspan': self.pointer.spanX,
      'rowspan': self.pointer.spanY,
    }
    if sticky is None:
      sticky = conf.POSGRID_STICKY
    sticky = sticky.upper()
    stickyParam = 'n'
    if 'H' in sticky: stickyParam += 's'
    if 'R' in sticky: stickyParam += 'e'
    if 'L' in sticky: stickyParam += 'w'
    result['sticky'] = stickyParam
    try: result['padx'] = kwargs['marginX']
    except KeyError: result['padx'] = self.DEFAULTS.marginX
    try: result['pady'] = kwargs['marginY']
    except KeyError: result['pady'] = self.DEFAULTS.marginY

    try: result['ipadx'] = kwargs['paddingX']
    except KeyError: result['ipadx'] = self.DEFAULTS.paddingX
    try: result['ipadx'] = kwargs['paddingX']
    except KeyError: result['ipadx'] = self.DEFAULTS.paddingX

    self.debug(f'Placing widget {widget.widgetType} "{widget.key}" in {self.view.key}'+\
      f'[{self.pointer.x}, {self.pointer.y}] sticky="{sticky}"')
    self.incrementPointer()
    return result

  def incrementPointer(self):
    self.pointer.x += self.pointer.spanX
    if self.pointer.x >= self.colWrap:
      self.pointer.x = 0
      self.pointer.y += 1
    self.pointer.spanX = 1
    self.pointer.spanY = 1
