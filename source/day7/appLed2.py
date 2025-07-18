from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

ledPin = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

@app.route('/')
def ledFlask():
    return "LED Control Web"

@app.route('/led/<state>') # state 여기에 on이나 off (사용자에 맞게)
def led(state):
    if state == 'on':
        GPIO.output(ledPin, GPIO.HIGH)
    else:
        GPIO.output(ledPin, GPIO.LOW)
    return "LED" + state

@app.route('/led/clean')
def gpioCleanup():
    GPIO.cleanup()
    return "<h1> GPIO CLEANUP </h1>"    

if __name__ == "__main__":
    app.run(host="0.0.0.0")
