import  RPi.GPIO as GPIO
import time

swPin =14
ledPin = 15

GPIO.setmode(GPIO.BCM)

# 스위치 입력 설정 (풀업)
GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# LED 출력 설정 
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.LOW) # 처음에는 led 꺼둠 

def printcallback(channel):
    print("pushed")
    GPIO.output(ledPin, GPIO.HIGH) # led
    time.sleep(0.5) # 0.5초 동안 켜기
    GPIO.output(ledPin, GPIO.LOW) # led 끔 
    
# 이벤트 감지 등록 
GPIO.add_event_detect(swPin, GPIO.RISING, callback=printcallback, bouncetime=100)

try:
    while True:
        pass
except KeyboardInterrupt:
    GPIO.output(ledPin,GPIO.LOW)
    GPIO.setup(ledPin, GPIO.IN)
    GPIO.cleanup()
