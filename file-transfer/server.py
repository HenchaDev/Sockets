# Import the necessary modules
import socket  # For socket and network operations
import os  # For file and directory operations
import time  # For measuring time

# Server configuration
HOST = '127.0.0.1'  # Server's IP address
PORT = 45549        # Server's port number
BUFFER_SIZE = 1024  # Size of the data buffer for receiving files
UPLOAD_FOLDER = 'uploads/'  # Folder to store uploaded files

def main():
    # Create a socket using IPv4 and TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the server address and port
    server_socket.bind((HOST, PORT))
    
    # Listen for incoming connections, allowing up to 1 pending connection
    server_socket.listen(1)
    
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        # Accept incoming connections and return a new socket and client address
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        # Receive the file name from the client
        received_file_name = client_socket.recv(BUFFER_SIZE).decode()
        received_file_path = os.path.join(UPLOAD_FOLDER, received_file_name)

        # Measure the start time for upload speed calculation
        start_time = time.time()

        # Open the file for writing in binary mode
        with open(received_file_path, 'wb') as file:
            while True:
                data = client_socket.recv(BUFFER_SIZE)  # Receive data in chunks
                if not data:
                    break
                file.write(data)  # Write the received data to the file

        # Measure the end time and calculate upload speed
        end_time = time.time()
        elapsed_time = end_time - start_time
        file_size = os.path.getsize(received_file_path)
        upload_speed = file_size / elapsed_time

        print(f"Received {received_file_name} from {addr}")
        print(f"Upload speed: {upload_speed:.2f} B/s")

        # Close the client socket
        client_socket.close()

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)  # Create the UPLOAD_FOLDER directory if it doesn't exist
    main()  # Start the server when the script is executed
