#Unix Password Cracker
import crypt

def testPass(cryptPass):
  salt = cryptPass[0:2]
  docFile = open('dictionary.txt','r')

  for word in docFile.readlines():
    word = word.strip('\n')
    cryptWord = crypt.crypt(word,salt)
    if (cryptWord == cryptPass):
      print("[+]Found password: ",word,"\n")
      return
  print("[-] Password not found.\n")
  return


def main():
  passFile = open('passwords.txt','r')
  for line in passFile.readlines():
    if ":" in line:
      user = line.split(':')[0]
      cryptPass = line.split(':')[1].strip('\n')
      print("[*] Cracking password for: ",user)
      testPass(cryptPass)

if __name__ == "__main__":
  main()