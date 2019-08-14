import time
import sys
import socket

upd_ip          = "127.0.0.1"
udp_port        = 7010
sock            = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

divider         = '- ' * 10
num_iters       = 11
sleep_interval  = 2

def msg_to_bytes(msg):
    return msg.encode('utf-8')

starting_msg = "Sending messages at an interval of {} seconds".format(sleep_interval)
sock.sendto(msg_to_bytes(starting_msg), (upd_ip, udp_port))

for each in range(num_iters):
    msg         = "{} of {}".format(each, num_iters-1)
    sock.sendto(msg_to_bytes(msg), (upd_ip, udp_port))
    time.sleep(sleep_interval)

ending_msg = "All messages sent"
sock.sendto(msg_to_bytes(ending_msg), (upd_ip, udp_port))