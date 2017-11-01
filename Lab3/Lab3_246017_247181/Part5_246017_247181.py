import websocket
host = "ws://tcpip.epfl.ch:5006"

ws = websocket.WebSocket()
ws.connect(host)
#ws.send("CMD_short:0")
#ws.send("CMD_short:1")
ws.send("CMD_floodme")
while True:
    res = ws.recv()
    if res:
        print(res.decode())
    else:
        break
ws.close()
