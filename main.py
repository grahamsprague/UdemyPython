
# extend list
class Superlist(list):
  # override len
  def __len__(self):
    return 1000;

#make a new superlist
super_list = Superlist([1,2,3,4,5,6,7])

#call len
print(super_list.__len__())