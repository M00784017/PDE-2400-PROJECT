#!C:\Users\obliq\AppData\Local\Programs\Python\Python310\python.exe
import opc #imports the simulator
from time import sleep #we just need sleep from time
import colorsys
import random
import numpy
import os
import sys

led_colour=[(0,0,0)]*360
led_colour1=[(0,0,0)]*20
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

#defining colour numbers in rgb
grey=(100,100,100)  #dark grey color number 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
orange=(255,165,0)
yellow=(255,255,0)
blue=(0,0,255)
light_blue=(173, 216, 230)
client = opc.Client('localhost:7890') #connects to simulator
s = 1 #saturation max 1.0 so i don't have to redefine calculations as floating point later on 
v = 0.8 #value max 
pixels = [] #start empty
numLEDs=360
#FOR MOREANIMATIONS FUNCTION
client = opc.Client('localhost:7890')
value=[(-2, 0.05), (-2, 0.15), (-1, 0.25), (0, 0.40), (1, 0.1), (2, 0.01)] #the higher the values, the more the screen becomes whiter
speed = value
fade = [(0, 0.75), (1, 0.5), (2, 0.25), ]# incrementing by 1, -0.25


new_leds=numLEDs*6%64

def Palestine():
    for i in range(len(led_colour)):
        if i in P:
            led_colour[i] = red
            sleep(0.01)
        if i in A:
            led_colour[i] = grey #although the palestine flag is black instead of grey here, I put dark grey because black will not appear.
            sleep(0.01)
        if i in L:
            led_colour[i] = grey
            sleep(0.01)
        if i in S:
            led_colour[i] = white
            sleep(0.01)
        if i in T:
            led_colour[i] = white
            sleep(0.01)
        if i in I:
            led_colour[i] = green
            sleep(0.01)
        if i in E:
            led_colour[i] = green
            sleep(0.01)
        client.put_pixels(led_colour)
    print("CAPITAL CITY OF PALESTINE IS : ALQUDS")
        
def England(): #I have made this to minimize use of code, I know its not ideal, but hopefully I will do something better   
    led=0
    for i in range (len(led_colour)):
            
        if i >= 20 and i <=40 or i>=80 and i<=100 or i>=140 and i<=160 or i>= 260 and i<=280 or i>=320 and i<=340 :
            led_colour[i] = (255,255,255) #returns all white at first
       
        if i >= 140 and i <=160 or i >= 200 and i <= 220 or i>=28 and i<=32 or i>=88 and i<=92 or i>=148 and i<=152 or i>=208 and i<=212 or i>=268 and i<=272 or i>=328 and i<=332  :
            led_colour[i] = (255,0,0) 
        
        
            
            client.put_pixels(led_colour)
                             
        client.put_pixels(led_colour)
        sleep(0.01)
    print("CAPITAL CITY OF ENGLAND IS : LONDON")
def Ireland():
    led=0
    while led<20:
        for rows in range(6):
            led_colour[led + rows*60] = (0,255,0)
            led_colour[59 -led + rows*60] = (255,160,50) 
        client.put_pixels(led_colour)
        sleep(0.1)
        led = led + 1 
        
    led=20
    while led>=20 and led<30 :
        for rows in range(6):
        	led_colour[led + rows*60] = (255,255,255)
        	led_colour[59-led + rows*60] = (255,255,255)
         
        client.put_pixels(led_colour)
        sleep(0.1)
        led = led + 1 #or reverse if you want
    led=40
    while led>40 :
        for rows in range(6):
            led_colour[led + rows*60] = (255,165,100)
         
        client.put_pixels(led_colour)
        sleep(0.1)
        led = led + 1 
    print("CAPITAL CITY OF IRELAND IS : DUBLIN")
def Ukraine():
    led = 0
    #sleep(1)
    while led<120:
        for rows in range(1,4):
            led_colour[led + rows*60] = (0,0,255)
            led_colour[59 -led + rows*60] = (0,0,255)
        client.put_pixels(led_colour)
        sleep(0.1)
        led = led + 1

    led = 0
    while led>=0 and led <120: 
        for rows in range(4,5):
            led_colour[led + rows*60] = (255,255,0)
            led_colour[59-led + rows*60] = (255,255,0)
            client.put_pixels(led_colour)
            sleep(0.07)
            led = led+1

    print("CAPITAL CITY OF UKRAIN IS : KIEV")

def Germany():
    led = 0
    sleep(1)
    while led<40:
        for rows in range(2):
            led_colour[led + rows*60] = (100,100,100)
            led_colour[59 -led + rows*60] = (100,100,100)
        client.put_pixels(led_colour)
        sleep(0.1)
        led = led + 1#or reverse if you want

    led = 0
    while led>=0 and led <60: #scroll all rows at the same time
        for rows in range(2,3):
            led_colour[led + rows*60] = (255,0,0)
            led_colour[119 -led + rows*60] = (255,0,0)
            client.put_pixels(led_colour)
            sleep(0.1)
            led = led +1
            
    led = 0
    while led>=0 and led <120: 
        for rows in range(5,6):
            #led_colour[led + rows*60] = (255,255,0)
            led_colour[59-led + rows*60] = (255,255,0)
            client.put_pixels(led_colour)
            sleep(0.1)
            led = led+1
    print("CAPITAL CITY OF GERMANY IS : BERLIN")

  
def Armenia():
    led = 0

    while led < 60 :#scroll all rows at the same time
        for rows in range (2): #first 2 rows
            led_colour[59-led + rows * 60] = (255,0,0)
        for rows in range (2,4): #second 2 rows
            led_colour[led + rows * 60] = (0,0,255)
        for rows in range (4,6): #third 2 rows
            led_colour[59-led + rows * 60] = (255,165,0)
        client.put_pixels(led_colour)
        sleep(0.1)
        led = led + 1
    print("CAPITAL CITY OF ARMENIA IS : YEREVAN")
def Brazil():
    led=0
    
    
        
    for i in range (len(led_colour)):
                
        if i >= 0 :
            led_colour[i] = (0,180,0) #returns all green at first
       
        if i >= 140 and i <=160 or i >= 82 and i <= 98 or i>=25 and i<=35 or i>=200 and i<=220 or i>=262 and i<=278 or i>=325 and i<=335  :
            led_colour[i] = (255,200,0) 
            
        if i>= 89 and i<=92 or  i>=148 and i<=153 or i>=208 and i<=213 or i>=269 and i<=272:
            led_colour[i]=(0,0,255)
            
            client.put_pixels(led_colour)
                
                
                
                     
        client.put_pixels(led_colour)
        sleep(0.01)
    print("CAPITAL CITY OF Brazil IS : Brasília")
def options(): 
    
    print('\nEnter the number of the flag you wish to be displayed:')
    print('\n1. Palestine\n2. England\n3. Ireland\n4. Ukraine\n5. Germany\n6. Armenia\n7. Brazil\n8. exit')
   # x = (input()) #the value from the user is an integer
    while True:
        x= input('Please enter a number between 1 and 8')
        try:
            x = int(x) #exception catch - if value isn't integer, go to except:
            if x <1 or x > 8: #value validation:
                print('') #if not from the list:
             #return to top of while and ask again
            else: #if correct value:
                print(f'your value is {x} and its type is {type(x)}') #print a response, optional
                break # exit while loop. Value remains.
        except ValueError:
            if x == 'one':
                 x = 1
                 break
            elif x == 'two':
                   x = 2
                   break
            elif x == 'three':
                  x = 3
                  break
            elif x == 'four':
                  x = 4
                  break
            elif x == 'five':
                  x = 5
                  break
            elif x == 'six':
                  x = 6
                  break
            elif x == 'seven':
                  x = 7
                  break
            elif x == 'eight':
                  x = 8
                  break
        
        

    
    if x == 1:
        return Palestine()
        
        
    elif x==2 :
        return England()
    elif x==3:
        return Ireland()
    elif x==4:
        return Ukraine()
    elif x==5:
        return Germany()
    elif x==6:
        return Armenia()
    elif x==7:
        return Brazil()
    elif x==8:
        #os.execv(sys.argv[0], sys.argv) # does not work, should restart
        sys.exit() #closes script
        
def user():
    print("Which country are you currently in")
    z=(input())
    print("What is the weather in", z)
    
    print("Is it \n1 Rainy.\n2 Sunny\n3.Cloudy\n4.Rainbow\n5.Exit\n")
    
    while True:
        z = input('Please enter a number between 1 and 5')
        try:
            z = int(z) #exception catch - if value isn't integer, go to except:
            if z <1 or z > 5: #value validation:
                print('') #if not from the list:
                 #return to top of while and ask again
            else: #if correct value:
                print(f'your value is {z} and its type is {type(z)}') #print a response, optional
                break # exit while loop. Value remains.
        except ValueError:
            if z == 'one':
                 z = 1
                 break
            elif z == 'two':
                   z = 2
                   break
            elif z == 'three':
                  z = 3
                  break
            elif z == 'four':
                  z = 4
                  break
            elif z == 'five':
                  z = 5
                  break
            #else:
                 # print('valid number, please') #prompt user again,
                  #continue #return to top of while loop.
    #continue with code based on value such as:
 
    #print("Is it \n1 Rainy.\n2 Sunny\n3.Cloudy\n4.Rainbow\n")
    #weather=(input())#only integers at the moment
    if z== 1 :
        print("As Usual")
        screen = [black]*360
        client.put_pixels(screen)
        
        for i in range(360):
            
            if i%3 ==0:
                
                screen[i] = blue
                sleep(0.01)
                client.put_pixels(screen)
                
    elif z== 2 :
        print("Nice")
        screen = [black]*360
        client.put_pixels(screen)
        
        for i in range(360):
            
            if i%3 ==0:
                
                screen[i] = yellow
                sleep(0.01)
                client.put_pixels(screen)

    elif z== 3 :
        print("Cool")
        screen = [black]*360
        client.put_pixels(screen)
        
        for iterate in range(6):
	        for i in range(60*iterate, 60*iterate+60): # 0-59, 60-119, 120-179, 180-239, 240-299, 300-359
	            
	            if i%3 ==0:
	                
	                screen[i] = light_blue
	                sleep(0.05)
	        #numpy.roll(screen, 1) #move every element 2 spaces forward
	        client.put_pixels(screen)

    elif z==4:
        print('Rainbow!!!!')
        for hue in range(360):
            
            
            rgb_fractional = colorsys.hsv_to_rgb(hue/360.0, s, v) 
             

            r_float = rgb_fractional[0] #extract said floating point numbers
            g_float = rgb_fractional[1]
            b_float = rgb_fractional[2]

    

            rgb = (r_float*176, g_float*200, b_float*255) 
            pixels.append(rgb)
            
                        
            client.put_pixels(pixels)
            sleep(0.01) #speed control
    elif z==5:
        sys.exit()
def MoreAnimations():
    print("This is the last set of animations. Please Select which animation you would like to see")
    print("\n1 RGB Fading.\n2 Fading movement\n3.Police\n4.Exit")
    while True:
            T = input('Please enter a number between 1 and 4')
            try:
                T = int(T) #exception catch - if value isn't integer, go to except:
                if T <1 or T > 4: #value validation:
                    print('') #if not from the list:
                 #return to top of while and ask again
                else: #if correct value:
                    print(f'your value is {T} and its type is {type(T)}') #print a response, optional
                    break # exit while loop. Value remains.
            except ValueError:
                if T == 'one':
                     T = 1
                     break
                elif T == 'two':
                       T = 2
                       break
                elif T == 'three':
                      T = 3
                      break
                elif T == 'four':
                      T = 4
                      break

    if T==1:
        colors=[]
        for i in range(0,255):
            rgb = colorsys.hsv_to_rgb(i/360.0, s, v) #colorsys returns floats between 0 and 1
            r = rgb[0] 
            g = rgb[1]
            b = rgb[2]
            colors.append((r,g,b))
            rgb = (r*255, g*255, b*255) #creates a new tuple
            client.put_pixels([rgb] *numLEDs) #put the pixels in the simulator

            sleep(0.1) 

        
        

    elif T==2:
        
        pixels = [ (0,0,0) ] * numLEDs
        while True:
            
            new_pixels = list(pixels)
            
            for i in range(numLEDs):
                pixels.append(i)
                r, g, b = (0, 0, 0)
                
                for gradiant, deg in speed:
                    
                    j = (numLEDs+gradiant+i) % numLEDs
                    fade_amount= pixels[j][1]
                    r = r + fade_amount*deg
                    g = g + fade_amount*deg
                    b = b + fade_amount*deg
                new_pixels[i] = max(2, min(255, r)), max(2, min(255, g)), max(2, min(255, b))
                fade_amount=fade_amount +1
            for x in range(360):
               if (random.randint(0,6) == 0) is True and speed==value:
                    
                    movement = random.randint(0, 360)
                    drop = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
                    for gradiant, deg in fade:
                        i = (gradiant + movement) % 360 #360 to cover all leds
                        color = []
                        for c in 0, 1, 2:
                            color.append(drop[c]*deg + new_pixels[i][c]*(1-deg))
                            
                        new_pixels[i] = tuple(color)
            pixels = new_pixels
            client.put_pixels(pixels)
            sleep(0.4) #can be adjusted to make it faster or slower
    elif T==3:
        while True:
    
            for x in range (len(led_colour1)):
                pixels = []
                if x % 2 == 0:
                    while(len(pixels) <= 360):
                        pixels = pixels + ([red if x % 3 == 0 else blue]*16)
                        pixels = pixels + ([blue if x % 3 == 0 else red]*16)

                else:
                    pixels = [green]*360
                client.put_pixels(pixels)
                sleep(0.1)




            for x in range (len(led_colour1)):
                pixels = []
                if int((x % (len(led_colour1)))*8) %2 ==0:
                    if x%2 == 0:
                        pixels = [blue]*360
                    elif x%2==1:
                        pixels = [red]*360        #blinks blue and red after each other
                        
                        
               
                client.put_pixels(pixels)
                sleep(0.1)

            for cycles in range(len(led_colour1)):
                cycles = 0
                if cycles==10:
                    break
                else:
                    continue
                        
                break

    elif T==4:
        
        sys.exit() #closes script


        

while True:
    options()
    client.put_pixels(led_colour) 
    
    
    client.put_pixels(led_colour)
    sleep(1)
    
    user()
    sleep(1)
    MoreAnimations()
   
    

