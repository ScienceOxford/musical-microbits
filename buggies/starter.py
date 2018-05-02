from microbit import *

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

on = 511
off = 1023


def stop(time):
    pin14.write_analog(off)
    pin13.write_analog(off)
    pin12.write_analog(off)
    pin15.write_analog(off)
    sleep(time)


def forward(time):
    pin14.write_analog(on)
    pin13.write_analog(off)
    pin12.write_analog(on)
    pin15.write_analog(off)
    sleep(time)


def backward(time):
    pin14.write_analog(off)
    pin13.write_analog(on)
    pin12.write_analog(off)
    pin15.write_analog(on)
    sleep(time)

