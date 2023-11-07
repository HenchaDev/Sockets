# Import the necessary modules
import socket  # For socket and network operations
import time  # For timing the data transfer

# Function to send an image file using UDP
def send_image(file_name, receiver_address, packet_size=2048):
    # Create a UDP socket for sending data
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Open the image file in binary read mode
        with open(file_name, 'rb') as file:
            data = file.read(packet_size)  # Read the file in chunks of packet_size
            total_data_sent = 0  # Initialize a variable to track the total data sent

            while data:
                start_time = time.time()  # Record the start time for measuring transfer speed
                sender.sendto(data, receiver_address)  # Send the data to the receiver's address
                total_data_sent += len(data)  # Update the total data sent
                data = file.read(packet_size)  # Read the next chunk of data
                end_time = time.time()  # Record the end time

                # Print progress and transfer speed
                print(f'Sent {total_data_sent} bytes with packet size {packet_size} in {end_time - start_time} seconds')

        print('File sent successfully.')

    finally:
        sender.close()  # Close the sender socket when done

if __name__ == "__main__":
    file_to_send = 'cat.jpg'  # Name of the file to send
    receiver_address = ('127.0.0.1', 9999)  # Receiver's IP address and port
    send_image(file_to_send, receiver_address)  # Start sending the image when the script is executed
