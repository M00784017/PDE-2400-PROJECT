import opc #imports the simulator
from time import sleep #we just need sleep from time

led_colour=[(0,0,0)]*360 #main list with 360 tuples
# The numbers in each letter represent a pixel in the simulator 60*6
P = [0,1,2,60,61,62,63,120,121,122,123,124,180,181,182,183,184,240,241,242,243,300,301,302] 
A = range(3,60) 
L = range(64,120)
S = range(185,240)
T=range(125,180)
 #I = range(171,239)
I = range(244,300)
N=range(302,330)
E=range(303,360)
#values for colours I will be using
grey=(100,100,100)  #dark grey color number 
black = (0,0,0)
white = (255,255,255)
red = (233,0,0)
green = (81,186,52)

#this is for a user input check:
acceptable_colours = ['r', 'g', 'b', 'R', 'G', 'B']

client = opc.Client('localhost:7890') #connects to simulator
def Palestine():
    for number, colour in enumerate(led_colour):#iterate through 360 LEDs
        #if count inside position of letters, pixel will be green:
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

def menu(): #this is the main menu for selecting the flags
    #this will be displayed on the screen
    print('\nPlease choose a flag to be displayed:')
    print('\n1. Palestine\n')
    x = int(input()) #user input is assigned to variable x
    #check if user input is within the acceptable values:
    while(x not in (1,2,3,4)):
        print('\nPlease enter a valid input!\n')
        x = int(input()) #user input is assigned to variable x
    #depending on the user input return a different flag:
    if x == 1:
        return Palestine()

    
while True:
    menu()
    client.put_pixels(led_colour) #sends values to led simulator
    #need to send it twice if not constantly sending values
    #due to interpolation setting on fadecandy
    client.put_pixels(led_colour)
    sleep(3) #adds a delay


