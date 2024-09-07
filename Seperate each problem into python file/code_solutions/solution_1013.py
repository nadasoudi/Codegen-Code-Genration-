import socket

def send_request(url):
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the server
    s.connect((url, 80))
    # send the request
    s.send(url.encode())
    # receive the response
    response = s.recv(1024)
    # close