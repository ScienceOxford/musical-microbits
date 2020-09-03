from microbit import *
import radio
import music
import neopixel
import random

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

radio.on()
np = neopixel.NeoPixel(pin0, 5)

while True:
    if button_b.was_pressed():
        radio.off()
        for repeat in range(0,5):
            pin2.write_analog(90)
            sleep(500)
            pin2.write_analog(50)
            sleep(500)
        pin2.write_digital(0)
        radio.on()
    red = random.randint(0, 60)
    green = random.randint(0, 60)
    blue = random.randint(0, 60)
    sleep(100)
    message = radio.receive()
    try:
        music.play(message, pin1)
        for pixel_id in range(0, 5):
            np[pixel_id] = (red, green, blue)
        np.show()
    except:
        music.play("R:4", pin1)
