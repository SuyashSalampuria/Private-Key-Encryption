import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8082))

file2 = open('var2.txt')
msg = file2.read()

client.send(str(msg).encode())
# client.send(str(binary).encode())

from_server = client.recv(4096)
client.close()

