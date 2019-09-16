from TkiWrapper.viewCore import ViewCore

class View(ViewCore):
  '''View to place in main frame'''
  def __init__(self, root, key, slot, positioner=None, showKey=None):
    super().__init__(root, key, slot, positioner)
    if showKey is not None:
      self.root.root.bind(showKey, lambda evt: self.root.show(self.key))

  def changeSlot(self, slot):
    if self.shown:
      raise Exception('Only can change view\'s slot when it is not shown')
    self.viewType = slot


class HeaderView(ViewCore):
  '''View to use as header'''
  def __init__(self, root, key, positioner=None):
    super().__init__(root, key, 'h', positioner)
    self.show()


class FooterView(ViewCore):
  '''View to use as footer'''
  def __init__(self, root, key, positioner=None):
    super().__init__(root, key, 'f', positioner)
    self.show()
