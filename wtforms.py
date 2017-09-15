class Car(object):
  def __init__(self, name):
    self.name = name

  @classmethod
  def save(cls, name):
    return cls(name=name)

def main():
  c = Car.save('ebby')
  print 'name'
  print c.name


if __name__ == '__main__':
  main()