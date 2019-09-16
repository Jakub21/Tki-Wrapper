import tkinter as tk
from tkinter import ttk
from TkiWrapper.widgets.widget import Widget

class Separator(Widget):
  def __init__(self, view, key=None, sticky='LR', isSub=False, **kwargs):
    super().__init__(view, key)
    self.sticky = sticky
    self.widget = ttk.Separator(view.holder, **kwargs)
    if not isSub: self.place()
