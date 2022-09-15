import RPi.GPIO as GPIO
from pynput import keyboard

'''
    This script maps the GPIO14 pin on the RPi3B to the q key. When pressing q
    the pin is high, when not pressing q the pin is low.
'''

# Global vars
out_pin = 8             # The pin sending the current

# Configure GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(out_pin, GPIO.OUT, initial = GPIO.LOW)


def on_press(key):
    print "Key pressed", key.char

    if (key.char == "q"):
        print "Turning GPIO14 on..."
        GPIO.output(out_pin, GPIO.HIGH)
    return


def on_release(key):
    print "Key released", key.char

    if (key.char == "q"):
        print("Turning GPIO14 off...")
        GPIO.output(out_pin, GPIO.LOW)
    return

if __name__ == "__main__":
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()