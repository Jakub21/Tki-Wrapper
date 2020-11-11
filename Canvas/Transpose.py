from TkiWrapper.Point import Point

class Transpose:
  def __init__(self, tx, ty, sx, sy):
    # t = translate, s = scale
    self.tx = tx; self.ty = ty; self.sx = sx; self.sy = sy
    self.get = self._getContain
    self.bounds = None
    self.mode = None
    self.cvsSize = None
    self.anchor = None

  def setElemSpaceBounds(self, bounds):
    self.bounds = bounds

  def setMode(self, mode):
    self.mode = mode

  def setRealSize(self, size):
    self.cvsSize = size

  def setAnchorMode(self, mode):
    self.anchor = mode

  def get(self, point):
    if None in [self.bounds, self.mode, self.cvsSize]:
      raise ValueError('[CanvasTranspose] Must set bounds, mode and real size first')
    return Namespace(
      contain = self._setModeContain,
      fill = self._setModeFill,
      stretch = self._setModeStretch,
    )[self.mode](point)

  def _getContain(self, point):
    scale = self._calcScale(min)
    anchor = self._calcAnchor(self.cnvSize, scale)
    return anchor, scale

  def _getStretch(self, point):
    scale = self._calcScale(max)
    anchor = self._calcAnchor(self.cnvSize, scale)
    return anchor, scale

  def _getFill(self, point):
    scale = Point(self.cnvSize.x/self.bounds.x, self.cnvSize.y/self.bounds.y)
    anchor = Point(0, 0)
    return anchor, scale

  def _calcScale(self, comprator):
    '''Helper method for _getContain and _getStretch'''
    cnvSize = self._getSize()
    xScale = cnvSize.x / self.bounds.x
    yScale = cnvSize.y / self.bounds.y
    scale = comprator(xScale, yScale)
    return Point(scale, scale)

  def _calcAnchor(self, cnvSize, scale):
    '''Helper method for _getContain and _getStretch'''
    if self.anchor == 'ul':
      x, y = 0, 0
    elif self.anchor == 'center':
      x = (cnvSize.x - scale.x * self.bounds.x) / 2
      y = (cnvSize.y - scale.y * self.bounds.y) / 2
    return Point(x, y)

  # def reversed(self, point): # TODO
  #   anchor, scale = self.get(point)
