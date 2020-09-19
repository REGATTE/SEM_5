import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5996))

#server_msg=s.recv(1024)
#print(server_msg.decode("utf-8"))
import random
M=random.randint(1,807043)
C=(M**3)%807043
print("Original Message: ",M,"Encrypted message:",C)
s.send(bytes(str(C),"utf-8"))

