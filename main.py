

#Square

mylist = [5,4,3]

print(list(map((lambda item: item**2), mylist)))


#list sorting by second item

a = [(0,2),(4,3), (10,-1), (9,9)]

print(a)

#change the default key to the second index[1]
a.sort(key=lambda x: x[1])

print(a)