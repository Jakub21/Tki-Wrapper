import tkinter as tk
from tkinter import ttk
from TkiWrapper.namespace import Namespace, Dict
from TkiWrapper.logger import Logger
from TkiWrapper.config import conf

class Style(Logger):
  def __init__(self):
    super().__init__(__file__)
    self.theme = conf.STYLE.THEME
    self.buttonWidth = conf.STYLE.BTN_WIDTH
    self.fileChoiceLabelMargin = conf.STYLE.FC_LABEL_MARGIN # horizontal
    self.fontSize = Dict(
      heading1 = conf.STYLE.FS_HEAD1,
      heading2 = conf.STYLE.FS_HEAD2,
      heading3 = conf.STYLE.FS_HEAD3,
      label = conf.STYLE.FS_LABEL,
      output = conf.STYLE.FS_OUTPUT,
      button = conf.STYLE.FS_BUTTON,
      checkbox = conf.STYLE.FS_CHECKBOX,
      input = conf.STYLE.FS_INPUT,
      listbox = conf.STYLE.FS_LISTBOX,
    )
    self.fontFamily = Namespace(
      std = conf.STYLE.FONT_STD,
      mono = conf.STYLE.FONT_MONO,
    )
    self.colors = Namespace(
      fg = conf.STYLE.CLR_FG,
      bg = conf.STYLE.CLR_BG,
      disabled = conf.STYLE.CLR_DISABLED,
      textFg = conf.STYLE.CLR_TEXT_FG,
      textBg = conf.STYLE.CLR_TEXT_BG,
    )

  #----------------------------------------------------------------
  # Setters to use in app

  def setTheme(self, theme):
    self.theme = theme

  def setFontSize(self, key, value):
    if key not in self.fontSize.keys():
      self.error('Invalid font size key')
      raise KeyError('Invalid font size key')
    self.fontSize[key] = value

  def setFontFam(self, key, value):
    d = self.fontFamily.__dict__
    if key not in d.keys():
      self.error('Invalid font type key')
      raise KeyError('Invalid font type key')
    d[key] = value

  def setColor(self, key, value):
    if key not in self.colors.__dict__.keys():
      self.error('Invalid color key')
      raise KeyError('Invalid color key')
    self.colors.__dict__[key] = value

  def setButtonFixedWidth(self, width):
    self.buttonWidth = width

  #----------------------------------------------------------------
  # Core

  def apply(self):
    self.debug('Applying styles')
    style = ttk.Style()
    # Set theme
    if self.theme is not None:
      style.theme_use(self.theme)
    # Helpers
    getStd = lambda k: (self.fontFamily.std, self.fontSize[k])
    getMono = lambda k: (self.fontFamily.mono, self.fontSize[k])
    kw = Dict(background=self.colors.bg, foreground=self.colors.fg)
    # Configure TTK styles
    style.configure('TFrame', **kw)
    style.configure('TLabel', font=getStd('label'), **kw)
    style.configure('heading1.TLabel', font=getStd('heading1'), **kw)
    style.configure('heading2.TLabel', font=getStd('heading2'), **kw)
    style.configure('heading3.TLabel', font=getStd('heading3'), **kw)
    style.configure('output.TEntry', font=getMono('output'),
      background=self.colors.bg)
    style.configure('TSeparator', **kw)
    style.configure('TCheckbutton', font=getStd('checkbox'), **kw)
    # Apply button styles including fixed width if is set
    if self.buttonWidth is None:
      style.configure('TButton', font=getStd('button'),
        background=self.colors.bg)
    else:
      style.configure('TButton', font=getStd('button'), width=self.buttonWidth,
        background=self.colors.bg)
