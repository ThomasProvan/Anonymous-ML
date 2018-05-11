# -*- coding: utf-8 -*-
"""
Created on Thu May 10 17:32:08 2018

@author: Der Niabs

Master Script for the Anon-ML project

Takes in data in the Active directory of the main project, brings it into python
and formats. (Currently at ./Data)
Then makes a TestController to execute tests.

Some of the code in here will be moved to TestController later, when that class
is more complete.
"""

import KNearestSystem
import TestController
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import numpy as np
import ipaddress
# Look into paring this down to *exactly* what we need. We're just reading
# packets and doing some parsing on them.



packet_lists = [] #fun with packets!
packet_list = []
directory = './Data'
for filename in os.listdir(directory):
    packets = rdpcap(directory + '/' + filename)
    packet_lists.append(packets)
    for packet in packets:
        packet_list.append(packet)


"""
for packet in packet_list
    
scapy notes

packet[|LAYER_NAME|] returns a packet with that layer, and all subsequent layers

packet.show() displays fields of the packet

packet.field gives the first field of that name in the packet.
    Will drill through layers. If multiple have the same name, will return the
    one in the highest layer.
    
packet.time (!!) gives the time (since last epoch) the packet was recieved.
    Not shown in summary.
    Warning: packet[IP].time gives the time scapy read in the packet.

int(ipaddress.ip_address(randompacket[IP].src)) ## Converts IP address string
 to int
     # To evaluate - is there a better way to do this conversion?



"""