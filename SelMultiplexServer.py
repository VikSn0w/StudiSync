import socket
import select
import sys
from common.bcolors import bcolors
from common.full_write import full_write

MAXLINE = 256

def server_main(server_address, server_port):
    list_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    list_fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s_addr = (server_address, server_port)

    try:
        list_fd.bind(s_addr)
        list_fd.listen(10)
    except Exception as e:
        print(f"Error in socket setup: {e}")
        sys.exit(1)

    print(f"Server listening on port {server_port}...")

    fd_open = {list_fd.fileno(): list_fd}
    max_fd = list_fd.fileno()

    while True:
        readable, _, _ = select.select(list(fd_open.keys()), [], [])

        for i in readable:
            if i == list_fd.fileno():
                # New connection
                fd, c_addr = list_fd.accept()
                fd_open[fd.fileno()] = fd
                if fd.fileno() > max_fd:
                    max_fd = fd.fileno()
                print(f"New connection from {c_addr}")
            else:
                # Data on existing connection
                fd = fd_open[i]
                try:
                    data = fd.recv(MAXLINE)
                    print(f"Received from {c_addr}: {data}")
                    if not data:
                        # Closed connection
                        print(f"Connection closed by {fd.getpeername()}")
                        fd.close()
                        del fd_open[i]
                        if max_fd == i:
                            while fd_open[max_fd] == 0:
                                max_fd -= 1
                        continue

                    response = f"{data.decode().replace("\n","")} server".encode()
                    # response = f"{len(data) - 1}\n".encode()
                    if full_write(fd, response):
                        print(f"Error in writing data to {fd.getpeername()}")
                except Exception as e:
                    print(f"{bcolors.FAIL} Error: {e}{bcolors.ENDC}")

if __name__ == "__main__":
    server_main("127.0.0.1",1024)