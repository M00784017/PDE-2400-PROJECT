import opc
import time
#this is the rgb color for yellow, and I multiplied it by the number of leds
yellow=[(255,255,0)]*360
red= [ (0,255,0)] *360
print (yellow)

#to open the opc simulator
client = opc.Client('localhost:7890')


client.put_pixels(yellow)
time.sleep(1)

