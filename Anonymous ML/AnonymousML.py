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

import KNearestSystem as KNNSys
import TestController
import KNClassifierSystem as KNCSys
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
data = []
# May want to convert this to ndarray here. 


# Remember how knn works, Kri...
# There aren't a *ton* of duplicates, it's just that there are enough that there
# are values nearby to each one.
# ... okay, maybe there are a ton of duplicates. Kind of. :P


diffDict = {}

# Base version of the function. Takes in the keys as seperate inputs,
# then returns either the difference between the recorded and current time, or
# None if the keys have not been see before in this order.
def keyDiff(value, *keys):
    if keys in diffDict:
        diff = value - diffDict[keys]
        diffDict[keys] = value
        return diff
    diffDict[keys] = value
    return None

# ... I was really hoping to never encouter a * notation again. Oh well.
# Forces the keys into a particular order and **removes duplicates**, then calls
# keyDiff.
def keyDiffSet(value, *keys):
    return keyDiff(value, *tuple(set(keys)))


# For data formatting purposes, the *first* column should be the class, if
# relevant to the current tests. Any MLSystem doing classification *will* assume
# the first column is the class of interest when doing any necessary processing.
directory = './Data'
for filename in os.listdir(directory):
    #TODO: Need to do something to resolve diff, or guarantee order with multiple
    # files. Keep in mind if we are ever using multiples.
    packets = rdpcap(directory + '/' + filename)
    for packet in packets:
        
        dstIP = int(ipaddress.ip_address(packet[IP].dst))
        srcIP = int(ipaddress.ip_address(packet[IP].src))
        
        # One-way diff, IP: returns time since last packet sent from src to dst
#        diff = keyDiff(packet.time, dstIP, srcIP)
#        if not diff: #If we haven't seen this connection before, throw away packet
#            continue
        
        # Two-way diff, IP: returns time since last packet sent between src & dst
        diff = keyDiffSet(packet.time, dstIP, srcIP)
        if not diff: #If we haven't seen this connection before, throw away packet
            continue
        
        dataEntry = []
        dataEntry.append(packet.dport)      #Dst Port
        dataEntry.append(dstIP)             #Dst IP
        dataEntry.append(packet.sport)      #Src Port
        dataEntry.append(srcIP)             #Src IP
        dataEntry.append(packet[IP].len)    #IP Length
        #dataEntry.append(packet.time)      #Timestamp
        dataEntry.append(diff)              #Current time difference (varies)
        data.append(dataEntry)

"""
I have completely forgotten what sort of changes I was going to do with the this...
Other than adjusting it for classification of dport.
I remember we were going to do something w.r.t time, but now that I'm thinking
about it I can't remember which one we decided on... and I thought of a third
way to do it XD

Packets are returned in 'file order'. As long as the file is chronological,
the time-stamps will be as well. That said, there's an anomaly: What do I do
with the first packet in the file? 3 options: throw it out, assign it the 'avg'
value, or assign it '0'.
        
Second thing, there's connectionless-diff, where i'm just recording the time
since last packet in the file, and connection-diff, where I'm recording the time
since last packet between two particular IP's (this is still easy, though it makes
the previous question of 'what do I do with the first one')
"""


#QUESTION: Is it useful to feed this into np.unique?
"""
With the initial Berkeley dataset, we've got some backbone traffic in the data.
As a result, only a few kinds of 'packets' make up most of our data. Using just
IP & Port, roughly 90% (or more) of the traffic is traffic on one of 6 connections.
    (according to raw packet count)
My instinct is generally no, but it might be useful to make KNN's output
more sensible. Possibly. I don't know, this may just be an expected result.
I'm curious if some of the CRAWDAD data will have similar proprties. I assume
it will, if backbone traffic is included. 
"""
    
# Making a ML system and passing to TestController after this point.

kns = KNNSys.KNearestSystem()
knc = KNCSys.KNClassifierSystem()

controller = TestController.TestController(data)
# Working out what the constructor looks like.


#knnResults = controller.run(kns)
 



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