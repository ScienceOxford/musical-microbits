from microbit import *
#Credit to ScienceOxford 

on = 511
off = 1023


def stop(time):
    pin14.write_digital(off)
    pin13.write_digital(off)
    pin12.write_digital(off)
    pin15.write_digital(off)
    sleep(time)


def forward(time):
    pin14.write_digital(on)
    pin13.write_digital(off)
    pin12.write_digital(on)
    pin15.write_digital(off)
    sleep(time)


def backward(time):
    pin14.write_digital(off)
    pin13.write_digital(on)
    pin12.write_digital(off)
    pin15.write_digital(on)
    sleep(time)


