import socket
import os
import time

# Server configuration
HOST = '127.0.0.1'
PORT = 45549
BUFFER_SIZE = 1024

def download_file(client_socket):
    file_to_download = input("Enter the name of the file to download: ")
    client_socket.send(file_to_download.encode())

    download_folder = 'downloads'
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    download_path = os.path.join(download_folder, file_to_download)

    start_time = time.time()

    with open(download_path, 'wb') as file:
        while True:
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                break
            file.write(data)

    end_time = time.time()
    elapsed_time = end_time - start_time

    file_size = os.path.getsize(download_path)
    download_speed = file_size / elapsed_time

    print(f"{file_to_download} downloaded and stored in the 'downloads' folder")
    print(f"Download speed: {download_speed:.2f} B/s")

def upload_file(client_socket):
    file_path = input("Enter the path of the file to upload: ")

    # Extract the actual file name from the file path
    file_name = os.path.basename(file_path)

    # Send the file path and file name to the server
    client_socket.send(file_path.encode())
    client_socket.send(file_name.encode())

    start_time = time.time()

    with open(file_path, 'rb') as file:
        while True:
            data = file.read(BUFFER_SIZE)
            if not data:
                break
            client_socket.send(data)

    end_time = time.time()
    elapsed_time = end_time - start_time

    file_size = os.path.getsize(file_path)
    upload_speed = file_size / elapsed_time

    print(f"{file_name} sent to the server")
    print(f"Upload speed: {upload_speed:.2f} B/s")


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    while True:
        print("1. Download a file")
        print("2. Upload a file")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            client_socket.send(b'download')
            download_file(client_socket)
        elif choice == '2':
            client_socket.send(b'upload')
            upload_file(client_socket)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

    client_socket.close()

if __name__ == "__main__":
    main()
