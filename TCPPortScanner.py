# Input a hostname, CSV of ports to scan
import optparse
import socket
import threading
from threading import *

def main():
  parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
  parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
  parser.add_option('-p',dest='tgtPort',type='string',help='specify target port[s]separated by comma')
  (options, args) = parser.parse_args()
  tgtHost = options.tgtHost
  tgtPorts = str(options.tgtPort).split(",")
  if (tgtHost == None) | (tgtPorts[0] == None):
    print("[-] You must specify a target host and port[s].")
    exit(0)
  portScan(tgtHost,tgtPorts)

screenLock = threading.Semaphore(1)
#Connect to target addr & specific port
def connScan(tgtHost,tgtPort):
  try:
    connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connSkt.connect((tgtHost, tgtPort))
    #Determine specific service running on port, send garbage data, read app banner
    connSkt.send("ViolentPython3\r\n")
    results = connSkt.recv(100)
    screenLock.acquire()
    print("[+] tcp open",tgtPort)
    print("[+]",str(results))
  except:
    screenLock.acquire()
    print("[-] tcp closed",tgtPort)  
  finally:
    screenLock.release()
    connSkt.close()

#Translate hostname into IPv4 addr
def portScan(tgtHost,tgtPorts):
  try:
    #gethostbyname: takes hostname and returns IP addr
    tgtIP = socket.gethostbyname(tgtHost)
  except:
    print("[-] Cannot resolve '%s': Unknown host",tgtHost)
    return
  try:
    tgtName = socket.gethostbyaddr(tgtIP)
    print("\n[+] Scan results for: ",tgtName[2])
  except:
    print("\n[+] Scan results for: ",tgtIP)
  socket.setdefaulttimeout(1)
  for tgtPort in tgtPorts:
    t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
    t.start()
    #connScan(tgtHost,int(tgtPort))

if __name__ == '__main__':
  main()