import socket
import sys
import asyncio
from common.bcolors import bcolors
from common.communication import object_to_json_string, customHash
from common.full_write import full_write
import json

MAXLINE = 256


async def read_input(data, sock):
    # Read strings directly instead of using filein.readline
    while True:
        # Simulate the end of input with an empty string
        if not data:
            break
        await asyncio.to_thread(full_write, sock, data.encode())
        # Break out of the loop after writing the data
        break


async def read_socket(sock):
    while True:
        recvbuff = await asyncio.to_thread(sock.recv, MAXLINE)
        if not recvbuff:
            print(f"{bcolors.WARNING}EOF on the socket{bcolors.ENDC}")
            break
        sys.stdout.buffer.write(recvbuff)
        sys.stdout.flush()


async def client_echo(data, sock):
    await asyncio.gather(
        read_input(data, sock),
        read_socket(sock)
    )

def launchMethod(input:str, server_address:str, server_port:int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serv_add = (server_address, server_port)

    try:
        sock.connect(serv_add)
        print(f"{bcolors.OKGREEN}Connection to {serv_add} established!{bcolors.ENDC}")
    except Exception as e:
        print(f"{bcolors.FAIL}Connection error: {e}{bcolors.ENDC}")
        sys.exit(1)

    asyncio.run(client_echo(input, sock))

if __name__ == "__main__":
    input_data = {"header": "StudentsLogin", "payload": {"Matricola": "0124002584", "Password": "test123"}}
    launchMethod(json.dumps(input_data), "127.0.0.1", 1024)
