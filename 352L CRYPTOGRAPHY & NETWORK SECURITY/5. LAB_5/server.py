import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5996))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    msg_rec=clientsocket.recv(1024)
    msg=msg_rec.decode("utf-8")
    print("Message recieved: " + msg)
    M_R=(int(msg)**536827)%807043
    print("Decrypted Message:", M_R)
