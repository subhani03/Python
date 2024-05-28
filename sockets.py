'''import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=16789
s.bind((host,port))
s.listen(5)
while True:
    c,addr=s.accept()
    print('got connection from',addr)
    s1="thanks for connecting"
    c.send(s1.encode())
    c.close()'''
#workout
import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=12345
s.bind((host,port))
s.listen(2)
while True:
    c,addr=s.accept()
    print('got connection from',addr)
    s1="The best way to predict the future that's create it"
    c.send(s1.encode())
    c.close()