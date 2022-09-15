from flask import Flask
from time import sleep
import RPi.GPIO as GPIO

# Configure flask
app = Flask(__name__)

# Configure GPIO
global out_pin = 8                 # The pin sending the current
global current_pin_state = 0       # 0 = LOW, 1 = HIGH  
GPIO.setmode(GPIO.BOARD)
GPIO.setup(out_pin, GPIO.OUT, initial = GPIO.LOW)

def led_blink()
    for i in range(30):
        if (current_pin_state = 0):
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