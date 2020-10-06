import re

message = 'Call me 415-555-1011 tomorrow  or at 415-555-9999'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#Below searches for the first occurence of the regex
#mo = phoneNumRegex.search(message)
#print(mo.group())

#Below prints for all occurences of regex
# findall() returns a list
print(phoneNumRegex.findall(message))