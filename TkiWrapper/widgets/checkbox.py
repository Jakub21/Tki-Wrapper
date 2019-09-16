import tkinter as tk
from tkinter import ttk
from TkiWrapper.widgets.widget import Widget

class Checkbox(Widget):
  def __init__(self, view, key, label, action=None, enabled=True, sticky='L',
      isSub=False, **kwargs):
    super().__init__(view, key)
    self.sticky = sticky
    self.widget = ttk.Checkbutton(view.holder, text=label, **kwargs)
    self.widget.state(['!alternate'])
    self.widget.state(['!disabled'] if enabled else ['disabled'])
    if not isSub: self.place()

  def read(self):
    return 'selected' in self.widget.state()
