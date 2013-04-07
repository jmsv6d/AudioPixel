import os.path, sys, socket
import pygame.mixer, pygame.time
mixer = pygame.mixer
time = pygame.time

GROUP_IP = '192.168.0.22'
PORT = 8002
BUFFER_SIZE = 38000
PIXEL_ID = 2

mixer.init(44100, -16, 1, 1024)
channel = mixer.find_channel()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((GROUP_IP, PORT))

while True:
	data, addr = sock.recvfrom(BUFFER_SIZE)
	s = mixer.Sound(data)
	channel.queue(s)
	