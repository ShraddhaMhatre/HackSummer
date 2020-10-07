import re

#message = 'Call me 415-555-1011 tomorrow  or at 415-555-9999'
#Below paranthesis group the number as group1 for area code and group 2 for rest
#phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#mo = phoneNumRegex.search(message)
#print(mo.group())

message = 'Call me (415) 555-1011 tomorrow  or at (415) 555-9999'
#Below \(\) returns area code
phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())

#pipe can match one of many possible groups
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
bat = batRegex.search('Batmobile lost a wheel')
print(bat.group())