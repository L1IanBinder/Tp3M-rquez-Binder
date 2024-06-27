import socket

import socket

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address and port
s.bind(('localhost', 12345))

print("UDP server is up and listening on port 12345")

while True:
    # Receive data from the client (1024 bytes)
    data, addr = s.recvfrom(1024)
    print(f"Received message from {addr}: {data.decode()}")

    # Send a response back to the client
    response = "Message for client".encode()
    s.sendto(response, addr)

    print(response)
