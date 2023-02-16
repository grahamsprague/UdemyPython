

import re

pattern = re.compile(r"([a-zA-Z0-9@#%$]{8,}\d)")

string = 'mYtes12345t@#%' # match
# string = 'mYtes12345t@#%!!!!(*&^&(*&))' # no match

a = pattern.search(string)

if  a != None:
    print(string + ' is a good password.')
else:
    print(string + 'does not meet the requirements. (Must be at least 8 char in length.)')

print(a)