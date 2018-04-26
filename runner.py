import subprocess, os
import sys

directory = '/Users/ErinMozdy/Desktop/runnerfiles'
for filename in os.listdir(directory):
	subprocess.call(['tcpdump','-r',directory + '/' + filename,'tcp','-w','/Users/ErinMozdy/Desktop/runnertcp/'+filename])
	subprocess.call(['tcpdump','-r',directory + '/' + filename,'udp','-w','/Users/ErinMozdy/Desktop/runnerudp/'+filename])


sys.stdout = open('netflowoutput', 'w')
second_directory = '/Users/ErinMozdy/Desktop/runnertcp'
for filename in os.listdir(second_directory):
	subprocess.call(['softflowd','-r',directory + '/' + filename])