import socket
import sys
import asyncio
from common.bcolors import bcolors
from common.full_write import full_write

MAXLINE = 256

async def read_input(filein, sock):
    while True:
        data = await asyncio.to_thread(filein.readline)
        if not data:
            break
        await asyncio.to_thread(full_write, sock, data.encode())

async def read_socket(sock):
    while True:
        recvbuff = await asyncio.to_thread(sock.recv, MAXLINE)
        if not recvbuff:
            print(f"{bcolors.WARNING}EOF on the socket{bcolors.ENDC}")
            break
        sys.stdout.buffer.write(recvbuff)
        sys.stdout.flush()

async def client_echo(filein, sock):
    await asyncio.gather(
        read_input(filein, sock),
        read_socket(sock)
    )

if __name__ == "__main__":

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serv_add = ("127.0.0.1", 1024)

    try:
        sock.connect(serv_add)
        print(f"{bcolors.OKGREEN}Connection to {serv_add} established!{bcolors.ENDC}")
    except Exception as e:
        print(f"{bcolors.FAIL}Connection error: {e}{bcolors.ENDC}")
        sys.exit(1)

    print("Writing I/O")
    asyncio.run(client_echo(sys.stdin, sock))