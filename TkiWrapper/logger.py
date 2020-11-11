from TkiWrapper.Settings import Settings
from Namespace.Namespace import Namespace
from datetime import datetime

class LogIssuer:
  def setIssuerData(self):
    self.__logIssuerData__ = Namespace(scope = 'tki',
      name = self.__class__.__name__, id = hex(id(self))[2:].upper())
    return self

def printLog(level, issuer, *message):
  if not Settings.enableLogs: return
  time = datetime.now()
  time = time.strftime('%I:%M:%S')
  levels = ['Debug', 'Info', 'Note', 'Warn', 'Error']
  levelNo = levels.index(level)
  if levelNo < levels.index(Settings.logLevel): return
  lvlPrefix = '+'*levelNo + ' '*(4-levelNo)
  try: issuer = issuer.__logIssuerData__
  except:
    print('LOG ISSUER NOT SPECIFIED')
    raise
  print(f'@{time} [{lvlPrefix}] <{issuer.id} {issuer.scope}:{issuer.name}>', *message)

def Debug(issuer, *message):
  printLog('Debug', issuer, *message)

def Info(issuer, *message):
  printLog('Info', issuer, *message)

def Note(issuer, *message):
  printLog('Note', issuer, *message)

def Warn(issuer, *message):
  printLog('Warn', issuer, *message)

def Error(issuer, *message):
  printLog('Error', issuer, *message)
