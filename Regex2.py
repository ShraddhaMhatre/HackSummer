import re

# ^ symbolizes that string begins with 'Hello'
beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search("Hello World!"))
print(beginsWithHelloRegex.search("He said 'Hello!'"))

# $ symbolizes that string ends with 'World'
endsWithWorldRegex = re.compile(r'World$')
print(endsWithWorldRegex.search('Hello World'))
print(endsWithWorldRegex.search('World is ending'))

#\d is for digits and \w is for words
alldigitsRegex = re.compile(r'^\d+$')
print(alldigitsRegex.search('123456'))
print(alldigitsRegex.search('678x901'))

# '.' matches single character
atRegex = re.compile(r'.at')
#return first occurrence
print(atRegex.search("The cat in hat sat on flat mat"))
#returns a list
print(atRegex.findall("The cat in hat sat on flat mat"))

attwoRegex = re.compile(r'.{1,2}at')
#This returns white spaces as well
print(attwoRegex.search("The cat in hat sat on flat mat"))
print(attwoRegex.findall("The cat in hat sat on flat mat"))

print('First Name: Zee Last Name: TV'.find(':'))
#Slicing
print('First Name: Zee Last Name: TV'[12:])

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
#returns a tuple
print(nameRegex.findall('First Name: Zee Last Name: TV'))

serve = '<To server humans> for dinner>'
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.search(serve))
greedy = re.compile(r'<(.*)>')
print(greedy.search(serve))

prime = 'Serve trust.\nProtect th innocent.\nUpload the law'
print(prime)
# '.'' means any character except new line
dotStar = re.compile(r'.*')
print(dotStar.search(prime))
# 47 characters is limit
dotStarAll = re.compile(r'.*',re.DOTALL)
print(dotStarAll.search(prime))

vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.findall('Al, why does your programming book talk about Robocop so much'))

vowelCaseRegex = re.compile(r'[aeiou]', re.IGNORECASE)
print(vowelCaseRegex.findall('Al, why does your programming book talk about Robocop so much'))

vowelCaseRegex1 = re.compile(r'[aeiou]', re.I)
print(vowelCaseRegex1.findall('Al, why does your programming book talk about Robocop so much'))