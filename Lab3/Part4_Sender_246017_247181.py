import socket
import struct

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5005
dest = (MCAST_GRP, MCAST_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)




try:
  while True:
      message = input("Your text : ")
      send = "247181" + message
      sock.sendto(send.encode(), (MCAST_GRP, MCAST_PORT))
except KeyboardInterrupt:
    pass
sock.close()
