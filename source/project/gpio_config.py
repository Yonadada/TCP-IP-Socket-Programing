import RPi.GPIO as GPIO
import atexit

# GPIO 핀  번호 설정 
LED_PINS = {"red" : 4,  "blue" : 17}

# gpio 초기화
# GPIO 모드 설정
GPIO.setmode(GPIO.BCM)

# LED 핀 출력으로 설정
for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)

# 종료 시 자동정리
atexit.register(GPIO.cleanup)