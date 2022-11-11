import socketserver


def check_string_of_data(str):
        if "SECRET" in str:
                digitsFound= ""
                for char in str:
                        if char.isdigit():
                                digitsFound = digitsFound + char
                lengthofDigits=len(digitsFound)
                return True, digitsFound, lengthOfDigits
        else:
            return False, "", ""

class MyHandler (socketserver.StreamRequestHandler):
        def handle(self):
                ad=self.request.getpeername( )
                print(ad, "connected to server")
                dataReceived=self.request.recv(1024)
                found, digits, length = check_string_of_data(dataReceived.decode())
                if found:
                        output_result="Digits found are: " + str(digits) + "Count:" + str(length)
                else:
                        output_result="Secret Code not found"
                self.wfile.write(output_result.encode())
                allow_reuse_address = True


HOST = ""
PORT = 5100

server = socketserver.TCPServer((HOST,PORT), MyHandler)
print("Server is Started: ", server)
server.serve_forever()
