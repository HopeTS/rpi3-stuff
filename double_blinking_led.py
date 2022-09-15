import RPi.GPIO as GPIO
from time import sleep

'''
    Blinking between a yellow and blue LED from two different circuits
'''

# global vars
yellow_led_pin = 8
blue_led_pin = 11

''' Configure GPIO and pins '''
def setup():
    # LED pin numbers
    global yellow_led_pin = 8
    global blue_led_pin = 11

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup([yellow_led_pin, blue_led_pin], GPIO.OUT, initial = GPIO.LOW)
    return 


''' Individual cycle of yellow / blue LED blink '''
def blink_cycle():
    print("Starting blink cycle...")
    GPIO.output(yellow_led_pin, GPIO.HIGH)
    sleep(0.2)
    GPIO.output(yellow_led_pin, GPIO.LOW)
    GPIO.output(blue_led_pin, GPIO.HIGH)
    sleep(0.2)
    GPIO.output(blue_led_pin, GPIO.LOW)
    return


if __name__ == "__main__":
    setup()

    for i in range(20):
        blink_cycle()

