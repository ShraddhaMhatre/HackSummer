import pprint

message = 'Mr. and Mrs. Dursley of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much.'
count = {}
for character in message.upper():
  count.setdefault(character,0)
  count[character] = count[character] + 1

#pprint.pprint(count)
stringText = pprint.pformat(count)
print(stringText)