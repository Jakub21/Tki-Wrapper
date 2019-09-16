'''File automatically imports all widget classes
Limitations:
- only imports one class from each file
- class name must be same as file name
- class name must consist only of lowercase letters
  except for 1st letter which must be uppercase (result of filename.title())
'''
import os

try:
  sep = os.path.sep
  files = [f for f in os.listdir(sep.join(__file__.split(sep)[:-1])) if \
    f.endswith('.py') and not f.startswith('__init__')]

  for file in files:
    fname = file[:file.index('.')]
    dotpath = f'TkiWrapper.canvas.elements.{fname}'
    className = fname
    try: exec(f'from {dotpath} import {className}')
    except ImportError:
      print(className)
      if className != 'Ocvimage': raise
except:
  print(f'Unexpected error in canvas.elements.__init__\nNotes:\n{__doc__}\n')
  raise
