from scapy.all import *

packets = rdpcap("level02.pcap")
for i, packet in enumerate(packets):
    print(i, packet.sprintf("{Raw:%Raw.load%\n}"))