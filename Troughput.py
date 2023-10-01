from scapy.all import *

conf.dot15d4_protocol = "sixlowpan"

pcaps = ['15-SA.pcap','15-AA.pcap']  #Load Files Here
         
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

flux()

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
    

    
