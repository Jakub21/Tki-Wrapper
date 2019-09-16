import tkinter as tk
from tkinter import ttk
from TkiWrapper.widgets.widget import Widget

class Combo(Widget):
  def __init__(self, view, key, values, allowUnlisted=False, enabled=True,
      sticky='L', isSub=False, **kwargs):
    super().__init__(view, key)
    self.sticky = sticky
    self.widget = ttk.Combobox(view.holder, values=values, exportselection=0,
      **kwargs)
    self.widget.state(['!disabled'] if enabled else ['disabled'])
    if not isSub: self.place()
    self.allowUnlisted = allowUnlisted
    self.values = values
    self.validValue = True

  def read(self):
    if self.allowUnlisted:
      return self.widget.get()
    else:
      index = self.widget.current()
      if index == -1:
        self.error('Invalid Choice, please select item from list')
        self.validValue = False
        return self.widget.get()
      self.validValue = True
      return self.values[index]
