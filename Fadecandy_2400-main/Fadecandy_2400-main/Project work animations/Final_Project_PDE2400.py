#!C:\Users\obliq\AppData\Local\Programs\Python\Python310\python.exe
import opc #imports the simulator
from time import sleep #we just need sleep from time
import colorsys#used for rainbow animation
import random#to assign random numbers and colours and in shuffling
import numpy#to shift
import os#used for exit 
import sys#used for exit

led_colour=[(0,0,0)]*360
led_colour1=[(0,0,0)]*20
led_colour3=[(0,0,0)]*360# I have 3 variables with the same value because it gets in the way when one animation using the same variable transitions to the other set of animations with the same variable.
# The numbers in each letter represent a pixel in the simulator 60*6
P = [0,1,2,3,60,61,62,63,64,120,121,122,123,124,125,180,181,182,183,184,185,240,241,242,243,244,300,301,302,303] 
A = range(4,60) 
L = range(65,120)
S = range(186,240)
T=range(126,180)
I = range(245,300)
N=range(302,330)
E=range(304,360)
led_colour2=[(0,0,0)]*360
#defining colour numbers in rgb
grey=(100,100,100)  #dark grey color number in rgb
black = (0,0,0)#black color number in rgb
white = (255,255,255)#white color number in rgb
red = (255,0,0)#red color number in rgb
green = (0,255,0)#green color number in rgb
orange=(255,165,0)#orange color number in rgb
yellow=(255,255,0)#yellow color number in rgb
blue=(0,0,255)#blue color number in rgb
light_blue=(173, 216, 230)#light_blue color number in rgb
client = opc.Client('localhost:7890') #connects to simulator
s = 1 #saturation max 1.0 so i don't have to redefine calculations as floating point later on 
v = 1 #value max 
pixels = [] #start empty
numLEDs=360#number of leds available in the simulator
#FOR MOREANIMATIONS FUNCTION
client = opc.Client('localhost:7890')




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
            led_colour[i] = white#adds white colour leds in range
            sleep(0.01)
        if i in T:
            led_colour[i] = white
            sleep(0.01)
        if i in I:
            led_colour[i] = green#adds green colour leds in range
            sleep(0.01)
        if i in E:
            led_colour[i] = green
            sleep(0.01)
        
        client.put_pixels(led_colour)

            
    print("CAPITAL CITY OF PALESTINE IS : ALQUDS") #prints the capital city for the chosen country
        
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
    print("CAPITAL CITY OF ENGLAND IS : LONDON")#prints the capital city for the chosen country
def Ireland():
    led=0
    while led<20:
        for rows in range(6):
            led_colour[led + rows*60] = (0,255,0)#sends green to the first 20 leds in each row
            led_colour[59 -led + rows*60] = (255,160,50) 
        client.put_pixels(led_colour)
        sleep(0.1)
        led = led + 1 
        
    led=20
    while led>=20 and led<30 :
        for rows in range(6):
        	led_colour[led + rows*60] = (255,255,255)#when the animation reaches the middle 20 flags, send white in the middle
        	led_colour[59-led + rows*60] = (255,255,255)#from both directions
         
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
    print("CAPITAL CITY OF IRELAND IS : DUBLIN")#prints the capital city for the chosen country
def Ukraine():
    led = 0
    #sleep(1)
    while led<120:
        for rows in range(1,4):
            led_colour[led + rows*60] = (0,0,255)#animate blue for the rows between 1 and 4
            led_colour[59 -led + rows*60] = (0,0,255)
        client.put_pixels(led_colour)
        sleep(0.1)
        led = led + 1

    led = 0
    while led>=0 and led <120: 
        for rows in range(4,5):
            led_colour[led + rows*60] = (255,255,0)#this sends out yellow colour when blue is finished, to complete the flag
            led_colour[59-led + rows*60] = (255,255,0)
            client.put_pixels(led_colour)
            sleep(0.03)
            led = led+1

    print("CAPITAL CITY OF UKRAINE IS : KIEV")#prints the capital city for the chosen country

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
            led_colour[119 -led + rows*60] = (255,0,0)#two lines of red leds cross each other
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
    print("CAPITAL CITY OF GERMANY IS : BERLIN")#prints the capital city for the chosen country

  
def Armenia():
    led = 0

    while led < 60 :#scroll all rows at the same time
        for rows in range (2): #first 2 rows
            led_colour[59-led + rows * 60] = (255,0,0) #2 red rows scroll from the right to left
        for rows in range (2,4): #second 2 rows
            led_colour[led + rows * 60] = (0,0,255)#the 2 blue rows in the middle scroll from the left to right
        for rows in range (4,6): #third 2 rows
            led_colour[59-led + rows * 60] = (255,165,0)#2 orange rows scroll from the right to left
        client.put_pixels(led_colour)
        sleep(0.1)
        led = led + 1#increment by 1
    print("CAPITAL CITY OF ARMENIA IS : YEREVAN")#prints the capital city for the chosen country
def Brazil():
    led=0
    
    
        
    for i in range (len(led_colour)):
                
        if i >= 0 :
            led_colour[i] = (0,180,0) #returns all green at first
       
        if i >= 140 and i <=160 or i >= 82 and i <= 98 or i>=25 and i<=35 or i>=200 and i<=220 or i>=262 and i<=278 or i>=325 and i<=335  : #if led is within the range specified
            led_colour[i] = (255,200,0) #add yellow
            
        if i>= 89 and i<=92 or  i>=148 and i<=153 or i>=208 and i<=213 or i>=269 and i<=272:#if led is within the range specified
            led_colour[i]=(0,0,255)#add blue
            
            client.put_pixels(led_colour)
                
                
                
                     
        client.put_pixels(led_colour)
        sleep(0.01)
    print("CAPITAL CITY OF BRAZIL IS : Brasília")#prints the capital city for the chosen country


def options(): 
    
    print('\nEnter the number of the flag you wish to be displayed, eg:for Germany Flag, enter "five" or "5" all lower case. ') #asks the user to input their chosen animation 
    print('\n1. Palestine\n2. England\n3. Ireland\n4. Ukraine\n5. Germany\n6. Armenia\n7. Brazil\n8. Exit\n9. Restart')#available options
   
    while True:
        x= input('Please enter a number between 1 and 9: ')
        try:
            x = int(x) #exception catch - if value isn't integer, go to except:
            if x <1 or x > 9: #value validation:
                print('') #if not from the list:
             #return to top of while and ask again
            else: #if correct value:
                print(f'your value is {x} and its type is {type(x)}')#prints the data type if its a number
                break # exits while loop while keeeping value.
        except ValueError:
            if x == 'one':#check if input entered can be translated to an in-range integer
                 x = 1
                 break#if yes allow it 
            elif x == 'two':#check if input entered can be translated to an in-range integer
                   x = 2
                   break#if yes allow it 
            elif x == 'three':#check if input entered can be translated to an in-range integer
                  x = 3
                  break#if yes allow it 
            elif x == 'four':#check if input entered can be translated to an in-range integer
                  x = 4
                  break#if yes allow it  
            elif x == 'five':#check if input entered can be translated to an in-range integer
                  x = 5
                  break#if yes allow it 
            elif x == 'six':#check if input entered can be translated to an in-range integer
                  x = 6
                  break#if yes allow it 
            elif x == 'seven':#check if input entered can be translated to an in-range integer
                  x = 7
                  break#if yes allow it 
            elif x == 'eight':#check if input entered can be translated to an in-range integer
                  x = 8
                  break#if yes allow it 
            elif x=='nine':#check if input entered can be translated to an in-range integer
                x=9
                break#if yes allow it

            
        
        

    
    if x == 1: #if the user choses this value
        return Palestine()#returns function with the defined flag      
    elif x==2 :#if the user choses this value
        return England()#returns function with the defined flag
    elif x==3:#if the user choses this value
        return Ireland()#returns function with the defined flag
    elif x==4:#if the user choses this value
        return Ukraine()#returns function with the defined flag
    elif x==5:#if the user choses this value
        return Germany()#returns function with the defined flag
    elif x==6:#if the user choses this value
        return Armenia()#returns function with the defined flag
    elif x==7:#if the user choses this value
        return Brazil()#returns function with the defined flag
    elif x==8:#if the user choses this value
        sys.exit() #closes script
    elif x==9:#if the user choses this value
        #os.execv(sys.executable, ['python'] + sys.argv) does not work
        #os.execv(sys.argv[0], sys.argv) # does not work, should restart
        print(" Restarted Sucessfully ")#for confirmation purposes
        
        options()#resets the program
        
        
def user():
    print("Which country are you currently in?")#asks the user for the country
    z=(input())#input of the user
    
    if z.isdigit()==False:#if the input is not a digit, allow it to continue 
        print("What is the weather in", z)
        
        
    else:#if input is a number, ask for a valid word
        print("Please enter a valid word")
        return user() #repeats the question
        
    
        
   
    
    print("Is it \n1 Rainy.\n2 Sunny\n3.Cloudy\n4.Rainbow\n5.Exit\n6.Restart\n")
    
    while True:
        z = input('Please enter a number between 1 and 6: ')
        try:
            z = int(z) #exception catch - if value isn't integer, go to except:
            if z <1 or z > 6: #value validation:
                print('') #if not from the list:
                 #return to top of while and ask again
            else: #if correct value:
                print(f'your value is {z} and its type is {type(z)}') #prints the data type if its a number
                break # exits while loop while keeeping value.
        except ValueError: #exception values that can be allowed
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
            elif z=='six':
                z = 6
                break

    if z== 1 :
        print("As Usual")
        screen = [black]*360
        client.put_pixels(screen)
        
        for i in range(360):#for all leds within the range
            
            if i%3 ==0:#every 2 pixels
                
                #screen[i] = blue#add color blue to the leds
                led_colour2[i] = (random.randint(0, 0), random.randint(0, 100), random.randint(150, 255))  #chose a random colour close to the range of blue
                led_colour2[-i] = (random.randint(0, 0), random.randint(0, 100), random.randint(150, 255)) # -i is for the animation to go the opposite direction in this part
                sleep(0.02)#for speed
                client.put_pixels(led_colour2)#put leds in simulator

                
    elif z== 2 :
        print("Nice")
        screen = [black]*360
        client.put_pixels(screen)
        
        for i in range(360):
            
            if i%3 ==0:#every 3 pixels
                screen[i] = yellow
                led_colour2[179-i] = yellow  #start from the middle of the simulator
                led_colour2[i] = yellow #add yellow to indv. pixs
                sleep(0.02)#for speed
                client.put_pixels(led_colour2)
                
                

    elif z== 3 :
        print("Cool")
        screen = [black]*360
        client.put_pixels(screen)
        
        for iterate in range(6):
	        for i in range(60*iterate, 60*iterate+60): # 0-59, 60-119, 120-179, 180-239, 240-299, 300-359
	            
	            if i%3 ==0:
	                
	                screen[i] = light_blue#add light blue colour to leds
	                sleep(0.05)
	        numpy.roll(screen, 2) #move every element 2 spaces forward
	        client.put_pixels(screen)

    elif z==4:
        print('Rainbow!!!!')
        for i in range(360):
            
            
            rgb_fractional = colorsys.hsv_to_rgb(i/360.0, s, v) 
             

            r = rgb_fractional[0] #extract said floating point numbers
            g = rgb_fractional[1]
            b = rgb_fractional[2]

    

            rgb = (r*random.randint(100,200), g*random.randint(150,200), b*random.randint(170,255)) #random colours between a range that makes sense for a rainbow
            pixels.append(rgb)
            
                        
            client.put_pixels(pixels)
            sleep(0.01) #speed control
    elif z==5:
        sys.exit()
    elif z==6:
        print(" Restarted Sucessfully ")
        options()#resets the program
        user()
def MoreAnimations():
    print("This is the last set of animations. Please Select which animation you would like to see")
    print("\n1 RGB Fading.\n2 Netherlands Flag\n3.Police\n4.Scrlloing Colours\n5.Exit\n6.Restart")
    while True:
            T = input('Please enter a number between 1 and 6: ')
            try:
                T = int(T) #exception catch - if value isn't integer, go to except:
                if T <1 or T > 6: #value validation:
                    print('') #if not from the list:
                 #return to top of while and ask again
                else: #if correct value:
                    print(f'your value is {T} and its type is {type(T)}') #prints the data type if its a number
                    break # exits while loop while keeeping value.
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
                elif T=='five':
                    T=5
                    break
                elif T=='six':
                    T=6
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
        led = 30#for leds to start in the middle and then split up
    

        while led>=0:
            for rows in range(2):
                led_colour3[led + rows*60]= (230,0,0) 
                
                led_colour3 [59-led + rows*60] = (230, 0, 0) #first 2 rows in red
                
            for rows in range(2,4):
                led_colour3[led + rows*60]= (255,255,255) #middle 2 rows in red
                
                led_colour3 [59- led + rows*60] = (255,255,255) 
            for rows in range(4,6):
                led_colour3[led + rows*60]= (0,0,200) #last 2 rows in blue
                
                led_colour3 [59- led + rows*60] = (0,0,200) 

            for rows in range(6):
                
                led_colour3[led-40 + rows*60]= (0,0,0)#split them in 2 so that it becomes 2 flags and the middle part is empty
            
            
            client.put_pixels (led_colour3)
            sleep(0.09)
            led=led-1
        print("CAPITAL CITY OF NETHERLANDS IS : Amsterdam")#prints the capital city for the chosen country
        
            
    elif T==3:
        led=30
        while True:
            while led>=0:
                for rows in range(6):
                    led_colour3[led + rows*60]= (230,0,0) #send red colours in both directions
                    
                    led_colour3 [59-led + rows*60] = (230, 0, 0) #animate them so red moves from middle to left and right
                    
                

                for rows in range(6): #while still in range
                    
                    led_colour3[led-40 + rows*60]= (0,0,255)#send blue leds in the middle between the 2 red

                client.put_pixels (led_colour3)#send pixels to the server
                sleep(0.5)
                led=led-1
        
            
    #this part is for the blinking siren, red-blue, red-blue etc.

            for x in range (len(led_colour1)):
                pixels = []
                
                if x%2 == 1:#start by checking
                    pixels = [blue]*360 #fill simulator with blue
                elif x%2==0:
                    pixels = [red]*360        #blinks blue and red after each other
                        
                        
               
                client.put_pixels(pixels)
                sleep(0.25)

            for cycles in range(len(led_colour1)):
                cycles = 0
                cycles+=1
                if cycles==20:
                    break
                else:
                    continue
                            
            break #if the animation is done, repeat the script, allowing the user to exit if wanted
    elif T==4:
        led = 359
    

        while led>=60:
            for rows in range(2):
                #leds[led + rows*60]= (0,200,255) 
                
                led_colour3 [59-led + rows*60] = (255, 0, 0) 
                
                led_colour3 [119-led + rows*60] = (128,0,128)
                led_colour3 [179- led + rows*60] = (0,0,255)
                led_colour3 [239- led + rows*60] = (255,47,153)
                led_colour3 [299- led + rows*60] = (255,170,0)
                led_colour3 [359- led + rows*60] = (0,130,255)

            
            
            
            client.put_pixels (led_colour3)
            sleep(0.02)
            led=led-1
    elif T==5:
        
        sys.exit() #closes script
    elif T==6:
        print(" Restarted Sucessfully ")
        options()
        user()
        MoreAnimations()


        

while True:
    options()
    client.put_pixels(led_colour) 
    
    
    client.put_pixels(led_colour)
    sleep(1)
    
    user()
    sleep(1)
    MoreAnimations()
   
    

