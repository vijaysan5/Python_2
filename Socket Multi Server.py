import socket

soc = socket.socket()
soc.bind(('localhost', 12354))
soc.listen(2)
print("Listening...")

while True:
    con, add = soc.accept()
    print(f"Connection is Successfully! {add}")
    con.send(b"Hey... Thank you for Bind with this Server...")
    con.close()
 
