from functools import reduce

#zip
#filter
#map
#reduce


#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def my_cap(item):
  return item.capitalize()

print(list(map(my_cap, my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, my_numbers)))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def above_50_only(item):
  return item > 50

print(list(filter(above_50_only, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

my_numbers.extend(scores)

print(my_numbers)

def accumulator(acc, item):
  return acc + item

print(reduce(accumulator, my_numbers, 0))
