import socket
import random

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT=1234
HOST_IP = 'localhost'
client.connect((HOST_IP,PORT))

msg=client.recv(2048)
print('messagae: ',msg.decode())
p=13
q=5
a=random.randint(1,p)

client.send(str(p).encode())
print('Modulus is sent (p): ',p)

client.send(str(q).encode())
print('Base is sent (q): ',q)

public=((q**a)%p)
client.send(str(public).encode())
print('Public key is sent to server: ',public)

msg1=client.recv(1028)
print('Public key is received from server: ',msg1.decode())
r=int(msg1.decode())
K=((r**a)%p)
print("The key is : ",K)