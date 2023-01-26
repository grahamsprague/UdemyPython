#Scroll down to see the answers!
#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

user_profile = {
  'username': 'yimmy',
  'age': 85,
  'weapons': ['axe', 'bat'],
  'is_active': True,
  'clan': 'Fail for Effect'
}
print('---new user profile---')
print(user_profile)
print('')

#2 iterate and print all the keys in the above user.
print('---keys---')
for item in user_profile:
  print(item)
print('')


#3 Add a new weapon to your user
print('new weapon added')
user_profile['weapons'].insert(0,'golf club')
print(user_profile['weapons'])
print('')
#4 Add a new key to include 'is_banned'. Set it to false

user_profile['is_banned'] = False

print('---is_banned added---')
print(user_profile)
print('')

#5 Ban the user by setting the previous key to True

user_profile['is_banned'] = True
print('---user is banned---')
print(user_profile)
print('')
#6 create a new user2 my copying the previous user and update the age value and username value.

user_profile2 = user_profile.copy();
user_profile2['username'] = 'hoat gerder'
user_profile2['age'] = 45
user_profile2['is_banned'] = False #not fair to ban a new player

print('---new user created---')
print(user_profile2)
print('')


