# This file will help server recieve the message

import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8080))
server.listen(5)

# server reading the message
while True:
    conn, addr = server.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data.decode('UTF-8','ignore')
        print (from_client)
    conn.close()
    print ('client disconnected')
