'''import socket 
s=socket.socket()
host=socket.gethostname()
port=16789
s.connect((host,port))
a=s.recv(1024)
print(a.decode()+"I am a client")
s.close()'''
#workout
import socket
s=socket.socket()
host=socket.gethostname()
port=12345
s.connect((host,port))
a=s.recv(1024)
print(a.decode())
s.close()