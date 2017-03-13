from machine import Timer
import ampel
from time import sleep 

i = 0

def callback(t):
    global i
    i = (i + 1) % 2
    if i == 0:
        ampel.auto_rot()
        sleep(1)
        ampel.fuss_gruen()
    else:
        ampel.fuss_rot()
        sleep(1)
        ampel.auto_gruen()

ampel.auto_rot()
tim = Timer(-1)
tim.init(period=10000, mode=Timer.PERIODIC, callback=callback)
