from TkiWrapper.Logger import *

class Widget(LogIssuer):
  def __init__(self, frame, sticky):
    self.setIssuerData()
    Debug(self, 'Widget created')
    self.frame = frame
    self.visible = False
    self.alive = True
    self.sticky = sticky

  def show(self):
    if not self.checkAlive(): return
    self.tk.grid(**self.frame.pst.get(self.sticky))
    self.visible = True
    Debug(self, 'Widget shown')

  def hide(self):
    if not self.checkAlive(): return
    self.tk.grid_forget()
    self.visible = False
    Debug(self, 'Widget hidden')

  def toggleVisibility(self):
    if not self.checkAlive(): return
    if self.visible: self.hide()
    else: self.show()

  def delete(self):
    if not self.checkAlive(): return
    self.tk.destroy()
    self.alive = False

  def bind(self, key, callback):
    self.tk.bind(key, callback)

  def isAlive(self):
    '''Alive checker for external use'''
    return self.alive

  def checkAlive(self):
    '''Internal alive checker with auto warn'''
    if not self.alive:
      Warn(self, 'Attempted to call method of a deleted widget')
    return self.alive
