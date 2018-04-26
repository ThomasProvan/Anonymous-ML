import subprocess, os
import sys

directory = 'runnerfiles'
for filename in os.listdir(directory):
	subprocess.call(['tcpdump','-r',directory + '/' + filename,'tcp','-w','runnertcp/'+filename])
	subprocess.call(['tcpdump','-r',directory + '/' + filename,'udp','-w','runnerudp/'+filename])


#sys.stdout = open('netflowoutput', 'w')
second_directory = 'runnertcp'
for filename in os.listdir(second_directory):
	subprocess.call(['softflowd','-r',directory + '/' + filename])