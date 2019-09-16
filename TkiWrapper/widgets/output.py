import tkinter as tk
from tkinter import ttk
from TkiWrapper.widgets.widget import Widget

# NOTE: TTK widget can not have its font set through styles
# Using TK widget instead
# NOTE: Using "readonly" mode makes it impossible to copy text

class Output(Widget):
  def __init__(self, view, key, content, sticky='L', isSub=False, **kwargs):
    super().__init__(view, key)
    self.sticky = sticky
    style = self.view.root.style
    self.content = content
    self.widget = tk.Entry(view.holder, font=(style.fontFamily.mono,
      style.fontSize['output']), **kwargs)
    if not isSub: self.place()
    self.focus = False
    self.widget.bind('<FocusIn>', lambda evt: self.setFocus(True))
    self.widget.bind('<FocusOut>', lambda evt: self.setFocus(False))

  def update(self):
    self.widget.delete(0, tk.END)
    if callable(self.content): content = self.content(self)
    else: content = str(self.content)
    self.widget.insert(0, content)
    if self.focus:
      self._selectAll()
    else:
      self._selectNone()

  def setContent(self, content):
    self.content = content

  def setFocus(self, state):
    self.focus = state

  def _selectAll(self):
    self.widget.selection_range(0, tk.END)

  def _selectNone(self):
    self.widget.selection_clear()
