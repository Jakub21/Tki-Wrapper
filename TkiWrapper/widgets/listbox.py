import tkinter as tk
from tkinter import ttk
from TkiWrapper.widgets.widget import Widget

class Listbox(Widget):
  def __init__(self, view, key, values, selMode='browse', enabled=True,
      sticky='L', isSub=False, **kwargs):
    super().__init__(view, key)
    self.sticky = sticky
    style = self.view.root.style
    state = 'normal' if enabled else 'disabled'
    selMode = {
      'browse': tk.BROWSE,
      'single': tk.SINGLE,
      'multiple': tk.MULTIPLE,
      'extended': tk.EXTENDED,
    }[selMode]
    self.widget = tk.Listbox(view.holder, font=(style.fontFamily.mono,
      style.fontSize['listbox']), state=state, selectmode=selMode, **kwargs)
    self.widget.insert(0, *values)
    if not isSub: self.place()

  def read(self):
    selection = list(self.widget.curselection())
    return [self.widget.get(i) for i in selection]
