import socket
import os
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s', ifname[:15])
    )[20:24])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(0.5)

try:
    get_ip_address('eth0:1')
    print "get it"
except Exception, e:
    try:
        s.connect(('192.168.1.11', 3306))
        os.system('sudo ifconfig eth0:1 192.168.1.10 up')
    except Exception, ee:
        print "Cannot connect to 1.11"
    print "Cannot found eth0:1"
