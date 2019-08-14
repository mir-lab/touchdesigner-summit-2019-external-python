import time
import sys
import socket
from argparse import ArgumentParser

def msg_to_bytes(msg):
    return msg.encode('utf-8')

def msg_loop(port, interval, loop):
    # localhost
    upd_ip          = "127.0.0.1"

    # set udp port with input val and initialize socket connection
    udp_port        = int(port)
    sock            = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # set additional variables with input vals
    num_iters       = int(loop)
    sleep_interval  = int(interval)

    # send message that we're starting
    starting_msg = "Sending messages at an interval of {} seconds".format(sleep_interval)
    sock.sendto(msg_to_bytes(starting_msg), (upd_ip, udp_port))

    # run message loop
    for each in range(num_iters):
        msg         = "{} of {}".format(each, num_iters-1)
        sock.sendto(msg_to_bytes(msg), (upd_ip, udp_port))
        time.sleep(sleep_interval)

    # send message that we're ending
    ending_msg = "All messages sent"
    sock.sendto(msg_to_bytes(ending_msg), (upd_ip, udp_port))



# execution order matters -this puppy has to be at the bottom as our functions are defined above
if __name__ == '__main__':
    parser = ArgumentParser(description='A simple UDP example')
    parser.add_argument("-p", "--port", dest="port", help="UDP port", required=True, default=1234)
    parser.add_argument("-i", "--interval", dest="interval", help="loop interval", required=True, default=5)
    parser.add_argument("-l", "--loop", dest="loop", help="number of repetitions", required=True, default=10)
    args = parser.parse_args()

    msg_loop(args.port, args.interval, args.loop)
    pass

# example
# python .\cmd_line_python_udp_msg_args.py -p=5000 -i=2 -l=10