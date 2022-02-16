import opc
import time
import random

leds = [(255,255,255)]*360 #white

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

 #for led in leds: # pick out an element: led = (255,255,255)
for led in range(60):
    
    leds[led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)

led = 60
while led<=119:
    leds[led] = (0,255,0)
    time.sleep(.01)
    client.put_pixels(leds)
    led = led + 1 #or reverse if you want
led = 60
while led<=179:
    leds[led] = (0,0,255)
    time.sleep(.01)
    client.put_pixels(leds)
    led = led + 1 #or reverse if you want
led = 60
while led<=119:
    leds[59-led] = (100,170,50)
    time.sleep(.01)
    client.put_pixels(leds)
    led = led + 1 #or reverse if you want







# reverse the last example.
# do a scroll from the middle to the outside - two pixels moving away from each other.
# reverse the scroll from the middle
# do a snake, 5 pixels long, returns to start when it hits the end



