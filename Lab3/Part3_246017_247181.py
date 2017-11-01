import socket

def clientUDP():
    HOST = 'lab3.iew.epfl.ch'
    PORT = 5004
    # The remote host
    #port number of communicating partner
    message = b'Reset:20'
    s4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s4.sendto(message, (HOST,PORT) )
    s4.close()
    s6 = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    s6.sendto(message, (HOST,PORT) )
    s6.close()

clientUDP()
