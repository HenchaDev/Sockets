# Import the necessary module
import socket  # For socket operations

# Define server address and port
server_host = '127.0.0.1'  # Server's IP address
server_port = 45545  # Server's port number

# Function to start the client
def start_client():
    # Create a socket using IPv4 and TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server using the server address and port
    client_socket.connect((server_host, server_port))

    while True:
        # Prompt the user to enter a message
        message = input("Enter a message: ")
        
        # Encode and send the message to the server
        client_socket.send(message.encode())

        # Receive and decode the response from the server (up to 1024 bytes)
        response = client_socket.recv(1024).decode()
        
        # Print the response from the server
        print(f"Server: {response}")

# Entry point of the script
if __name__ == "__main__":
    start_client()  # Start the client when the script is executed
