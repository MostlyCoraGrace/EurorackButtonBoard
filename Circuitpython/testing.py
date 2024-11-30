import board
import digitalio
from time import sleep

pin1 = board.D1
pin2 = board.D2
button1 = digitalio.DigitalInOut(pin1)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(pin2)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

while True:
    if not button1.value:
        print("Yes")
    else:
        if not button2.value:
            print("YYes")
        else:
            print("No")
    sleep(0.1)
