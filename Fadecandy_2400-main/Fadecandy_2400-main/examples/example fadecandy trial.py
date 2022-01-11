

from __future__ import division 

import opc
import time
import colorsys
from time import sleep
from random import seed
from random import randint
bits = ( (255,0,0), (0,0,255) )
client = opc.Client('localhost:7890')
while True:
	# Flash each strip in turn
	for strip in range(6):
		pixels = [ (90,90,90) ] * 512
		for i in range(32):
			pixels[strip * 64 + i * 2] = (255,127,255)

		# Label all strips always
		for s in range(6):
			pixels[s * 64 + 0] = bits[(s >> 2) & 1]
			pixels[s * 64 + 1] = bits[(s >> 1) & 1]
			pixels[s * 64 + 2] = bits[(s >> 0) & 1]

		client.put_pixels(pixels)
		time.sleep(0.5)
