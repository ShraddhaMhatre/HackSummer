#Python script to copy from one file to another
#usage: python main.py test.txt new_file.txt
from sys import argv
from os.path import exists

script, from_file, to_file = argv
print("Copying from %s to %s" %(from_file, to_file))

in_file = open(from_file)
indata = in_file.read()
print("Input file is %s bytes long." %(len(from_file)))

print("Does the output file exists? %r" %exists(to_file))
print("Ready, hit RETURN to continue, CTRL+C to abort.")
input()

out_file = open(to_file,'w')
out_file.write(indata)

print("Alright, all done.")
out_file.close()
in_file.close()