import socket
HOST = "tcpip.epfl.ch"
PORT = 5003

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))
message = "CMD_short:0"
sock.sendall(message.encode())
while True:
    data = sock.recv(18).decode()

    if data:
        print(data)
    else:
        break
sock.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))
message = "CMD_short:1"
sock.sendall(message.encode())
while True:
    data = sock.recv(18).decode()

    if data:
        print(data)
    else:
        break
sock.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))
message = "CMD_floodme"
sock.sendall(message.encode())
i = 0
while True:
    data = sock.recv(2000).decode()
    if data:
        print(data)
    else:
        break
sock.close()
