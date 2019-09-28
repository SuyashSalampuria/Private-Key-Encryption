import socket


P=1000000007
G=44654584
a=4

Priv_key1=pow(G,a,P)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8081))

client.send(str(Priv_key1).encode())
# client.send(str(binary).encode())

from_server = client.recv(4096)
client.close()
#print (from_server.decode('UTF-8','ignore'))

Secret_key1=pow(int(from_server),a,P)
print (Secret_key1)

