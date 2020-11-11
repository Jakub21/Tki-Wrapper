from tkinter import ttk
from TkiWrapper.Widget import Widget

class Placeholder(Widget):
  def __init__(self, frame, sticky='L', **kwargs):
    super().__init__(frame, sticky)
    self.tk = ttk.Frame(frame.upperFrame, **kwargs)
    self.show()
