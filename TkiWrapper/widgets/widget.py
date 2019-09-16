import tkinter as tk
from tkinter import ttk
from TkiWrapper.namespace import Namespace
from TkiWrapper.logger import Logger

AUTOKEY = 0

class Widget(Logger):
  '''Widget template class'''
  def __init__(self, view, key):
    super().__init__(__file__)
    self.widgetType = self.__class__.__name__
    if key is None:
      global AUTOKEY
      key = f'{self.widgetType.lower()}_{AUTOKEY}_'
      AUTOKEY += 1
    self.key = key
    self.debug(f'Creating widget {self.widgetType}')
    self.view = view
    self.view.add(self)

  def place(self):
    self.widget.grid(**self.view.pst.getPos(self, sticky=self.sticky))

  def bind(self, *args, **kwargs):
    self.widget.bind(*args, **kwargs)

  def state(self, value):
    try: self.widget['state'] = 'normal' if value else 'disabled'
    except: self.widget.state(['!disabled'] if value else ['disabled'])

  def update(self):
    pass
