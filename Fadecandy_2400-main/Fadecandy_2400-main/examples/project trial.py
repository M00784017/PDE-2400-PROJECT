value = input('''Welcome to the menu. Options are listed below:,
              \t 1.chase
              \t 2. plain yellow
              \t 3. Random RGB
              Type the number of your choice and press Enter.''') #\n - newline; \t - tab
import opc
import time
import random

yellow=[(255,255,0)]*360
red= [ (0,255,0)] *360
client = opc.Client('localhost:7890')
numLEDs= 360


def color(val):
    return client.put_pixels(yellow)

time.sleep(1)
def chase(val):
    
        
    for i in range(numLEDs):
        
            pixels = [ (0,0,255)] * numLEDs
        
            pixels[i] = (255, 0, 0)
            client.put_pixels(pixels)
            time.sleep(0.1)
    
    return client.put_pixels(pixels)
def rgb(val):
    while True:
        
        my_pixels = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]*120
        random.shuffle(my_pixels)
        
        if client.put_pixels(my_pixels, channel=0):
            
            print ('Merry Christmas')
            time.sleep(0.3)

    return my_pixels

while True:
    if value.isdigit() == True: # .isdigit() 
        value = int(value)
        if value>3 or value<1:
            
            value = input("please input a number between 1 and 3. ")
            continue
        else:
            

            break # on correct value datatype: exit the loop
    else:
        value=input("invalid input, please provide an integer:") #ask for a new value
#print("The converted is:", value)
#print(f'it is of type {type(value)}.')
#compare numeric value to choices available, perform assicoated function or sequence.
if value == 1:
    print(chase(value))
elif value == 2:
    print(color(value))
elif value == 3:
    print(rgb(value))

if value>3 or value<1:
    value = input("please input a number between 1 and 3. ")


