import re

# Below is greedy match i.e. match longest possible string
# haRegex = re.compile(r'(Ha){3,5}')
# mo3 = haRegex.search('He said "HaHaHaHaHa"')
# print(mo3.group())

# Adding '?' creates non-greedy match i.e. match shortest string
haRegex = re.compile(r'(Ha){3,5}?')
mo3 = haRegex.search('He said "HaHaHaHaHa"')
print(mo3.group())

# moRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
# mo1 = moRegex.search('123-456-7890,234-567-8901,345-5678-8901')
# print(mo1.group()== None)

# # ? matches 0 or 1
# regexVar = re.compile(r'Bat(wo)?man')
# mo = regexVar.search('This is a Batwoman')
# print(mo.group())
# mo1 = regexVar.search('This is a Batwowowowowowowoman')
# print(mo1 == None)

# # * matches 0 or more
# regexVar1 = re.compile(r'Bat(wo)*man')
# mo2 = regexVar1.search('This is a Batwowowowowowowoman')
# print(mo2.group())

# regexVar = re.compile(r'\+\?\*')
# mo = regexVar.search('This is +?*')
# print(mo.group())

# # + matches 1 or more
# regexVar1 = re.compile(r'(\+\?\*)+')
# mo1 = regexVar1.search('This is +?*+?*9+?*+?*+?*+?*+?*+?')
# print(mo1.group())

# # {Count} of pattern expected
# haRegex = re.compile(r'(Ha){3}')
# mo2 = haRegex.search('He said "HaHaHa"')
# print(mo2.group())

