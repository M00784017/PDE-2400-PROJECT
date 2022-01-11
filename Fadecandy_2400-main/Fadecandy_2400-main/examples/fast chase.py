import opc, time

numLEDs = 360
client = opc.Client('localhost:7890')

while True:
	for i in range(numLEDs):
		pixels = [ (0,0,255) ] * numLEDs
		pixels[i] = (255, 0, 0)
		client.put_pixels(pixels)
		time.sleep(0.01)
