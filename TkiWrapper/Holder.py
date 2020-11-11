
class Holder:
  def __init__(self):
    self.slaves = {}

  def addSlave(self, point, slave):
    self.slaves[f'{point.x}_{point.y}'] = slave

  def getSlave(self, point):
    return self.slaves[f'{point.x}_{point.y}']

  def delSlave(self, point):
    del self.slaves[f'{point.x}_{point.y}']
