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
# Look into paring this down to *exactly* what we need. We're just reading
# packets and doing some parsing on them.

import numpy as np
import ipaddress



# Going to start with the data in a list, mostly to play around with converting
# to array. We may not want it to ever be in a list due to memory issues, but
# we'll see.

#
dataList = []
#

# Current Data: [IP].src (int), [IP].dst (int), [TCP]sport, [TCP]dport,
#               time (abs, ms)
# Probably want to remove time eventually, I'm just using it to force a
# difference. There's... a lot of duplicate entries.
directory = './Data'
for filename in os.listdir(directory):
    packets = rdpcap(directory + '/' + filename)
    for packet in packets:
        dataEntry = []
        dataEntry.append(int(ipaddress.ip_address(packet[IP].src)))
        dataEntry.append(int(ipaddress.ip_address(packet[IP].dst)))
        dataEntry.append(packet.sport)
        dataEntry.append(packet.dport)
        #dataEntry.append(packet.time)
        dataList.append(dataEntry)


# Making a ML system and passing to TestController after this point.

kns = KNearestSystem.KNearestSystem()
knnController = TestController.TestController(dataList, kns)



# Data formatting notes

# The various scikit-learn libraries expect an 'array like' object.
# Fortunately, they can correctly convert a list. So, a list-of-lists is a
# valid object to pass them. We may want to convert to array's at some point
# for memory reasons, but that can be done hear. Below this, I'll probably
# just pass inputs through array() as necessary.

# Current configuration works, it just might be memory inefficient.



"""
for packet in packet_list
    
scapy notes

packet[|LAYER_NAME|] returns a packet with that layer, and all subsequent layers

packet.show() displays fields of the packet

packet.field gives the first field of that name in the packet.
    Will drill through layers. If multiple have the same name, will return the
    one in the highest layer.
    
packet.time (!!) gives the time (since last epoch) the packet was recieved.
    Not in show()
    Warning: packet[IP].time gives the time scapy read in the packet.

int(ipaddress.ip_address(randompacket[IP].src)) ## Converts IP address string
 to int
     # To evaluate - is there a better way to do this conversion?



"""