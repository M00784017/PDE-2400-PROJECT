import opc, time

numLEDs = 360
client = opc.Client('localhost:7890')

blue = [ (0,0,255) ] * numLEDs
white = [ (255,255,255) ] * numLEDs


client.put_pixels(blue)
client.put_pixels(blue)
time.sleep(2)
client.put_pixels(white)
