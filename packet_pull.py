import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

packet_list = []
directory = 'runnerfiles'
for filename in os.listdir(directory):
	packets = rdpcap(directory + '/' + filename)
	for packet in packets:
		packet_list.append(packet)