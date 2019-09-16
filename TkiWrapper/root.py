import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as tkFile
from TkiWrapper.namespace import Namespace, Dict
from TkiWrapper.style import Style
from TkiWrapper.logger import Logger

class Root(Logger):
  def __init__(self, title='Tki Window', panedSections=False):
    super().__init__(__file__)
    self.note(f'Starting root (paned={panedSections})')
    self.root = tk.Tk()
    self.style = Style()
    self.applyStyle(self.style)
    self.root.protocol('WM_DELETE_WINDOW', self.quit)
    self.root.columnconfigure(0, weight=1)
    self.root.rowconfigure(0, weight=1)
    self.setTitle(title)
    self.leave = False
    self.headers = {}
    self.footers = {}
    self.views = {}
    self.widgets = {}
    self.menuBar = None

    self.rootHolder = ttk.Frame(self.root)
    self.rootHolder.grid(column=0, row=0, sticky='nsew')
    self.rootHolder.columnconfigure(0, weight=1)
    self.setSectionWeights(0, 1, 0)
    # panedSections must be False or positive integer
    if panedSections:
      self.holder = tk.PanedWindow(self.rootHolder, bd=0)
      self.panedSlots = [ttk.Frame(self.holder) for i in range(panedSections)]
      for slot in self.panedSlots:
        slot.columnconfigure(0, weight=1)
        slot.rowconfigure(0, weight=1)
        self.holder.add(slot)
    else:
      self.holder = ttk.Frame(self.rootHolder)
      self.holder.columnconfigure(0, weight=1)
      self.holder.rowconfigure(0, weight=1)
    self.holder.grid(column=0, row=1, sticky='nsew')
    self.isPaned = panedSections

  #----------------------------------------------------------------
  # General core methods

  def update(self):
    try:
      if not self.leave:
        self.root.update()
        for key, widget in self.widgets.items():
          widget.update()
    except KeyboardInterrupt:
      self.error('Interrupted')
      self.leave = True
    except tk.TclError:
      if not self.leave: raise
    except:
      self.error('Uncaught error in main loop')
      raise

  def quit(self):
    self.warn(f'Root quitting')
    self.root.destroy()
    self.leave = True

  #----------------------------------------------------------------
  # Root window configuration and styling

  def setTitle(self, title):
    self.info('Setting root title')
    self.root.title(title)

  def setIcon(self, path):
    self.info('Setting root icon')
    self.root.iconbitmap(path)

  def setInitSize(self, x, y):
    self.info('Setting root fixed size')
    self.root.geometry(f'{x}x{y}')

  def setMinSize(self, x, y):
    self.info('Setting root minimal size')
    self.root.minsize(x, y)

  def setSectionWeights(self, header, content, footer):
    self.info('Setting root sections weights')
    self.rootHolder.rowconfigure(0, weight=header)
    self.rootHolder.rowconfigure(1, weight=content)
    self.rootHolder.rowconfigure(2, weight=footer)

  def setSlotsWeights(self, *weights):
    self.info('Setting main-frame slots weights')
    if self.isPaned:
      self.error('root.setSlotsWeights can only be used on non-paned roots')
      raise Exception('root.setSlotsWeights can only be used on non-paned roots')
    for index, weight in enumerate(weights):
      self.holder.columnconfigure(index, weight=weight)

  def applyStyle(self, style):
    self.style = style
    style.apply()

  #----------------------------------------------------------------
  # Adding views

  def getHolder(self, identifer):
    '''Called by ViewCore class on init to determine parent holder'''
    if identifer in ('h', 'f'):
      return self.rootHolder
    if self.isPaned:
      return self.panedSlots[identifer]
    return self.holder

  def _addView(self, view, viewType, key):
    if viewType == 'h': self.headers[key] = view
    elif viewType == 'f': self.footers[key] = view
    else: self.views[key] = view

  def show(self, key):
    new = self.views[key]
    self.note(f'Switching slot {new.viewType} to view "{key}"')
    for k, view in self.views.items():
      if view.viewType == new.viewType:
        view.hide()
    new.show()

  #----------------------------------------------------------------
  # Managing widgets

  def addWidget(self, widget):
    try:
      self.widgets[widget.key]
      self.error('Widget with this key already exists')
      raise Exception('Widget with this key already exists')
    except KeyError:
      self.widgets[widget.key] = widget

  def getByKey(self, key):
    try: return self.widgets[key]
    except KeyError:
      self.error(f'Could not find widget with key "{key}"')
      raise Exception(f'Could not find widget with key "{key}"')

  #----------------------------------------------------------------
  # Managing widgets

  def setMenuBar(self, menuBar):
    self.menuBar = menuBar
    self.root.config(menu=menuBar.menu)
