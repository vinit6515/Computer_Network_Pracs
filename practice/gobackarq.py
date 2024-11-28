import random , time 
def send_frame(frame_number):
    print(f"Sending frame {frame_number}")
    return random.choice(['True','False'])
def recieve_frame(expected_frame):
    time.sleep(1)
    return random.choice([None,expected_frame])
window_size = int(input("Enter the window size: "))
total_frames = int(input("Enter the total number of frames: "))
base =0
ack_recieved=-1
next_frame=0
while base < total_frames:
    while next_frame< base + window_size and next_frame< total_frames:
        if send_frame(next_frame):
            print(f"Frame {next_frame} sent successfully.")
        else:
            print(f"Frame {next_frame} is lost.")
        next_frame +=1
    ack_recieved=recieve_frame(base)
    if ack_recieved is not None:
        print(f"ACK recieved for frame {ack_recieved}.")
        base = ack_recieved+1
    else:
        print(f"ACK for frame not recieved due to timeout. Resending the base frame ")
        next_frame=base
