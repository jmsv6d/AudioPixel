import os.path, sys, socket
import pygame.mixer, pygame.time
mixer = pygame.mixer
time = pygame.time

IP = '127.0.0.1'
PORT = 8800
BUFFER_SIZE = 1024
PIXEL_ID = 1

main_dir = os.path.split(os.path.abspath(__file__))[0]

file_path = os.path.join(main_dir,
                                 'tone.wav')

mixer.init(44100, -16, 1, 8192)
sound = mixer.Sound(file_path)
channel = sound.play()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP, PORT))
sock.send(str(PIXEL_ID))

while True:
	data = sock.recv(BUFFER_SIZE)
	s = mixer.Sound(data)
	channel.play(s)

