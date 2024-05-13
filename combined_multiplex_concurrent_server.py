import socket
import socketserver
import selectors
import json
import threading
import time

from common.bcolors import bcolors
from common.full_write import full_write
from server_side import method_switch

MAXLINE = 256


class MyHandler(socketserver.StreamRequestHandler):
    def handle(self):
        timeval = time.ctime(time.time())
        buffer = f"{timeval}\r\n".encode('utf-8')
        full_write(self.request, buffer)

        host, port = self.client_address
        print(f"Request from host {host}, port {port}")

        while True:
            try:
                data = self.rfile.readline(MAXLINE)
                if not data:
                    print(f"Connection closed by {self.client_address}")
                    break

                print(f"Received from {self.client_address}: {data}")
                data_decoded = data.decode().replace('\n', '')
                data_decoded = json.loads(data_decoded)

                print(f"Parsed Data: {data_decoded}")

                result = method_switch(data_decoded["header"], data_decoded["payload"])
                response = f"{json.dumps(result)}\r\n".encode()

                # Use blocking send to ensure the response is fully sent before closing
                full_write(self.request, response)

            except socket.error as e:
                if e.errno == 10054:
                    print(f"Connection forcibly closed by the remote host {self.client_address}")
                else:
                    print(f"{bcolors.FAIL} Socket Error: {e}{bcolors.ENDC}")
                break
            except Exception as e:
                print(f"{bcolors.FAIL} Generic Exception Error: {e}{bcolors.ENDC}")
                break


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def server_main(server_address, server_port):
    server = ThreadedTCPServer((server_address, server_port), MyHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
    print(f"Server listening on port {server_port}...")

    try:
        server_thread.join()
    except KeyboardInterrupt:
        print("Server terminated by user")


if __name__ == "__main__":
    server_main("127.0.0.1", 1024)