import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost',1546465465))
s.listen()

conn, addr = s.accept()
data = conn.recv(1024)
conn.sendall('Message for client'.encode())

