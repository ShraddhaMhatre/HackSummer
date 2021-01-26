#Pexpect has the ability to interact with programs, watch for expected o/p and respond based on expected o/p

import pexpect
PROMPT = ['# ','>>> ','> ','\$ ']

#Sends command to SSH session
def send_command(child, cmd):
  child.sendline(cmd)
  #waits for the session
  child.expect(PROMPT)
  #after catching the cmd prompt, prints o/p from SSH session
  print(child.before)

#Returns an SSH connection 
def connect(user, host, password):
  ssh_newkey = 'Are you sure you want to continue connecting'
  connStr = 'ssh ' + user + '@' + host
  #resulting in an SSH spawned connection
  child = pexpect.spawn(connStr)
  #3 expected o/p; Timeout, a msg indicating that the host has a new public key, password prompt
  ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
  #if Timeout
  if ret == 0:
    print("[-] Error connecting")
    return
  #if ssh_newkey message
  if ret == 1:
    #send 'yes' to accept new key
    child.sendline('yes')
    #Loop B: 2 expected o/p; Timeout, password prompt
    ret = child.expect([pexpect.TIMEOUT,'[P|p]assword:'])
    #if Timeout
    if ret == 0:
      print("[-] Error connecting")
      return
 #handles original if ret == 2 and the #B's if ret == 1
 child.sendline(password)
  child.expect(PROMPT)
  return child

def main():
  host = 'localhost'
  user = 'root'
  password = 'toor'
  child = connect(user, host, password)
  send_command(child, 'whoami')

if __name__ == '__main__':
  main()