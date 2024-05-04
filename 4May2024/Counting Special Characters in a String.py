import re

str1 = "%^$&%^"

count = re.sub('[\w]+','',str1)
print(len(str1))

