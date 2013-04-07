import os.path, sys, socket
import pygame.mixer, pygame.time
mixer = pygame.mixer
time = pygame.time

GROUP_IP = '192.168.0.22'
PORT = 8002
BUFFER_SIZE = 38000
PIXEL_ID = 2
connected = False

mixer.init(44100, -16, 1, 1024)
channel = mixer.find_channel()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while not connected
	try:
		sock.connect((GROUP_IP, PORT))
		connected = True
	except:
		pass

while True:
	data, addr = sock.recvfrom(BUFFER_SIZE)
	s = mixer.Sound(data)
	channel.queue(s)
	
# Do we want the client to always be trying to connect to the server?
#in order to catch when the server disconnects we could
# 1) do a try block and an outer loop so when the client can no longer recieve
#    data break out of current loop and try connecting again

# 2) Include a SHUTDOWN and/or EXIT command that can be sent from the server before shutting down
#    a) For a SHUTDOWN request the clients would close the connection then perhaps perform a shutdown command to 
#       shutdown the pi
#    b) For an EXIT request perhaps the client would close the connection and then try connecting again
