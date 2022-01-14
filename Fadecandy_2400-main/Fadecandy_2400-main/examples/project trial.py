x = input('''Welcome to the menu. Options are listed below:,
              \t 1.chase
              \t 2. plain yellow
              \t 3. Random RGB
              Type the number of your choice and press Enter.''') #\n - newline; \t - tab
import opc
import time
import random

#defining variables
mix=[(175,255,50)]*360
red= [ (255,0,0)] *360
client = opc.Client('localhost:7890')
numLEDs= 360

#defining functions and what they do 
def color(val):
    
    
   client.put_pixels(mix)

time.sleep(1)
def chase(val):
    
        
    for i in range(numLEDs):
        
            pixels = [ (0,0,255)] * numLEDs #print blue on all the leds which is 360
        
            pixels[i] = (255, 0, 0) #make a single red led move through all
            client.put_pixels(pixels)
            time.sleep(0.05)
    
def rgb(val):
    while True:
        
        my_pixels = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]*120
        random.shuffle(my_pixels)
       
        if client.put_pixels(my_pixels, channel=0):
            
            
            time.sleep(0.3)
    


while True:
    if x.isdigit() == True: # .isdigit() 
        x = int(x)
        if x>3 or x<1:
            
            x = input("please input a number between 1 and 3. ")
            continue
        else:
            

            break # on correct value datatype: exit the loop
    else:
        x=input("invalid input, please provide an integer:") #ask for a new value
#print("The converted is:", value)
#print(f'it is of type {type(value)}.')
#compare numeric value to choices available, perform assicoated function or sequence.
if x == 1:
    print(chase(x))
elif x == 2:
    print(color(x))
elif x == 3:
    print ('Merry Christmas')
    print(rgb(x))
    

if x>3 or x<1:
    x = input("please input a number between 1 and 3. ")
