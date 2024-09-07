import socket
import sys

# Create a socket
s = socket.socket()

# Define the port on which you want to connect
port = 80

# Connect to the server
s.connect(('localhost', port))

# Send some data
s.send(b'GET / HTTP/1.0\r\n\r\n')

# Receive some data
response = s.recv(4096)

# Print the received data