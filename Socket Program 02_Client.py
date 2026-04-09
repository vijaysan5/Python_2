import socket

soc = socket.socket()
print("Waiting for Server")
soc.connect(('127.0.0.1', 12345))
print("Connected. Waiting for Texting...")

# Server send a Msg 1st so, Client Received Server's Msg
data = soc.recv(12345)
print("Received > Server:", data.decode())

# Client Send Replay to Server
soc.send(b"Yes... You are Always Welcome...")

# Server Replay Again so Client Received Server's Replay with Variable
xyz = soc.recv(12345)
print("Received > Server:", xyz.decode())
soc.close()
