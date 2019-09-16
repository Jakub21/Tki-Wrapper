from PIL.ImageColor import getrgb as pilHslToRgb
from TkiWrapper.config import conf

class Color:
  def __init__(self, mode, *args, **kwargs):
    self.SETCOLOR = {
      'r': ('r', self.recalcHsl),
      'g': ('g', self.recalcHsl),
      'b': ('b', self.recalcHsl),
      'h': ('hue', self.recalcRgb),
      's': ('sat', self.recalcRgb),
      'l': ('lum', self.recalcRgb),
    }
    self.noColor = False
    if mode is None:
      self.initNoColor()
      return
    method = {
      'RGB': self.rgb, 'HSL': self.hsl, 'STR': self.string
    }[mode]
    method(*args, **kwargs)

  def rgb(self, r, g, b):
    self.r, self.g, self.b = r, g, b
    self.recalcHsl()

  def hsl(self, hue, sat, lum):
    if not conf.CANVAS.COLOR_ENABLE_HSL:
      raise ValueError('Enable config.CANVAS.COLOR_ENABLE_HSL to use this method')
    self.hue, self.sat, self.lum = hue, sat, lum
    self.recalcRgb()

  def string(self, string):
    if len(string) == 4:
      self.r = self.hexToDec(string[1]) * 17
      self.g = self.hexToDec(string[2]) * 17
      self.b = self.hexToDec(string[3]) * 17
      # 17 is not a typo, this makes 4-len strings be able to reach true max
    elif len(string) == 7:
      self.r = self.hexToDec(string[1:3])
      self.g = self.hexToDec(string[3:5])
      self.b = self.hexToDec(string[5:7])
    else:
      raise ValueError('Invalid color string')
    self.recalcHsl()

  def set(self, **kwargs):
    actions = self.SETCOLOR
    for key, amount in kwargs.items():
      try: attrKey, method = actions[key]
      except KeyError:
        raise ValueError(f'Invalid parameter, use [{", ".join(actions.keys())}]')
      self.__dict__[attrKey] = amount
      method()

  def shift(self, **kwargs):
    for key, amount in kwargs.items():
      attrKey = self.SETCOLOR[key][0]
      kwargs[key] = amount + self.__dict__[attrKey]
    self.set(**kwargs)

  def get(self):
    if self.noColor:
      return ''
    r = self.decToHex(self.r)
    g = self.decToHex(self.g)
    b = self.decToHex(self.b)
    return f'#{r}{g}{b}'

  def recalcHsl(self):
    self._limit('r', 0, 255)
    self._limit('g', 0, 255)
    self._limit('b', 0, 255)
    low, high = min(self.r, self.g, self.b), max(self.r, self.g, self.b)
    lum = int((low+high)/5.1)
    try:
      if lum < 50: sat = abs(int((high-low)/(high+low)*100))
      else: sat = abs(int((high-low)/(2-high-low)*100))
    except ZeroDivisionError: sat = 100
    hue = 0
    try:
      if high == self.r: hue = (self.g-self.b)/(high-low)
      elif high == self.g: hue = 2+(self.b-self.r)/(high-low)
      elif high == self.b: hue = 4+(self.r-self.g)/(high-low)
      hue = int(hue * 60)
      if hue < 0: hue += 360
    except ZeroDivisionError: hue = 0
    self.hue, self.sat, self.lum = hue, sat, lum

  def recalcRgb(self):
    self._limit('sat', 0, 100)
    self._limit('lum', 0, 100)
    self.hue %= 360
    hue, sat, lum = int(self.hue), int(self.sat), int(self.lum)
    hslString = f'hsl({hue}, {sat}%, {lum}%)'
    self.r, self.g, self.b = pilHslToRgb(hslString)

  def clone(self):
    clr = Color('RGB', self.r, self.g, self.b)
    clr.noColor = self.noColor
    if conf.CANVAS.COLOR_ENABLE_HSL:
      clr.hue, clr.sat, clr.lum = self.hue, self.sat, self.lum
    return clr

  def initNoColor(self):
    self.noColor = True
    self.r, self.g, self.b = 0, 0, 0
    if conf.CANVAS.COLOR_ENABLE_HSL:
      self.hue, self.sat, self.lum = 0, 0, 0

  def _limit(self, attrKey, _min, _max):
    value = self.__dict__[attrKey]
    if value > _max: value = _max
    if value < _min: value = _min
    self.__dict__[attrKey] = value

  @staticmethod
  def hexToDec(hex):
    hexmap = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    result = 0
    power = len(hex)-1
    for c in hex:
      try: dec = int(c)
      except: dec = hexmap[c]
      result += dec * pow(16, power)
      power -= 1
    return result

  @staticmethod
  def decToHex(dec):
    num = hex(int(dec))[2:].upper()
    if len(num) == 1: num = f'0{num}'
    return num
