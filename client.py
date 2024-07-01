import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost', 1546465465))
s.send("Hola, servidor".encode())
response = s.recv(1024).decode()