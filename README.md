# Contiki-Cooja-IOT
Analyze pcap logs from Contiki cooja

# Script Description:

This Python script collection is designed to analyze PCAP (Packet Capture) log files from a network and calculate essential metrics related to the RPL (Routing Protocol for Low-Power and Lossy Networks) protocol. RPL is commonly used in IoT (Internet of Things) and low-power wireless networks.

# Key Features:

The collection consists of two scripts, each with its own purpose:

1. Throughput Analysis (throughput.py):

    This script calculates network throughput by analyzing PCAP log files.
    It identifies and counts IPv6 packets within the logs.
    Two types of IPv6 packets are considered:
        DIO (DODAG Information Object) packets, which carry routing information.
        DAO (Destination Advertisement Object) packets, which advertise available destinations.
    The script categorizes packets into two groups:
        "WITHOUT ATTACK": Packets captured under normal network conditions.
        "WITH ATTACK": Packets captured during network attacks or compromised conditions.
    It calculates and reports metrics for each group:
        The number of DIO packets.
        The number of DAO packets.
    The script calculates throughput and reports it in bits per second.

2. DIO and DAO Packet Analysis (dio_dao.py):

    This script specifically analyzes DIO and DAO packets within PCAP log files.
    It identifies and counts DIO and DAO packets in the logs.
    The analysis can help understand the behavior of the RPL-based network.

# Usage:

For "throughput.py" and "dio_dao.py," follow these steps:

    1 - Ensure you have the required Python environment and the Scapy library installed.

    2 - Place your PCAP log files in the designated variable (specified as pcaps) for each script.

    3 - Run the desired script to process the PCAP files.

    For "throughput.py," the script will calculate and print network throughput, helping assess data transfer rates under different network conditions.

    For "dio_dao.py," the script will provide insights into DIO and DAO packet counts, aiding in understanding network routing behavior.

    Both scripts can be useful for network administrators, engineers, and security professionals to monitor network performance and detect anomalies.

    Press "Enter" to exit each script after reviewing the results.

These scripts collectively provide valuable insights into the behavior of RPL-based networks and can help network administrators and security professionals identify abnormal network activity or security breaches.
