from tkinter import ttk
from TkiWrapper.Widget import Widget

class Button(Widget):
  def __init__(self, frame, label, onclick=None, sticky='LR', **kwargs):
    super().__init__(frame, sticky)
    self.tk = ttk.Button(frame.upperFrame, text=label, **kwargs)
    if onclick is not None:
      self.onclick(onclick)
    self.show()

  def onclick(self, callback):
    self.tk.configure(command=callback)
