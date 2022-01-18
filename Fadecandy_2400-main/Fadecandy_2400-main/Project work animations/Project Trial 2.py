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
G=range(0,27)
D=range(33,87)
D1=range(93,120)
D2=range(240,267)
D3=range(273,327)
D4=range(333,360)
D5=range(27,33)
D6=range(87,93)
D7=range(267,273)
D8=range(327,333)
E1=range(208,212)
E2=range(148,152)
#defining colour numbers in rgb
grey=(100,100,100)  #dark grey color number 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
orange=(255,165,0)
yellow=(255,255,0)
blue=(0,0,255)

client = opc.Client('localhost:7890') #connects to simulator
def Palestine():
    for i in range(len(led_colour)):
        if i in P:
            led_colour[i] = red
        if i in A:
            led_colour[i] = grey #although the palestine flag is black instead of grey here, I put dark grey because black will not appear.
        if i in L:
            led_colour[i] = grey
        if i in S:
            led_colour[i] = white
        if i in T:
            led_colour[i] = white
        
        if i in I:
            led_colour[i] = green   
        if i in E:
            led_colour[i] = green
def England():
    
    for number, colour in enumerate(led_colour):
        if number in G:
            led_colour[number] = white
        if number in D:
            led_colour[number] = white
        if number in D1:
            led_colour[number] = white
        if number in D2:
            led_colour[number] = white
        if number in D3:
            led_colour[number] = white
        if number in D4:
            led_colour[number] = white
        if number in D5:
            led_colour[number] = red
        if number in D6:
            led_colour[number] = red
        if number in D7:
            led_colour[number] = red
        if number in D8:
            led_colour[number] = red   
        if (number % 360 >= 120) and (number % 360 < 240):
            led_colour[number] = red
        
def Ireland():
    for number, colour in enumerate(led_colour):#iterate through 360 LEDs (with an index (count))
        #green part of flag:
        if number % 60 <= 20:
            led_colour[number] = green
        #white part of flag:
        if (number % 60 <= 40) and (number % 60 >= 20):
            led_colour[number] = white
        #red part of flag:
        if (number % 60 >= 40) and (number % 60 <= 80):
            led_colour[number] = orange
def Ukraine():
    for number, colour in enumerate(led_colour):#iterate through 360 LEDs (with an index (count))
        #black part of flag:
        if number % 360 <= 180:
            led_colour[number] = blue

        
        #yellow part of flag:
        if (number % 360 >= 180):
            led_colour[number] = yellow
def Germany():
    for i in range(len(led_colour)):
        if i % 360 <= 120:
            led_colour[i] = grey
        if (i % 360 >= 120) and (i % 360 < 240):
            led_colour[i] = red
   
        if (i % 360 >= 240) and (i % 360 < 360):
            led_colour[i] = yellow

def options(): 
    
    print('\nEnter the number of the flag you wish to be displayed:')
    print('\n1. Palestine\n2. England\n3. Ireland\n4. Ukraine\n5. Germany')
    x = int(input()) #the value from the user is an integer
    while(x not in (1,2,3,4,5)):
        
        print('\nPlease enter a value between 1-5!\n')
        x = int(input()) 
    
    if x == 1:
        return Palestine()
    
        
    elif x==2:
        return England()
    elif x==3:
        return Ireland()
    elif x==4:
        return Ukraine()
    elif x==5:
        return Germany()
def user():
    print("Which country are you currently in")
    z=input()
    print("What is the weather in", z)
    print("Is it \n1 Rainy.\n2 Sunny\n3. Cloudy\n")
    weather=input()
    if weather=='Rainy' or 'rainy':
        print("As Usual")
        screen = [black]*360
        client.put_pixels(screen)
        
        for i in range(0,360):
            
            if i%2 ==0:
                
                screen[i] = blue
                sleep(0.1)
                client.put_pixels(screen)
                
    elif weather=='Sunny' or 'sunny':
        print("Nice")
        screen = [black]*360
        client.put_pixels(screen)
        
        for i in range(0,360):
            
            if i%2 ==0:
                
                screen[i] = yellow
                sleep(0.1)
                client.put_pixels(screen)
while True:
    options()
    client.put_pixels(led_colour) 
    
    
    client.put_pixels(led_colour)
    sleep(1)
    
    user()
    #break #till now that is the end of the animation

