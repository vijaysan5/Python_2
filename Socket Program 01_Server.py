
import socket
soc  = socket.socket()
#Bind IP Add >>> Insted of IP Add === type > "localhost"
soc.bind(('127.0.0.1', 12345))
soc.listen(1)
print("Listening...")

# Accepting
code, address = soc.accept()
print("Connect from", address)

# Sending Msg to Client
code.send(b"Hey... Thank you for this connection")

# Receiving Replay >>> Client
abcd = code.recv(12345)
print("Received > Client:", abcd.decode())

# Again Sending Replay to Client
code.send(b"yeah!")

code.close()
soc.close()

