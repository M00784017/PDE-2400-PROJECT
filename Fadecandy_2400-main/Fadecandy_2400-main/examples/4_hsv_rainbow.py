import opc
from time import sleep
import colorsys

client = opc.Client('localhost:7890')
numLEDs=360
s = 1.0 ##maximum colour
v = 1.0 ##maximum brightness
colors=[]
for i in range(0,255):
    rgb = colorsys.hsv_to_rgb(i/360.0, s, v) #colorsys returns floats between 0 and 1
    r = rgb[0] #extract said floating point numbers
    g = rgb[1]
    b = rgb[2]
    colors.append((r,g,b))
    rgb = (r*255, g*255, b*255) #make new tuple with corrected values
    client.put_pixels([rgb] *numLEDs) #send out

    sleep(0.1) #20ms 
