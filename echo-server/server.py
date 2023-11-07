# Import the necessary modules
import socket  # For socket operations
import os  # For process management
import sys  # For system-related operations

# Define server address and port
server_host = '127.0.0.1'  # Server's IP address
server_port = 45545  # Server's port number

# Function to start the server
def start_server():
    # Create a socket using IPv4 and TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the server address and port
    server_socket.bind((server_host, server_port))
    
    # Listen for incoming connections
    server_socket.listen()
    
    print(f"Server is listening on {server_host}:{server_port}")

    while True:
        # Accept incoming connections and return a new socket and client address
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Fork a new process to handle the client
        pid = os.fork()

        if pid == 0:
            # In the child process
            handle_client(client_socket)
            sys.exit()
        else:
            # In the parent process
            client_socket.close()

# Function to handle a client in a child process
def handle_client(client_socket):
    while True:
        # Receive data from the client (up to 1024 bytes) and decode it
        data = client_socket.recv(1024).decode()
        
        if not data:
            # Client has disconnected, close the client socket and exit the loop
            client_socket.close()
            break

        # Echo the received data back to the client (doubled)
        echoed_data = data * 2
        client_socket.send(echoed_data.encode())

# Entry point of the script
if __name__ == "__main__":
    start_server()  # Start the server when the script is executed
