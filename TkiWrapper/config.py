from TkiWrapper.namespace import Namespace
import TkiWrapper as tkw

conf = Namespace(
  WARNINGS_SILENCED = False,
  # Enable wrapper internal logs to console
  LOGS_ENABLED = False,
  # Positioner passed to ViewCore constructor when other is not defined
  POSITIONER = 'Grid',
  # Positioner GRID config
  POSGRID_STICKY = 'LRH',
  # Default view grid weights
  VIEW_ROW_WEIGHTS = [],
  VIEW_COL_WEIGHTS = [],
  # Style class default properties
  STYLE = Namespace(
    THEME = 'default', # TTK Theme
    BTN_WIDTH = None, # Button fixed width (None for non-fixed)
    FC_LABEL_MARGIN = 4, # FileChoice widget's label's horizontal margin
    # Font size
    FS_HEAD1 = 25,
    FS_HEAD2 = 20,
    FS_HEAD3 = 15,
    FS_LABEL = 11,
    FS_OUTPUT = 12,
    FS_BUTTON = 10,
    FS_CHECKBOX = 11,
    FS_INPUT = 12,
    FS_LISTBOX = 12,
    # Font family
    FONT_STD = 'Verdana',
    FONT_MONO = 'Courier New',
    # App colors
    CLR_FG = '#000',
    CLR_BG = '#CFCFCF',
    CLR_DISABLED = '#AAA',
    CLR_TEXT_FG = '#FFF',
    CLR_TEXT_BG = '#000',
  ),
  CANVAS = Namespace(
    COLOR_ENABLE_HSL = True, # Enable HSL Color mode (may slow down the program)
    VECTOR_ARROW_MAXLEN = 3, # in canvas width units
    VECTOR_ARROW_RATIO = 0.15,
    VECTOR_ARROW_ANGLE = 0.15, # radians
  )
)

def config(key, value):
  if '.' in key:
    target = conf.__dict__
    key = key.split('.')
    for i, subkey in enumerate(key[:-1]):
      target = target[subkey]
      if i != len(key)-1: target = target.__dict__
    target[key[-1]] = value
  else:
    conf.__dict__[key] = value

def configToPrintable():
  return conf.toString(className='TkwConfig')
