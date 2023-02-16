

import re

pattern = re.compile(r"([a-zA-Z0-9@#%$]{8,}\d)")

string = 'mYtes12345t@#%' # match
# string = 'mYtes12345t@#%!!!!(*&^&(*&))' # no match

a = pattern.fullmatch(string)

if  a != None:
    print(string + ' is a good password.')
else:
    print(string + 'does not meet the requirements. (Can contain a-Z 0-9 @#$% and must be at least 8 char in length and end with a number.)')

print(a)