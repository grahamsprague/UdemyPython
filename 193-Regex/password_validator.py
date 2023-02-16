

import re

pattern = re.compile(r"([a-zA-Z0-9]+\@*\#*\%*\$*$)")

string = 'mYtes12345t@#%' # match
# string = 'mYtes12345t@#%!!!!(*&^&(*&))' # no match

a = pattern.search(string)

print(a)