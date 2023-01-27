# Find Duplicates

some_list = ['a','b','c','b','d','m','n','n']
some_list.sort()
compare_str = ''

for item in some_list:
  if item != compare_str:
    compare_str = item
  else:
    print(item)

