import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8082))
serv.listen(5)


while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data.decode('UTF-8','ignore')
        print (from_client)
    conn.close()
    print ('client disconnected')
