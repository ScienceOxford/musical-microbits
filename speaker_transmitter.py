from microbit import *
import radio

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

radio.on()

while True:
    radio.send("A2:4")
    sleep(1)
    radio.send("R:2")
    sleep(1)
    radio.send("B1:2")
    sleep(1)
    radio.send("C5:4")
    sleep(1)
    radio.send("ZFA")
    sleep(1)
