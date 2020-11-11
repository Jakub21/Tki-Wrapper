from tkinter import ttk
from TkiWrapper.Widget import Widget

class Label(Widget):
  def __init__(self, frame, content, sticky='L', **kwargs):
    super().__init__(frame, sticky)
    self.tk = ttk.Label(frame.upperFrame, **kwargs)
    self.show()
    self.set(content)

  def set(self, content):
    if not self.checkAlive(): return
    self.tk.config(text=content)
