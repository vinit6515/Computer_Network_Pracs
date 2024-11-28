#First let us implement Go-Back N arq
import random
import time
window_size= int(input("Enter the window size : "))
total_number_of_frames=int(input("Enter total number of frames: "))
timeout=int(input("Enter the timeout: "))

def send_frame(frame_number):
    print(f"Sending frame {frame_number}")
    return random.choice([True,False])
def recieve_ack(expected_frame):
    time.sleep(1)
    return random.choice([expected_frame,None])# Expected frame represents success and None represents failure
def go_back_n_arq():
    base=0
    next_frame_to_send =0 
    ack_recieved = -1
    while base < total_number_of_frames:
        while next_frame_to_send< base + window_size and next_frame_to_send < total_number_of_frames:
            if send_frame(next_frame_to_send):
                print(f"Frame {next_frame_to_send} sent successfully.")
            else:
                print(f"Frame {next_frame_to_send} is lost.")
            next_frame_to_send +=1
        ack_recieved = recieve_ack(base)
        if ack_recieved is not None:
            print(f"Recieved ACK for frame {ack_recieved}")
            base = ack_recieved +1
        else:
            print("ACK lost on timeout occured resending from base frame.")
            next_frame_to_send= base
if __name__=="__main__":
    go_back_n_arq()

