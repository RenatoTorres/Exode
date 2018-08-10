from Exode import *

#List Exode Boards
comport = BOARD.search()

print('Available Exode Boards:')
print( comport )

# Connecting
print('Connecting on ' + comport[0] + '...')
uno = Board( comport[0] )

led = Led( 13 )
led.blink(100)