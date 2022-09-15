import RPi.GPIO as GPIO
from time import sleep

# This script is a basic test of GPIO, it makes an LED connected to GPIO14
# and ground blink on and off for 10 seconds.








if __name__ == "__main__":

    # Script vars
    out_pin = 8             # The pin sending the current
    current_pin_state = 0   # 0 = low, 1 = high

    # Configure GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(out_pin, GPIO.OUT, initial = GPIO.LOW)
    maximum_cycles = 20     # number of times current alternates

    # Script output start
    print("LED will start blinking in ")
    i = 5
    while (i > 0):
        print i
        i = i - 1
        sleep(1)

    # Alternating blinking cycles
    for j in range(maximum_cycles):
        sleep(0.5)
        print "Cycle number:", i
        # Turn current on
        if (current_pin_state == 0):
            print "Turning LED on..."
            GPIO.output(out_pin, GPIO.HIGH)
            current_pin_state = 1

        # Turn current off
        else:
            print "Turning LED off..."
            GPIO.output(out_pin, GPIO.LOW)
            current_pin_state = 0

        sleep(0.5)

    print "Script complete."