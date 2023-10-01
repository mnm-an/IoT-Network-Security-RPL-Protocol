# Calculate RPL Network Metrics from PCAP Log Files
# This script analyzes PCAP log files to calculate RPL (Routing Protocol for Low-Power and Lossy Networks) network metrics.

# Import necessary modules from Scapy
from scapy.all import *

conf.dot15d4_protocol = "sixlowpan"

# Define a list of PCAP files to analyze
pcaps = ['15-SA.pcap', '15-AA.pcap','25-SA.pcap', '25-AA.pcap']

# Print a description of the PCAP files
print('SA: WITHOUT ATTACK')
print('AA: WITH ATTACK\n')

# Initialize variables to count DIO (DODAG Information Object) and DAO (Destination Advertisement Object) packets
DIO_WITHOUT_ATTACK = 0
DIO_WITH_ATTACK = 0
DAO_WITHOUT_ATTACK = 0
DAO_WITH_ATTACK = 0

# Loop through each PCAP file
for name in pcaps:
    cap = rdpcap(name)
    DIO_number = 0
    DAO_number = 0

    # Analyze packets in the PCAP file
    for packet in cap:
        if "IPv6" in packet and hasattr(packet[IPv6], "code") and packet[IPv6].code == 1:
            DIO_number += 1
        if "IPv6" in packet and hasattr(packet[IPv6], "code") and packet[IPv6].code == 2:
            DAO_number += 1
        else:
            continue

    # Print the number of DIO and DAO packets for each file
    print(f'DIO number for {name}: {DIO_number}')
    print(f'DAO number for {name}: {DAO_number}')
    print("\n")

    # Update the cumulative counts based on the file type
    if 'SA' in name:
        DIO_WITHOUT_ATTACK += DIO_number
        DAO_WITHOUT_ATTACK += DAO_number

    if 'AA' in name:
        DIO_WITH_ATTACK += DIO_number
        DAO_WITH_ATTACK += DAO_number

# Print summary statistics
print('-------------------------------------------------------------')
print(f'DIO Threshold WITHOUT ATTACK: {DIO_WITHOUT_ATTACK / 4}')
print(f'DIO Threshold WITH ATTACK: {DIO_WITH_ATTACK / 4}')
print("\n")
print(f'DAO Threshold WITHOUT ATTACK: {DAO_WITHOUT_ATTACK / 4}')
print(f'DAO Threshold WITH ATTACK: {DAO_WITH_ATTACK / 4}')

# Wait for user input before exiting
input("Press Enter to Exit: ")
