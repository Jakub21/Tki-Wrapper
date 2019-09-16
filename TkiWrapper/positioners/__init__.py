from TkiWrapper.namespace import Dict
from TkiWrapper.positioners.grid import Grid

class Register:
  positioners = Dict(
    Grid = Grid,
  )

  @classmethod
  def get(cls, key):
    return cls.positioners[key]

  @classmethod
  def add(cls, key, positioner):
    try:
      cls.positioners[key]
      raise Exception('There is already positioner assigned to this key')
    except KeyError:
      cls.positioners[key] = positioner
