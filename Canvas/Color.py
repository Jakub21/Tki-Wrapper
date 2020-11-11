from PIL.ImageColor import getrgb as pilHslToRgb

class BaseColor:
  @staticmethod
  def decToHex(dec):
    num = hex(int(dec))[2:].upper()
    return num if len(num) == 1 else f'0{num}'

  def makeHex(self, r, g, b):
    r = self.decToHex(r)
    g = self.decToHex(g)
    b = self.decToHex(b)
    return f'#{r}{g}{b}'


class HexColor(BaseColor):
  def __init__(self, hex):
    self.hex = hex

  def getHex(self):
    return self.hex


class RgbColor(BaseColor):
  def __init__(self, r, g, b):
    self.r = r
    self.g = g
    self.b = b

  def getHex(self):
    return self.makeHex(self.r, self.g, self.b)


class HslColor(BaseColor):
  def __init__(self, h, s, l):
    self.h = h
    self.s = s
    self.l = l

  def getHex(self):
    self.hue %= 360
    hue, sat, lum = int(self.hue), int(self.sat), int(self.lum)
    hslString = f'hsl({hue}, {sat}%, {lum}%)'
    return self.makeHex(*pilHslToRgb(hslString))
