import tkinter as tk
from tkinter import ttk
from TkiWrapper.logger import Logger

class Menu(Logger):
  def __init__(self, parent, **kwargs):
    try: parent = parent.menu
    except AttributeError: parent = parent.root
    self.parent = parent
    self.menu = tk.Menu(parent, **kwargs)

  def addCascade(self, label, menu):
    self.menu.add('cascade', label=label, menu=menu.menu)

  def addCommand(self, label, command):
    self.menu.add_command(label=label, command=command)

  def addSeparator(self):
    self.menu.add_separator()
