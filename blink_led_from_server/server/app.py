from flask import Flask
from time import sleep
import RPi.GPIO as GPIO

# Configure flask
app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial = GPIO.LOW)

def led_blink():
    out_pin = 8
    current_pin_state = 0
    blink_cycles = 30

    for i in range(blink_cycles):
        if (current_pin_state == 0):
            GPIO.output(out_pin, GPIO.HIGH)
            current_pin_state = 1
        
        else:
            GPIO.output(out_pin, GPIO.LOW)
            current_pin_state = 0
        
        sleep(0.2)
        

    return

@app.route("/")
def hello_world():
    print("Home page accessed")
    led_blink()
    return "<p>hello world</p>"