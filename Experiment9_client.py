import socket
import time

# Sender (Client) Function for Stop-and-Wait Protocol
def sender():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Server address
    server_address = ('localhost', 12345)
    
    # Timeout setting for waiting for acknowledgment
    client_socket.settimeout(3)  # Timeout after 3 seconds
    
    frame_number = 0
    total_frames = 5

    while frame_number < total_frames:
        # Send the frame
        print(f"Sending Frame {frame_number}")
        client_socket.sendto(str(frame_number).encode(), server_address)

        try:
            # Wait for acknowledgment
            ack, _ = client_socket.recvfrom(1024)
            if ack.decode() == str(frame_number):
                print(f"Acknowledgment received for Frame {frame_number}")
                frame_number += 1
        except socket.timeout:
            # Handle timeout and retransmit the same frame
            print(f"Timeout occurred for Frame {frame_number}. Retransmitting...")

    print("All frames sent successfully.")

    # Close the socket connection
    client_socket.close()

# Run the sender
if __name__ == "__main__":
    sender()
