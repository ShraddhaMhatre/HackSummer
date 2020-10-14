import re

# moRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
# mo = moRegex.findall("THis is the number 415-567-7890 and that is also the number 567-457-6789")
# #Below returns list of tuples
# print(mo)

#Character classes

# lyrics = "12 Drummers Drumming, 11 Pipers Piping, 10 Lords a Leaping, 9 Ladies Dancing, 8 Maids a Milking, 7 Swans a Swimming, 6 Geese a Laying, 5 Golden Rings, 4 Calling Birds, 3 French Hens, 2 Turtle Doves and 1 Partridge in a Pear Tree"
# xmasRegex = re.compile(r'\d+\s\w+')
# print(xmasRegex.findall(lyrics))

# vowelRegex = re.compile(r'[aeiouAEIOU]')
# print(vowelRegex.findall('Shahrukh Khan is a good actor'))

# doublevowelRegex = re.compile(r'[aeiouAEIOU]{2}')
# print(doublevowelRegex.findall('Mailaika Arora and her yoga fitness'))

consonantsRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantsRegex.findall('Hrithik is greek god'))