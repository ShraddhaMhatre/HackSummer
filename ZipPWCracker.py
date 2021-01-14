import zipfile
import optparse
#Zip File Password Cracker
from threading import Thread

def extractFile(zFile,password):
  try:
    #extractall requires bytes
    zFile.extractall(pwd=password)
    print('[+] Password = ',password,"\n")
  except:
    pass

def main():
  parser = optparse.OptionParser("usage%prog -f <zipfile> -d <dictionary>")
  parser.add_option('-f', dest='zname',type='string',help='specify zip file')
  parser.add_option('-d', dest='dname',type='string',help='specify dictionary file')
  (options, args) = parser.parse_args()
  if (options.zname == None) | (options.dname == None):
    print(parser.usage)
    exit(0)
  else:
    zname = options.zname
    dname = options.dname

  zFile = zipfile.ZipFile(zname)
  passFile = open(dname)
  for line in passFile.readlines():
    #string.encode('utf-8') converts str to byte
    password = line.strip('\n').encode('utf-8')
    #guess = extractFile(zFile,password)
    #if guess:
      #print('[+] Password = ',password,"\n")
      #exit(0)
    t = Thread(target=extractFile,args=(zFile,password))
    t.start()
if __name__ == '__main__':
  main()