from flask import Flask, render_template, request, url_for, session, redirect, jsonify
from login import app # login.py에 있는 app객체를 가져옴
from sensor import read_temp_humid
from sensor import blink_led
from gpio_config import LED_PINS

import time
import threading
import RPi.GPIO as GPIO
import board    # 라즈베리파이 GPIO 핀 제어

#led 초기 깜빡임 초기화
is_pink_blinking = False



@app.route('/dashboard')
def dashboard():
    # 로그인 안 한 경우 → 팝업 띄우고 로그인 페이지로 이동
    if not session.get('logged_in'):
        return '''
            <script>
                alert("로그인이 필요합니다!")
                window.location.href = "/login";
            </script>
        '''
    # ✅ 로그인한 사용자만 여기에 도달함!
    return render_template("dashboard.html")
 
 # =====================       
@app.route('/dashboard/data')
def dashboard_data():
    if not session.get('logged_in'):
        return {"Error" : "허용되지 않은 접근"}, 401
    
    result = read_temp_humid()
    return jsonify(result)
# =====================



#led 스위치 상태 제어 함수
@app.route("/dashboard/led")
def led_switch_handler():
    global is_pink_blinking
    
    #요청 파라미터 가져오기
    state = request.args.get("state") # on 또는 off
    
    if state == "on":
        if not is_pink_blinking:
            is_pink_blinking = True
            threading.Thread(target=blink_led, daemon=True).start()
        return jsonify({"result" : "LED 깜빡임 시작"})
    
    elif state == "off":
        is_pink_blinking = False
        GPIO.output(LED_PINS["red"], GPIO.LOW)
        GPIO.output(LED_PINS["blue"], GPIO.LOW)
        return jsonify({"result" : "LED 깜빡임 중지"})
    
    else:
        return jsonify({"error" : "잘못된 요청입니다"}), 400