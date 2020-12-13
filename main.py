import time
import random
import microcontroller
import pulseio
import board
from adafruit_circuitplayground.express import cpx
from adafruit_motor import servo
import touchio

# A4 is touch sensitive
touch_A4 = touchio.TouchIn(board.A4)

# create a PWMOut object on Pin A1
pwm = pulseio.PWMOut(board.A1, frequency=50)

# Create a servo object, my_servo
my_servo = servo.Servo(pwm)

while True:
    if touch_A4.value:
        time.sleep(2)
        cpx.play_file("waytogo.wav")
        for angle in range(25,85): # 0 to 49 degrees in 1 deg steps
            my_servo.angle = angle
            time.sleep(0.01)  # Tiny delay each step
        time.sleep(1)
        for angle in range(85, 25, -1):
            my_servo.angle = angle
            time.sleep(0.01)
        time.sleep(1)
        for angle in range(25,85): # 0 to 49 degrees in 1 deg steps
            my_servo.angle = angle
            time.sleep(0.01)  # Tiny delay each step
        time.sleep(1)
        for angle in range(85, 25, -1):
            my_servo.angle = angle
            time.sleep(0.01)
        time.sleep(1)

# Below is all of the original code.
# This is a special command that will cause a single-press RESET to go
# into bootloader more (instead of double-click) to make it easier for
# MakeCode-rs who don't intend to use CircuitPython!
# microcontroller.on_next_reset(microcontroller.RunMode.BOOTLOADER)

# Set this to True to turn on the capacitive touch tones
# TOUCH_PIANO = False

# NeoPixel color names
# WHITE = (50, 50, 50)
# OFF   = (0,   0,  0)

# Not too bright!
# cpx.pixels.brightness = 0.3

# def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
#     if (pos < 0) or (pos > 255):
#         return (0, 0, 0)
#     if pos < 85:
#         return (int(255 - pos*3), int(pos*3), 0)
#     elif pos < 170:
#         pos -= 85
#         return (0, int(255 - (pos*3)), int(pos*3))
#     else:
#         pos -= 170
#     return (int(pos*3), 0, int(255 - pos*3))

# cpx.play_file("Coin.wav")   # Play a coin sound on boot

# Set up the accelerometer to detect tapping
# cpx.detect_taps = 1    # detect single tap only

# Our counter for all 10 pixels
# pixeln = 0
# We can tell the switch changed
# last_switch = cpx.switch

# while True:
#     cpx.red_led = True                  # Turns the little LED next to USB on

#     if cpx.tapped:     # Look for a single tap
#         if random.randint(0, 1) == 0:   # Play one of two sounds...
#             cpx.play_file("Coin.wav")
#         else:
#             cpx.play_file("Wild Eep.wav")

    # This math makes a 'comet' of swirling rainbow colors!
#     for p in range(10):
#         color = wheel(25 * ((pixeln + p)%10))
#         cpx.pixels[p] = [int(c * ( (10 - (pixeln+p)%10)) / 10.0) for c in color]

#     cpx.red_led = False    # turn off the LED

    # Each time 'round we tick off one pixel at a time
#     if cpx.switch:      # depending on the switch we'll go clockwise
#         pixeln += 1
#         if pixeln > 9:
#             pixeln = 0
#     else:               # or counter clockwise
#         pixeln -= 1
#         if pixeln < 0:
#             pixeln = 9

#     if pixeln == 0:   # Every time we go around, print sensor data
#         print("Temperature: %0.1f *C" % cpx.temperature)
#         print("Light Level: %d" % cpx.light)
#         x, y, z = cpx.acceleration
#         print("Accelerometer: (%0.1f, %0.1f, %0.1f) m/s^2" % (x, y, z))
#         print('-' * 40)

    # Depending on the buttons, make it dimmer
#    if cpx.button_a:
#        print("Button A pressed")
#        cpx.pixels.brightness = 0.1
    # or brighter!
#    if cpx.button_b:
#        print("Button B pressed")
#        cpx.pixels.brightness = 0.5
    # neither buttons pressed
#     if not cpx.button_a and not cpx.button_b:
#         cpx.pixels.brightness = 0.3

    # Check the switch
#     if cpx.switch:
#         if last_switch != cpx.switch: # if it moved, print it out
#             print("Switch moved left")
#     else:
#         if last_switch != cpx.switch:
#             print("Switch moved right")
#     last_switch = cpx.switch

#     if TOUCH_PIANO:
#         if cpx.touch_A4:              #  If we set to play tones
#             cpx.start_tone(524)
#         elif cpx.touch_A5:
#             cpx.start_tone(588)
#         elif cpx.touch_A6:
#             cpx.start_tone(660)
#         elif cpx.touch_A7:
#             cpx.start_tone(698)
#         elif cpx.touch_A1:
#             cpx.start_tone(784)
#         elif cpx.touch_A2:
#             cpx.start_tone(880)
#         elif cpx.touch_A3:
#             cpx.start_tone(988)
#         else:
#             cpx.stop_tone()           # nothing touched? turn off the audio

    # loop to the beginning!