is_magician = True
is_expert = False


if (is_magician and is_expert):
  print('You are a magician.')
elif(is_magician and not(is_expert)):
  print('At least you are getting there.')
elif(not(is_magician)):
  print('You need magic powers.')