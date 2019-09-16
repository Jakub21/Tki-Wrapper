import tkinter as tk
from tkinter import ttk
from TkiWrapper.widgets.widget import Widget

class Input(Widget):
  def __init__(self, view, key, isPwd=False, enabled=True, sticky='L',
      isSub=False, **kwargs):
    super().__init__(view, key)
    self.sticky = sticky
    style = self.view.root.style
    state = 'normal' if enabled else 'disabled'
    self.widget = tk.Entry(view.holder, font=(style.fontFamily.mono,
      style.fontSize['input']), state=state, **kwargs)
    if not isSub: self.place()

  def read(self):
    return self.widget.get()

  def insert(self, *args, **kwargs):
    self.widget.insert(*args, **kwargs)

  def delete(self, *args, **kwargs):
    self.widget.delete(*args, **kwargs)
