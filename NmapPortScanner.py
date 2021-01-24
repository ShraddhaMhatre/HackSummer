#!/usr/bin/env python3

#Run this code in a machine where nmap is installed (e.g. Kali). Check if nmap is set in PATH. You need uninstall nmap and install python-nmap
#python -m pip uninstall nmap
#python3 -m pip install python-nmap (instead of nmap)

import optparse
import nmap

#This method performs nmap scan using host, port
def nmapScan(tgtHost,tgtPort):
  nmScan = nmap.PortScanner()
  nmScan.scan(tgtHost,tgtPort)
  
  #extracting state from indexed operations: state = tgtHost(tcp(tgtPort(state)))
  #t1 = nmScan[tgtHost]
  #t2 = t1['tcp']
  #t3 = t2[int(tgtPort)]
  #state = t3['state']
  state=nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
  print(" [*] "+tgtHost+" tcp/"+tgtPort+" "+state)

#This methods uses OptParse to take input (hostname, port(s)) and calls nmapScan method
def main():
  parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
  parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
  parser.add_option('-p',dest='tgtPort',type='string',help='specify target port[s]separated by comma')
  (options, args) = parser.parse_args()
  tgtHost = options.tgtHost
  tgtPorts = str(options.tgtPort).split(",")
  if (tgtHost == None) | (tgtPorts[0] == None):
    print(parser.usage)
    exit(0)
  for tgtPort in tgtPorts:
    nmapScan(tgtHost,tgtPort)

if __name__ == '__main__':
  main()