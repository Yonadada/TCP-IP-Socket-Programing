from flask import Flask
import RPi.GPIO as GPIO 

app = Flask(__name__)   #Flask 앱 생성
ledPin = 18          # 사용할 GPIO 핀번호 

GPIO.setmode(GPIO.BCM)  # BCM 모드 설정
GPIO.setup(ledPin, GPIO.OUT) # 핀을 출력으로 설정

@app.route('/')
def helloflask():
    return "Hello Flask"

@app.route('/led/on')   # 👉/led/on 접속 시 LED 켜짐
def ledOn():    
    GPIO.output(ledPin, GPIO.HIGH)
    return "<h1> LED ON </h1>"

@app.route('/led/off')  # 👉/led/off 접속 시 LED 꺼짐
def ledOff():
    GPIO.output(ledPin, GPIO.LOW)
    return "<h1> LED OFF </h1>"

# port는 사용자가 원하는데로 
if __name__ == "__main__": 
    app.run(host="0.0.0.0", port="5000")