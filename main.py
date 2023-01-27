


def checkDriverAge(age = 0):
  if age == '':
    return "You failed to specify an age, so you cannot drive." # I decided an age of 0 makes no sense so I informed the user they failed to enter an age.
  elif int(age) < 18:
  	return "Sorry, you are too young to drive this car. Powering off"
  elif int(age) > 18:
  	return "Powering On. Enjoy the ride!";
  elif int(age) == 18:
  	return "Congratulations on your first year of driving. Enjoy the ride!"

my_age = input("What is your age?: ")
print(checkDriverAge(my_age))



#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.