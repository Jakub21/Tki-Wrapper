import os
from TkiWrapper.namespace import Namespace
from TkiWrapper.config import conf
from datetime import datetime
from colorama import init as coloramaInit, Fore as ColoramaFore
from colorama import Style as coloramaStyle
RESET_COLOR = coloramaStyle.RESET_ALL
coloramaInit()

# print('Colorama FGs: ', ', '.join(ColoramaFore.__dict__.keys()))
# print('Colorama Styles: ', ', '.join(coloramaStyle.__dict__.keys()))

def clrPrint(color, *args, dark=False, **kwargs):
  header = ColoramaFore.__dict__[color]
  if dark == 2: header += coloramaStyle.DIM
  elif dark == 0: header += coloramaStyle.BRIGHT
  print(end=header)
  print(*args, **kwargs)
  print(end=RESET_COLOR)

class Logger:
  '''Class for normalizing terminal output'''
  def __init__(self, file):
    self.promptStr = '> '
    self.__loggerEnabled__ = conf.LOGS_ENABLED
    self.__loggerFile__ = file

  def error(self, msg):
    self._prompt()
    self._say('RED', msg)

  def warn(self, msg):
    self._prompt()
    self._say('YELLOW', msg)

  def note(self, msg):
    self._prompt()
    self._say('CYAN', msg)

  def info(self, msg):
    self._prompt()
    self._say('WHITE', msg)

  def debug(self, msg):
    self._prompt()
    self._say('LIGHTBLACK_EX', msg)

  def _say(self, color, msg):
    if self.__loggerEnabled__:
      clrPrint(color, msg)

  def _prompt(self):
    if self.__loggerEnabled__:
      cls = self.__class__.__name__
      time = self._loggerGetTime()
      path = self._getPath()
      clrPrint('MAGENTA', end=f'[{time} {path}{cls}]: ')

  def _loggerGetTime(self):
    now = datetime.now()
    hour = str(now.hour)
    if len(hour) <2: hour = f'0{hour}'
    minute = str(now.minute)
    if len(minute) <2: minute = f'0{minute}'
    second = str(now.second)
    if len(second) <2: second = f'0{second}'
    return f'{hour}:{minute}:{second}'

  def _getPath(self):
    path = self.__loggerFile__.split(os.path.sep)[-2]
    result = {
      'TkiWrapper':   'Core',
      'positioners':  'Positioner',
      'canvas':       'Canvas',
      'widgets':      'Widget',
    }[path]
    return result + '.'
