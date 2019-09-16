
def Dict(**kwargs):
  return kwargs

class Namespace:
  '''Converts dictionaries to namespaces'''
  def __init__(self, className=None, **data):
    self.__dict__.update(data)
    if className is not None:
      self.__NSclassName__ = className

  @classmethod
  def fromDict(cls, input_dict):
    obj = cls.__new__(cls)
    obj.__dict__.update(input_dict)
    return obj

  @classmethod
  def recursive(cls, **data):
    obj = cls.__new__(cls)
    for k, v in data.items():
      if type(v) is dict:
        v = cls.recursive(v)
      obj.__dict__.update({k:v})
    return obj

  def toString(self, indent=0, className='Namespace'):
    if className != 'dict': className = f'<{className}>'
    result = className + ' {\n'
    self.__repr_indent__ = indent
    def convertPrimitive(x):
      if type(x) == str:
        x = '"'+x+'"'
      return str(x)
    def convertDict(x):
      return Namespace(x).toString(self.__repr_indent__+1, 'dict')
    def convertList(x):
      if len(x) == 0: return '[]'
      else:
        self.__repr_indent__ += 1
        r = '['
        for xx in x: r += '\n' + ' '*4*(self.__repr_indent__+1) + choice(xx)
        r += '\n'+' '*4*self.__repr_indent__+']\n'
        self.__repr_indent__ -= 1
        return r
    def convertObject(x):
      return Namespace(**x.__dict__).toString(self.__repr_indent__+1, x.__class__.__name__)
    def convertClass(x):
      return f'<|Class {x.__name__}|>'
    def choice(x):
      if type(x) in [int, str, float, bool]:
        return convertPrimitive(x)
      elif type(x) == dict:
        return convertDict(x)
      elif type(x) == list:
        return convertList(x)
      elif 'object at' in str(x):
        return convertObject(x)
      elif type(x) == type(list): # class (not instance)
        return convertClass(x)
    for k, v in self.__dict__.items():
      if k == '__repr_indent__': continue
      result += ' '*4*(self.__repr_indent__+1) + str(k) + ': ' + str(choice(v)) + '\n'
    result += ' '*4*self.__repr_indent__ + '}'
    del self.__repr_indent__
    return result
