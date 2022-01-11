import opc
import time
import random
leds=[(255,255,255)]*360
client=opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)


for led in range(60):
    leds[led]=(255,0,0)
    time.sleep(0.1)
    client.put_pixels(leds)
    
led=0
while led<60:
    leds[59-led]=(255,255,255)
    time.sleep(0.1)
    client.put_pixels(leds)
    led=led+1
