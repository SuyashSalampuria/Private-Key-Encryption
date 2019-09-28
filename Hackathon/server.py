import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8081))
serv.listen(5)

P=1000000007
b=2
G=44654584
Priv_key2=pow(G,b,P)
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data.decode('UTF-8','ignore')
        # print (from_client)
        conn.send(str(Priv_key2).encode())
        Secret_key2=pow(int(from_client),b,P)
        print (Secret_key2)
    conn.close()
    print ('client disconnected')
