from TkiWrapper.Logger import *
from TkiWrapper.Holder import Holder
from Namespace import Namespace
import tkinter as tk
from tkinter import ttk

class RootBase(Holder, LogIssuer):
  '''Properties and methods common for all Root variants'''
  def __init__(self, windowName):
    super().__init__()
    self.setIssuerData()
    Info(self, f'Creating root "{windowName}"')
    self.windowName = windowName
    self.applicationDestroyed = False

    self.tk = tk.Tk(windowName)
    self.tk.protocol('WM_DELETE_WINDOW', self.onAppDestroyed)
    self.tk.columnconfigure(0, weight=1)
    self.tk.rowconfigure(0, weight=1)
    self.setTitle(windowName)

    self.lowerFrame = ttk.Frame(self.tk)
    self.lowerFrame.grid(column=0, row=0, sticky='nsew')

    # Info(self, Namespace.getObjectStructure(self))

  # Context manager

  def __enter__(self):
    return self

  def __exit__(self, *args):
    pass

  # Programming interface

  def update(self):
    self.tk.update()

  def isRunning(self):
    return not self.applicationDestroyed

  def setTitle(self, title):
    Info(self, 'Setting root title')
    self.tk.title(title)

  def setIcon(self, path):
    Info(self, 'Setting root icon')
    self.tk.iconbitmap(path)

  def setInitialSize(self, x, y):
    self.tk.geometry(f'{x}x{y}')

  def setMinSize(self, x, y):
    self.tk.minsize(x, y)

  def bind(self, key, callback):
    self.tk.bind(key, callback)

  # Internal methods

  def onAppDestroyed(self):
    Info(self, 'Application stopped')
    self.applicationDestroyed = True

  def getRoot(self):
    return self
