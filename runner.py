import subprocess, os

directory = '/Users/ErinMozdy/Desktop/runnerfiles'
for filename in os.listdir(directory):
	subprocess.call(['tcpdump','-r',directory + '/' + filename,'tcp','-w','/Users/ErinMozdy/Desktop/runnertcp/'+filename])
	subprocess.call(['tcpdump','-r',directory + '/' + filename,'udp','-w','/Users/ErinMozdy/Desktop/runnerudp/'+filename])