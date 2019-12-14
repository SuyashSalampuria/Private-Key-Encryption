import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8080))

# reading the  message to send it
msg_file = open('var2.txt')
msg = msg_file.read()

client.send(str(msg).encode())

from_server = client.recv(4096)
client.close()

