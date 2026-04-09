import socket

soc = socket.socket()

try:
    soc.connect(('localhost', 12354))
    print("Connecting with Server >>> Successfully...!")
    print("Received:", soc.recv(1024).decode())
except Exception as end:
    print("Is not Connect :", end)
finally:
    soc.close()

input("Press Enter to exit...")