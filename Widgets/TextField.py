import tkinter as tk
from TkiWrapper.Widget import Widget

class TextField(Widget):
  def __init__(self, frame, sticky='L', **kwargs):
    super().__init__(frame, sticky)
    self.tk = tk.Entry(frame.upperFrame, **kwargs)
    self.show()

  def set(self, content):
    if not self.checkAlive(): return
    self.tk.delete(0, 'end')
    self.tk.insert(0, content)

  def get(self):
    if not self.checkAlive(): return
    return self.tk.get()
