import socket
import os

divider= "|"

HOST = "10.10.10.2"
PORT = 5100

name_of_file = "1.txt"

s=socket.socket()

print(f"==> Initiating a Connection to {HOST}:{PORT}")
s.connect((HOST,PORT))
print(f"==> Connected: ")
s.send(f"{name_of_file}{divider}".encode())

with open(name_of_file,"rb") as f:
         while l:
                bytes_to_written=f.read(128)
                if not bytes_to_written:
                        break
                s.send(bytes_to_written)

s.close()
