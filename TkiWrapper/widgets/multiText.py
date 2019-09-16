import tkinter as tk
from tkinter import ttk
from TkiWrapper.widgets.widget import Widget

class Multitext(Widget):
  def __init__(self, view, key=None, sticky='LRH', isSub=False, **kwargs):
    super().__init__(view, key)
    self.sticky = sticky
    self.widget = tk.Text(view.holder, **kwargs)
    if not isSub: self.place()

  def insert(self, *args, **kwargs):
    self.widget.insert(*args, **kwargs)

  def delete(self, *args, **kwargs):
    self.widget.delete(*args, **kwargs)

  def bind(self, *args, **kwargs):
    self.widget.bind(*args, **kwargs)

  def see(self, *args, **kwargs):
    self.widget.see(*args, **kwargs)

  def tag_config(self, *args, **kwargs):
    self.widget.tag_config(*args, **kwargs)
