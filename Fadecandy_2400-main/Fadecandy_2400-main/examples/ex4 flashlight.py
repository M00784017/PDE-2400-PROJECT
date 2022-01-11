import opc, time, math

numLEDs = 360
numLEDs1 = 360
client = opc.Client('localhost:7890')

t = 0

while True:
    t += 0.5
    brightness = int(min(1, 1.25 + math.sin(t)) * 255)
    frame = [ (brightness, brightness, brightness) ] * numLEDs
    frame1=[ (brightness, brightness, brightness) ] * numLEDs1
    client.put_pixels(frame)
    client.put_pixels(frame1)
    
    
    time.sleep(0.5) 
                            
	
