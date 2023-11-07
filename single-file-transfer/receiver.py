# Import the necessary module
import socket  # For socket and network operations

# Function to receive an image file using UDP
def receive_image(file_name, packet_size=2048):
    # Create a UDP socket for receiving data
    receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver.bind(('0.0.0.0', 9999))  # Bind to any available IP address on port 9999

    # Create a file to store the received image data
    received_file = open(file_name, "wb")

    try:
        total_data_received = 0  # Initialize a variable to track the total received data size

        while True:
            try:
                data, addr = receiver.recvfrom(packet_size)  # Receive data and sender's address
                if not data:
                    break  # Break the loop if no more data is received

                received_file.write(data)  # Write the received data to the file
                total_data_received += len(data)  # Update the total data received
                print(f'Received {total_data_received} bytes and saved in "{file_name}".')
            except KeyboardInterrupt:
                print("Receiver interrupted. Closing the receiver.")
                break  # Exit the loop if the receiver is interrupted (e.g., Ctrl+C)
    finally:
        received_file.close()  # Close the received file
        receiver.close()  # Close the receiver socket

if __name__ == "__main__":
    file_to_receive = input("Enter the name for the received image file (e.g., received.jpg): ")
    receive_image(file_to_receive)  # Start receiving and saving the image when the script is executed
