def special_for(iterable):
  iterator = iter(iterable)
  while True:
    try:
      iterator*5
      next(iterator)
    except StopIteration:
      break


class MyGen:
  counter = 0
  current = 0
  previous = 0

  def __init__(self, first):
    self.first = first


  def __iter__(self):
    return self

  def __next__(self):

    # make sure we are under the given value threshold
    if MyGen.counter < self.first:

      # need to kick start by setting to 1 on second pass.
      if MyGen.counter > 0 and MyGen.current == 0:
        MyGen.current += 1

      # increment and calculate
      MyGen.counter += 1
      result = MyGen.previous + MyGen.current
      MyGen.previous = MyGen.current
      MyGen.current = result

      return result
    raise StopIteration

gen = MyGen(20)
for i in gen:
    print(i)