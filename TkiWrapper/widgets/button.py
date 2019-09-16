import tkinter as tk
from tkinter import ttk
from TkiWrapper.widgets.widget import Widget

class Button(Widget):
  def __init__(self, view, key, label, action=None, enabled=True, sticky='L',
      isSub=False, **kwargs):
    super().__init__(view, key)
    self.sticky = sticky
    if action is None: command = lambda: None
    else: command = action
    self.widget = ttk.Button(view.holder, text=label, command=action, **kwargs)
    self.widget.state(['!disabled'] if enabled else ['disabled'])
    if not isSub: self.place()

  def setOnclick(self, action):
    self.widget.configure(command=action)
