import socket

HOST = "10.10.10.2"
PORT = 5100

s = socket.socket()

s.connect ((HOST, PORT))

output_data_send = input("Enter the input data: ")
s.send(output_data_send.encode())

data_received = s.recv(1024)

s.close()

print("Received Data is:", data_received.decode())
