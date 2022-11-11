import socketserver
import os

divider = "|"

class MyHandler(socketserver.BaseRequestHandler):
        def handle(self):
                ad=self.request.getpeername()
                print (ad, "connected")
                getData=self.request.recv(1024).decode()
                name_of_file,data = getData.split(divider)
                name_ of_file = os.path.basename(name_of_file)
                with open(name_of_file,"wb") as f:
                        f.write(data.encode())
                        print("Received and written in file:", name_of_file)
                allow_reuse_address = True

HOST = ""
PORT = 5100
server = socketserver.TCPServer((HOST,PORT), MyHandler)
print("Started the server:", server)
server.serve_forever()
