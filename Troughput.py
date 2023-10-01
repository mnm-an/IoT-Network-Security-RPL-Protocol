# Calculate Throughput of an RPL Network from PCAP Log Files
# This script analyzes PCAP (Packet Capture) log files to calculate the throughput of a network using the RPL (Routing Protocol for Low-Power and Lossy Networks) protocol. RPL is commonly used in IoT (Internet of Things) and low-power wireless networks.

# Import necessary modules from Scapy
from scapy.all import *

# Set the DOT15.4 protocol to "sixlowpan"
conf.dot15d4_protocol = "sixlowpan"

# Define a list of PCAP files to analyze
pcaps = ['15-SA.pcap', '15-AA.pcap', '25-SA.pcap', '25-AA.pcap']

# Define a function called 'flux'
def flux():
    for name in pcaps:
        cap = rdpcap(name)

        start_time = 0
        end_time = 890.647727

        total_bytes = 0
        for packet in cap:
            if "IPv6" in packet:
                total_bytes += packet[IPv6].plen

        avg_bytes_per_sec = total_bytes / (end_time - start_time)

        throughput = avg_bytes_per_sec * 8

        print(f'Throughput for {name}: {throughput} bits/sec')

# Call the 'flux' function to calculate and print throughput
flux()

# Define a function called 'throughput'
def throughput(name):
    cap = rdpcap(name)

    start_time = 0
    end_time = 890.647727

    total_bytes = 0
    for packet in cap:
        if "IPv6" in packet:
            total_bytes += packet[IPv6].plen

    avg_bytes_per_sec = total_bytes / (end_time - start_time)

    return avg_bytes_per_sec * 8
