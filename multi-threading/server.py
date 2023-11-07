# Import the necessary modules
import socket  # For socket operations
import threading  # For creating threads to handle multiple clients

# Define server address and port
server_host = '127.0.0.1'  # Server's IP address (localhost in this case)
server_port = 45549  # Server's port number

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

        # Create a new thread to handle the client
        client_thread = threading.Thread(target=process_messages, args=(client_socket,))
        client_thread.start()

# Function to process messages from a client
def process_messages(client_socket):
    while True:
        # Receive and decode the message from the client (up to 1024 bytes)
        message = client_socket.recv(1024).decode()
        
        if not message:
            # Client has disconnected, close the client socket and exit the loop
            client_socket.close()
            break

        # Process the received message and get a response
        response = process_message(message)
        
        # Encode and send the response back to the client
        client_socket.send(response.encode())

# Function to process individual messages
def process_message(message):
    if "order" in message:
        return "How can I help you?"
    elif "menu" in message:
        return "Here is our menu."
    else:
        return "That's an interesting idea!"

# Entry point of the script
if __name__ == "__main__":
    start_server()  # Start the server when the script is executed
