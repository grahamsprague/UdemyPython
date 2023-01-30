
def highest_even(mylist):

  mylist.sort()
  mylist.reverse()

  for item in mylist:

    if item % 2 == 0:
      return item
      break

print(highest_even([10,1,2,3,4,11]))