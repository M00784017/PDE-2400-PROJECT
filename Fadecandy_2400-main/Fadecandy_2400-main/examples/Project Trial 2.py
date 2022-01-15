import opc #imports the simulator
from time import sleep #we just need sleep from time

led_colour=[(0,0,0)]*360 
# The numbers in each letter represent a pixel in the simulator 60*6
P = [0,1,2,3,60,61,62,63,64,120,121,122,123,124,125,180,181,182,183,184,185,240,241,242,243,244,300,301,302,303] 
A = range(4,60) 
L = range(65,120)
S = range(186,240)
T=range(126,180)
 #I = range(171,239)
I = range(245,300)
N=range(302,330)
E=range(304,360)

grey=(100,100,100)  #dark grey color number 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)




client = opc.Client('localhost:7890') #connects to simulator
def Palestine():
    for number, colour in enumerate(led_colour):
        
        if number in P:
            led_colour[number] = red
        if number in A:
            led_colour[number] = grey #although the palestine flag is black instead of grey here, I put dark grey because black will not appear.
        if number in L:
            led_colour[number] = grey
        if number in S:
            led_colour[number] = white
        if number in T:
            led_colour[number] = white
        
        if number in I:
            led_colour[number] = green   
        if number in E:
            led_colour[number] = green

def menu(): 
    
    print('\nEnter the number of the flag you wish to be displayed:')
    print('\n1. Palestine\n')
    x = int(input()) 
    while(x not in (1,2,3,4)):
        
        print('\nPlease enter a valid input!\n')
        x = int(input()) 
    
    if x == 1:
        return Palestine()

    
while True:
    menu()
    client.put_pixels(led_colour) 
  
    
    client.put_pixels(led_colour)
    sleep(1) 
    break #till now that is the end of the animation

