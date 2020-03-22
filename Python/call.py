class People:
  def __init__(self, a, b):
    self.a = a
    self.b = b
  
  def __call__(self):
    print("__call__ with {}, {}".format(self.a, self.b))

a = People("费", "开")
a()