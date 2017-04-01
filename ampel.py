import machine
from time import sleep

d1_fuss_rot = machine.Pin(5, machine.Pin.OUT)
d2_fuss_gruen = machine.Pin(4, machine.Pin.OUT)

d8_rot = machine.Pin(15, machine.Pin.OUT)
d7_gelb = machine.Pin(13, machine.Pin.OUT)
d6_gruen = machine.Pin(12, machine.Pin.OUT)

def fuss_rot():
    d1_fuss_rot(1)
    d2_fuss_gruen(0)

def fuss_gruen():
    d1_fuss_rot(0)
    d2_fuss_gruen(1)

def auto_gruen():
    print("auto gruen")
    d8_rot(0)
    d7_gelb(1)
    sleep(1)
    d7_gelb(0)
    d6_gruen(1)

def auto_rot():
    print("auto rot")
    d6_gruen(0)
    d7_gelb(1)
    sleep(1)
    d7_gelb(0)
    d8_rot(1)

def init()
    fuss_rot()
    d8_rot(1)
