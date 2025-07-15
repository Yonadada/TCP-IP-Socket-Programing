import RPi.GPIO as GPIO # RPi.GPIO → 라즈베리파이 핀을 제어할 수 있는 라이브러리
import time    # time → 릴레이 ON/OFF 간 시간 간격을 주기 위해 사용

relayPin = 26  # → GPIO 26번 핀에 릴레이 연결했다는 의미

GPIO.setmode(GPIO.BCM)  # → 핀 번호를 BCM 번호로 쓰겠다는 뜻
GPIO.setup(relayPin, GPIO.OUT)   # → 릴레이 핀을 출력 모드로 설정

try:
   while True:
      GPIO.output(relayPin, True) # = HIGH      #→ 릴레이 ON (스위치 닫힘 → 전류 흐름 → LED 켜짐)
      print("True")
      time.sleep(1)

      GPIO.output(relayPin, False) # → 릴레이 OFF (스위치 열림 → 전류 차단 → LED 꺼짐)
      print("False")
      time.sleep(1)     # → 1초 동안 대기

except KeyboardInterrupt:  # → Ctrl+C로 프로그램 종료할 때 예외 처리
   print("bye!")  
finally:
   GPIO.cleanup()    # → 핀 설정 초기화해서 다른 프로그램 사용 시 충돌 방지
