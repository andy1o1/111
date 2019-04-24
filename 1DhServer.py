import socket
import random

server=socket.socket()
PORT=1234
server.bind(('',PORT))
server.listen(5)
print("server strated ....")

conn,addr=server.accept()
conn.send('Serevr is listening'.encode())

msg1=conn.recv(1048)
print("Modulus is received (p) : ",msg1.decode())

msg2=conn.recv(1048)
print("Base is received (q) : ",msg2.decode())
p=int(msg1)
q=int(msg2)
b=random.randint(1,p)

msg3=conn.recv(1048)
print("Public key is received from client : ",msg3.decode())
s=int(msg3.decode())

public1=((q**b)%p)
conn.send(str(public1).encode())
print("Public key is sent to client : ",public1)
K=((s**b)%p)
print("The key is : ",K)
