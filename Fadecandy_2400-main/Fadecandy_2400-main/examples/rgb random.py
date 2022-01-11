import time
import random
import opc

ADDRESS = 'localhost:7890'

# Create a client object
client = opc.Client(ADDRESS)

# Test if it can connect
if client.can_connect():
    print ('connected to %s' % ADDRESS)
else:
    # We could exit here, but instead let's just print a warning
    # and then keep trying to send pixels in case the server
    # appears later
    print ('WARNING: could not connect to %s' % ADDRESS)

# Send pixels forever
while True:
    my_pixels = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]*120
    random.shuffle(my_pixels)
    if client.put_pixels(my_pixels, channel=0):
        print ('Merry Christmas')
    else:
        print( 'not connected')
    time.sleep(0.3)
