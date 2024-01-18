import socket
import time
import sys
from FullWrite import FullWrite
from FullRead import FullRead

def main(ip_address):
    listenfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servaddr = (ip_address, 1024)

    try:
        listenfd.bind(servaddr)
        listenfd.listen(1024)
        print("Server listening on port 1024")

        while True:
            print("Waiting for connection...")
            connfd, _ = listenfd.accept()
            print("Client connected")

            ticks = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            response = f"{'pisnelo'}\r\n"

            FullWrite(connfd, response.encode())
            recvline = FullRead(connfd, 1024)
            if sys.stdout.buffer.write(recvline) == -1:
                sys.stderr.write("fputs error\n")
                sys.exit(1)
            connfd.close()

    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        listenfd.close()

if __name__ == "__main__":
    main("127.0.0.1")
