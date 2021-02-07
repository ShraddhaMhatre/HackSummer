import re

sentence = 'Agent Smith gave roses to Agent Bond.'
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall(sentence))
# sub() replaces the matched pattern with provided string
print(namesRegex.sub('Doctor',sentence))

# (\w) grouping 1st letter of word & consecutive 0 or more letters of word
secretRegex = re.compile(r'Agent (\w)\w*')
print(secretRegex.findall('Agent Smith gave roses to Agent Bond.'))
# \1 is the first letter of group
print(secretRegex.sub(r'Agent \1*****','Agent Smith gave roses to Agent Bond.'))
