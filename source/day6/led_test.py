import RPi.GPIO as GPIO
import time

ledPins = [ 2,3,4]  

GPIO.setmode(GPIO.BCM)

for pin in ledPins:
    GPIO.setup(ledPins, GPIO.OUT)
    GPIO.setup(ledPins, GPIO.LOW)

try:
    for pin in ledPins:
        GPIO.output(ledPins, GPIO.HIGH)
        print(f"pin{ledPins}On")
        time.sleep(2)
        GPIO.output(ledPins, GPIO.LOW)
        time.sleep(1)
finally:
    GPIO.cleanup()
