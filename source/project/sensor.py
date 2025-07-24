from flask import Flask, render_template, request, url_for, session, redirect, jsonify
from login import app # login.py에 있는 app객체를 가져옴
from datetime import datetime
from gpio_config import LED_PINS

import time
import RPi.GPIO as GPIO
import board    # 라즈베리파이 GPIO 핀 제어
import adafruit_dht     # DHT 센서 라이브러리

# 센서객체 생성
dht11 = adafruit_dht.DHT11(board.D18)

#led 깜빡임 초기화
is_pink_blinking = False

# 온&습도 모듈
# 센서 읽기 함수
def read_temp_humid():
    try:
        temperature = dht11.temperature
        humidity = dht11.humidity
        
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 현재시각 문자열
        if temperature is None or humidity is None:
            return {
                    "temperature" : "Error",
                    "humidity" : "Error",
                    "timestamp" : now}
        else:
            return {    
                    "temperature" : temperature, 
                    "humidity" : humidity,
                    "timestamp" : now
                    }

    except Exception as e:
        print("온,습도 데이터 읽기 오류: ", e)
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {
            "temperature" : "Error",
            "humidity" : "Error",
            "timestamp" : now
            }



#led 깜빡임 함수
def blink_led():
   
    # R, B가 ON일때
    GPIO.output(LED_PINS["red"], GPIO.HIGH)
    GPIO.output(LED_PINS["blue"], GPIO.HIGH)
    time.sleep(1)
       
   
       
  
