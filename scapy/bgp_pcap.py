from scapy.sendrecv import sniff
from scapy.utils import rdpcap

path=r'C:\Users\alons\OneDrive - Universidad de Oviedo\IdR_English\PCAPs\bgp'


#packets = rdpcap(path+'\\'+'IBGP_adjacency.cap')

packets = sniff(offline=path+'\\'+'IBGP_adjacency.cap')

for packet in packets:
    print(packet[0].show())