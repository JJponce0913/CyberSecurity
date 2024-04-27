from scapy.all import *

# Read the pcap file
packets = rdpcap('traffic.pcap')

# Open a text file for writing
with open('pcapOutput2.txt', 'w') as file:
    # Process and write packet information to the text file
    for packet in packets:
        file.write(str(packet) + '\n')