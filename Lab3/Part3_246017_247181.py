import socket

def clientUDP():
    HOST = 'lab3.iew.epfl.ch'
    PORT = 5004
    dst = (HOST, PORT)

    message = b'RESET:20'
    c4 = 0
    c6 = 0
    n4 = 0
    success = False
    while(not success):
        s4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        success = sendWithTimeout(s4,dst,message,1)
        s4.close()
        c4 += 1

        if(not success):
            s6 = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
            success = sendWithTimeout(s6,dst,message,1)
            s6.close()
            c6 += 1
        else :
            n4 = 1
    return n4, (c4 if(n4 == 1) else c6)

def sendWithTimeout(s, destination, message, timeout):
    try:
        s.sendto(message, destination)
        s.settimeout(timeout)
        data, addr = s.recvfrom(200)
        # print(data.decode())
        return True
    except socket.timeout:
        return False

def try60():
    summ =  0
    s4 = 0
    for i in range(60):
        print(i)
        n4,c = clientUDP()
        summ += c
        s4 += n4
    print("ipv4 : ", s4, "mean : ", summ/60.0)

try60()
