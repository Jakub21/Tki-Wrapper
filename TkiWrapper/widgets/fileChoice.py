import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as tkFile
from TkiWrapper.widgets.widget import Widget

class Filechoice(Widget):
  def __init__(self, view, key, choiceType, label, enabled=True, sticky='L',
      isSub=False, **fileParams):
    super().__init__(view, key)
    self.sticky = sticky
    method = self._getOnclick(choiceType, fileParams)
    style = self.view.root.style
    self.widget = ttk.Frame(view.holder)
    if not isSub: self.place()
    self.button = ttk.Button(self.widget, text=label, command=method)
    self.button.state(['!disabled'] if enabled else ['disabled'])
    self.button.grid(row=0, column=0)
    self.label = ttk.Label(self.widget, text='')
    self.label.grid(row=0, column=1, padx=style.fileChoiceLabelMargin)
    self.file = None
    self.changed = False

  def getFile(self):
    self.changed = False
    return self.file

  def read(self):
    self.changed = False
    return self.file.name

  def _onclick(self, tkMethod, fileParams):
    file = tkMethod(**fileParams)
    if file is None: return
    self.file = file
    try: self.label.configure(text=self.file.name.split('/')[-1])
    except AttributeError: self.label.configure(text='None')
    self.changed = True

  def _getOnclick(self, choiceType, fileParams):
    methods = {
      'openfile' : tkFile.askopenfile,
      'filename' : tkFile.askopenfilename,
      'savefile' : tkFile.asksaveasfilename,
      'directory': tkFile.askdirectory,
    }
    try:
      tkMethod = methods[choiceType]
    except KeyError:
      keys = ', '.join(list(methods.keys()))
      self.error(f'Invalid type "{choiceType}", please choose one of these'+\
        f'\n\t{keys}')
      raise KeyError('Invalid choiceType parameter')
    return lambda: self._onclick(tkMethod, fileParams)
