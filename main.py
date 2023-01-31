#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def findOldest(cats):

      # init a storage for oldest cat
      max_cat = None
      for mycat in cats:
        # on the first pass max_cat will be empty and error on age compare
        if max_cat == None:
          max_cat = mycat
        # grabthe older and store it
        if mycat.age > max_cat.age:
          max_cat = mycat
      
      return max_cat
      
      
        

# 1 Instantiate the Cat object with 3 cats

cat1 = Cat('Bonkers', 10)
cat2 = Cat('Lucy', 25)
cat3 = Cat('Scooter', 28)

print(cat1)
print(cat2)
print(cat3)

# 2 Create a function that finds the oldest cat
cats = [cat1, cat2, cat3]
old_cat = Cat.findOldest(cats)

print('The oldest cat is ' + str(old_cat.age) + ' years old.')

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2