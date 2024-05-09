import errno
import socket
import threading
import time
# Utility function to ensure complete data is sent over the connection
from common.full_write import full_write

# Function to handle an individual connection in a separate thread
def handle_connection(conn_fd, client, cont, logging):
    # Get the current time
    timeval = time.ctime(time.time())
    # Encode the time string and send it to the client
    buffer = f"{timeval}\r\n".encode('utf-8')
    full_write(conn_fd, buffer)

    # If logging is enabled, print information about the client
    if logging:
        host, port = client
        print(f"Request from host {host} number {cont}, port {port}")

# Main function to run the server
def main():
    # Create a TCP socket
    list_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Specify the server address (host, port)
    serv_add = ('127.0.0.1', 1024)

    # Bind the socket to the specified address
    list_fd.bind(serv_add)
    # Start listening with a maximum backlog of 1024 pending connections
    list_fd.listen(1024)

    # Counter for tracking the number of connections
    cont = 0
    # Flag to enable/disable logging
    logging = 1

    # List to keep track of thread references
    threads = []

    try:
        # Infinite loop to accept incoming connections
        while True:
            # Accept a connection, creating a new socket (conn_fd) and storing client details
            conn_fd, client = list_fd.accept()
            # Increment the connection counter
            cont += 1

            # Create a new thread to handle the connection
            thread = threading.Thread(target=handle_connection, args=(conn_fd, client, cont, logging))
            # Start the thread
            thread.start()
            # Append the thread reference to the list
            threads.append(thread)

    # Handle a keyboard interrupt to gracefully terminate the server
    except KeyboardInterrupt:
        print("Server terminated by user")

    # Finally block to ensure cleanup even if an exception occurs
    finally:
        # Close the listening socket
        list_fd.close()

        # Wait for all threads to complete before exiting
        for thread in threads:
            thread.join()

# Entry point of the program
if __name__ == "__main__":
    main()
