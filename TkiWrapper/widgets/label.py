import tkinter as tk
from tkinter import ttk
from TkiWrapper.widgets.widget import Widget

class Label(Widget):
  def __init__(self, view, label, heading=None, key=None, sticky='L',
      isSub=False, **kwargs):
    super().__init__(view, key)
    self.sticky = sticky
    if heading is not None:
      if heading < 1 or heading > 3:
        raise Exception('Invalid heading level, only 1-3 are supported')
      style = f'heading{heading}.TLabel'
      self.widget = ttk.Label(view.holder, text=label, style=style, **kwargs)
    else:
      self.widget = ttk.Label(view.holder, text=label, **kwargs)
    if not isSub: self.place()

  def setText(self, text):
    self.widget.configure(text=text)
