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
    leds[59-led]=(0,255,0)
    time.sleep(0.1)
    client.put_pixels(leds)
    led=led+1

led=0
#making it more compact
while led<60:
    for rows in range(6):
        leds[led+ rows*60]=(0,0,255)
    #leds[led]=(0,0,255)
    #leds[led+60]=(0,0,255)
    time.sleep(0.1)
    client.put_pixels(leds)
    led=led+1

    
