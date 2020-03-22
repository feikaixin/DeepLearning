
from datetime import datetime
class Student(object):

  def __init__(self):
    super().__init__()
    self._score = None

  @property
  def score(self):
    return self._score
  
  @score.setter
  def score(self, value):
    if not isinstance(value, int):
      raise ValueError('score must be an integer!')
    if value < 0 or value > 100:
      raise ValueError('score must between 0 ~ 100!')
    self._score = value
  
s = Student()
s._score = 60
print(s._score)

# 不带参数的装饰器
def log(func):
  def wrapper(*awg, **kw):
    if not callable(func):
      raise ValueError('function')
    print(func.__name__)
    return func()
  return wrapper

# 带参数的装饰器
def log(level):
  def wrapper(func):
    def inner_wrapper(*awg, **kw):
      if not callable(func):
        raise ValueError('function')
      print(func.__name__)
      print(level)
      return func()
    return inner_wrapper
  return wrapper
@log(level=1)
def now():
  print(datetime.now())

now()
