# TCP-IP-Socket-Programing
iot 개발자 tcp/ip 프로그래밍 repository

## 1일차
1. VMware 설치
    - [Link](https://www.vmware.com/products/desktop-hypervisor/workstation-and-fusion)
2. Ubuntu 설치
    - [Link](https://releases.ubuntu.com/jammy/)
3. puTTy 설치
    - [Link](https://www.putty.org/)

#### ✅ 리눅스 개발환경 준비 및 설정
1. 터미널 열기 
    - Ctrl + Alt + T 
    ➡️ 우분투에서 터미널을 여는 단축키
<br>
2. 네트워크 관련 도구 설치
    ```bash
    sudo apt install net-tools
    ```
    ➡️ 네트워크 인터페이스(IP 주소 등) 정보 확인 
<br>
3. 패키지 목록 업데이트 및 업그레이트
    ```bash
    sudo apt update
    sudo apt upgrade
    ```
    ➡️ 시스템에 설치 가능한 패키지 목록을 최신으로 갱신
    ➡️ 설치된 패키지들을 최신 버전으로 업그레이트 
<br>
4. nano  편집기 설정 
    ```bash
        sudo nano/etc/nanorc
    ```
    ➡️ nano 편집기의 기본 설정 파일을 편집 
    ➡️예시 
    ``` bash
    set autoindent      # 자동 들여쓰기
    set linenumbers     # 줄 번호 표시
    set tabsize3        # 탭 크기를 3으로 설정
    ```

5. GCC  컴파일러 설치 
➡️ C언어 프로그램을 컴파일할 수 있는 GCC 컴파일러 설치 
- 설치
``` bash
    sudo apt install gcc 
```    
- 컴파일하기 
➡️ 실행 파일 이름이 기본으로 a.out이 생김
``` bash
    gcc main.c
```
- 실행파일 이름 바꾸고 싶다면 
``` bash
    gcc main.c -o mainProgram
```
<br>

#### 💻 리눅스 기본 명령어 
| 명령어        | 설명                           |
| ---------- | ---------------------------- |
| `uname -a` | 컴퓨터가 어떤 시스템인지 보여줌 (이름, 버전 등) |
| `cd`       | 폴더 안으로 들어가기                  |
| `ls`       | 폴더 안에 뭐가 있는지 보여줌             |
| `pwd`      | 내가 지금 어디 폴더에 있는지 알려줌         |
| `cd ..`    | 한 단계 위 폴더로 올라가기              |
| `mkdir`    | 새 폴더 만들기                     |
| `touch`    | 빈 파일 하나 만들기                  |
| `cat`      | 파일 내용을 화면에 보여줌               |
| `cp`       | 파일이나 폴더 복사하기                 |
| `clear`    | 터미널 화면 깨끗이 지우기               |
| `rm -rf`   | 파일이나 폴더 지우기 (조심해서 써야 함!)     |
| `chmod`    | 파일이나 폴더의 권한 바꾸기              |

### 🌐 네트워크 프로그래밍 기초
#### 🤝 클라이언트-서버 모델이란?
- 클라이언트 → "나 이거 하고 싶어요" 하고 요청 하는 쪽
- 서버 → "오케이~ 내가 해줄게" 하고 응답하고 처리해주는 쪽
<br>

#### 🪢 소켓(Socket)이란?
> "컴퓨터끼리 대화하게 해주는 가상의 통로"
- 소켓은 두 컴퓨터가 데이터를 주고 받을 수 있게 해주는 **가상의 연결 지점**
- 전화기처럼 연결선을 만들어놓고 데이터를 주고 받음!

 → 정리
> 소켓(socket)은 두 컴퓨터가 이야기 할 수 있는 가상 통로

<br>

#### 🌟서버 소켓 만드는 순서
서버

## 4일차
### 💡내가 하고 싶은 기능 
✅여러명이 동시에 서버에 접속할 수 있음
✅누가 접속했는지 서버가 알고 있음
✅글(메시지)을 보내면, 
    --> 서버가 받아서
    --> **다른 사람한테도 보내줌**
✅연결을 끊으면 서버가 "누가 연결이 끊겼나" 알 수 있음 

- 멀티 클라이언트 채팅 서버라고 부름

#### 방법
1. 서버가 소켓을 만든다
2. 서버가 "문 열고 기다림"

UDP 기반 멀티캐스트&브로드캐스트
- 네트워크에서 한 송신자가 데이터를 한 번에 여러 장치에게 전송할 때 사용되는 방식

1. 멀티캐스트
- 멀티캐스트 서버는 특정 멀티캐스트 그룹을 대상으로 데이터를 **딱 한번 전송**
- 주소는 224.0.0.0 ~ 239.255.255.255 범위에서 설정
- TTL(Time to live)필드를 가지고, 라우터 지날 때마다 TTL -1감소, 0이되면 더 이상 출력X

2. 브로드캐스트
- 동일한 네트워크 내(서브넷)에 존재하는 호스트에게 데이터를 전송, **데이터 전송의 대상이 호스트가 아닌 네트워크**
- 

### Thread
- 리눅스에서 쓰레드를

## 과제 
웹 서버 코드를 작성

웹서버 동작 순서
1. 소켓 생성(전화기 만들기)
2. bind(전화번호 등록)
3. listen(전화벨 기다리기)
4. accept(전화 받기)
5. 클라이언트 메시지 읽기
6. HTTP 응답 보내기 
7. 종료

### 라즈베리 putty 설정 방법
1. Putty에 접속 
    - host name -> raspberrypi 이름 입력 후 저장 -> open 
2. 명령어 입력
    - sudo apt update && sudo apt upgrade -y
    - sudo reboot now 
    - restart sessions
    - vncserver-virtual 
3. sudo raspi-config 명령어 입력 
    - interface options > VNC > Yes
4. vnc viewer 검색창에 raspbearrypi 입력 
    - username: raspi, pwd:raspi
5. vnc viewer 에서 Settings > Lan(KOR), UTF-8 
6. putty에서 한글(나눔글꼴) 설치 명령어 
    - sudo apt install fonts-nanum fonts-nanum-extra
7. 폰트등록 
    - sudo apt install fonts-unfonts-core
8. 재부팅
    - sudo reboot now
9. 명령어 입력 
    - sudo apt install ibus -y
    - sudo apt install ibus-hangul
    - sudo apt install fcitx-hangul
10. 설정 
    - 기본설정 > 입력기 > Yes > iBUS 선택 > 확인
    
    sudo nano /etc/nanorc > 편집기 열어서 주석 해제
    sudo etc/nanorc
    ls 
    ls -al a.txt
    cp a.txt b.txt
    ls
    cp ./a.txt ./c.txt
    mv c.txt d.txt
    ls
    ls *.txt
    ls ?.txt
    rm -fr *.txt
    ls
    echo $PWD > 환경변수 
    rmdir (삭제할 파일이름) > 삭제\
    

    ## 🐍 Pi.GPIO 모듈 쉽게 배우기
    - 라즈베리파이는 컴퓨터처럼 생긴 작은 기계이고 특별한 점은 **핀(Pin)** 이라는 구멍들이 있어서 전자부품을 연결할 수 있다!
    
    #### 예시
    - 파이썬으로 제어하려면 Pi.GPIO라는 모듈을 사용
        - LED 켜고 끄기
        - 버튼 눌렀는지 확인하기
        - 모터 돌리기

가상서버 명령어 

source activate
python 
    Pi.GPIO 모듈
        - GPIO.setmode(GPIO.BOARD) -> wPi
        - GPIO.setmode(GPIO.BCM) -> BCM
        - GPIO.setmode(channel, GPIO.BOARD) -> 사용할 핀의 모드 설정(IN/OUT)
        - GPIO.cleanup() -> 모든 핀 초기화
        - GPIO.setmode(channel, state) -> HIGH(1) / LOW(0)
        - GPIO.setmode(channel) 

        풀업 저항 풀다운 저항


        과제 
        버튼 1번 누르면 꺼지고 
             2번 빨간색
             3번 녹색
             4번 블루 
env > source active > 

home 에서 sudo apt update> sudo apt install mariadb-server > sudo systemctl start mysql


ModuleNotFoundError: No module named 'adafruit_dht'
-->에러시 

pip install adafruit-circuitpython-dht
sudo apt install libgpiod2



sudo apt install python3-pyqt5
sudo apt install qttools5-dev-tools


✅ 기본 상태

모든 LED가 OFF (0)

✅ 동작

각 버튼(slot1, slot2, slot3)을 누를 때마다 그 색이 ON (LED HIGH)

또 한 번 누르면 OFF (LED LOW)

다른 버튼 눌렀을 때는 해당 색만 ON, 나머지는 OFF

지금 올려준 코드는 여러 문제가 있어. 예를 들어:

while True가 클래스 안에 들어있어. → PyQt에서는 메인루프가 따로 있으므로 while True 쓰면 프로그램이 멈춤.

if (redBtn == 1) 같은 코드가 있는데 redBtn이라는 변수가 정의되어 있지 않아.

버튼 클릭은 PyQt의 시그널/슬롯으로 연결해야 해.

elif 뒤에 조건이 없거나 구문 오류가 있어.


아래는 수정된 PyQt5 코드 예시야. 네가 원하는 “누를 때마다 ON/OFF” 기능

<hr>

## 6일차
# ✅ Raspberry Pi Relay Practice with LED
> [▶️ 시연 영상 보기](https://github.com/user-attachments/assets/72c32a6b-cf24-4ce3-9890-5e6d901c46c3)


라즈베리파이를 이용해 릴레이로 LED를 제어한 프로젝트 기록

## 1.🔌Relay란?
- **릴레이 = 전기로 여닫는 스위치**
- 약한 전기(라즈베리파이 신호)로 → 센 전기(LED, 모터 등)을 켜거나 끔

### 릴레이랑 승압기랑 뭐가 다른가? 🤔
- 릴레이는 약한 전기로 문을 여닫는 **스위치** 일 뿐
- 전기를 세게 만들거나(전압, 전류를 올리거나)이 전류들이 왔다갔다 할 수 있게 넓히는 역할은 아니다

#### 쉽게 비유하자면...
- 릴레이 = **자동문**
    - 평소에는 닫혀 있다가, 약한 전기 신호가 오면 문을 열고
    - 센 전기가 지나갈 수 있는 **길**을 열어주는 것

- 승압기 = **물 펌프**
     -전기의 양이나 세기를 **직접 세게** 만들어 주는 장치

## 2. 릴레이 단자 설명
| 단자 | 설명 |
|------|--------------------------------|
| **COM (Common)** | 전기가 지나는 공통 길목 |
| **NC (Normally Closed)** | 평소 닫혀있어 전기가 흐름 |
| **NO (Normally Open)** | 평소 열려있어 전기가 안 흐름 |

## 3. ⚙️ NO, NC는 왜 선택해야 할까?
- 릴레이를 사용할 때 **NC, NO 중 어디를 연결**할 지는 장치를 평소에 **켜둘지, 꺼둘지** 에 따라 달라진다

| 원하는 동작 | 어떤 단자 사용? |
|-----------------------------|-------------|
| 평소엔 꺼져 있고, 신호 주면 켜지길 원할 때 | **NO 사용** |
| 평소엔 켜져 있고, 신호 주면 꺼지길 원할 때 | **NC 사용** |


## 4. ⭐ LED 연결 (내가 한 방식)
- 라즈베리파이 5V → LED (+)
- LED (-) → 릴레이 **NC**
- 릴레이 **COM** → 라즈베리파이 GND
> **왜 이렇게 연결 했나**
> 전기는 + 에서 - 로 흘러야 불이 켜지고, COM을 CND에 연결해야 전기가 집으로 돌아갈 수 있음

## 5. 🔥 타는 냄새 발생!!

### 문제 
- 릴레이 작동 시 LED를 켰는데 *브레인보드와 점퍼선에서 타는 냄새 진동*
- 피복이 살짝 녹음😬

### 원인
- 필요없는 점퍼선 빼지 않아서 전류가 잘못 흘러 **과전류** 발생!

### 해결법 
- 회로 구성 후 불필요한 선 제거
- 전기 냄새나면 즉시 전원 차단 

## 6. 한 줄 정리 ✨
> 릴레이는 전기의 문 역할
> 라즈베리파이가 문을 열면
> 전기가 지나가서 LED가 켜진다

## 7. 회로 연결도 
#### NO 연결도


## 8. GPIO 핀 배치도
[Raspberry Pi GPIO Pinout] 
<img src="/img/GPIO_Pinout.png" width="200">

## 9. 릴레이 제어 코드 💻
[전체 코드 보기 click](./source/day6/relay_Test.py)
> **핵심 요약**
> `GPIO.BCM` = 핀 번호 체계
> `GPIO.setup` = 출력핀 선언
> `GPIO.output` = 릴레이 ON/OFF 제어
> `GPIO.cleanup` = 마무리 정리

네ㅐ가 원하는 색깔 5
LED - 를 릴레이에 NO, 릴레이 COM을 라즈베리 GND

<hr>

# 🎯 Raspberry Pi - 스위치로 LED 제어 연습
- 스위치를 눌렀다가 뗐을때 led가 켜졌다 꺼지도록 제어
- 특수 핀으로 인한 led가 꺼지지 않는 문제를 경험
> [▶️ 시연 영상 보기](https://github.com/user-attachments/assets/50af7a88-2161-4397-b5c4-94b703d21be6
)




🛠️ 사용한 하드웨어
- Raspberry Pi
- RGB LED 모듈
- 점퍼선
- 브레드보드

## ✅ 1. GPIO 기본 개념

#### ✔️ GPIO란?

- **G**eneral **P**urpose **I**nput **O**utput (범용 입출력 핀)  
- HIGH (3.3V) / LOW (0V) 신호 출력 가능

#### ✔️ Pull-up / Pull-down ⚡

- **Pull-up** 🔼
  - 기본 HIGH 상태 유지
  - 신호가 GND로 떨어질 때만 LOW로 변함
- **Pull-down** 🔽
  - 기본 LOW 상태 유지
  - 신호가 HIGH로 올라갈 때만 HIGH로 변함

> 💡 **Tip:** 풀업/풀다운 저항은 스위치 떨림 방지 (채터링 방지)에 필수!

## ✅ GPIO 이벤트 감지와 콜백 함수

### 🤔 Polling vs Event

| 구분      | Polling 방식             | Event 방식                   |
|-----------|--------------------------|-----------------------------|
| 동작 방식 | 상태를 반복적으로 읽음   | 이벤트 발생 시 콜백 호출    |
| CPU 점유율| 높음                     | 낮음                        |
| 코드 구조 | 복잡해질 수 있음         | 간단하고 효율적             |




#### 🚨 GPIO의 특별한 핀들 (주의할 핀)

다음 핀들은 **특수 기능**이 있어, GPIO로 쓸 때 예상치 못한 동작이 일어날 수 있다

| ⚙️ GPIO | Pin No | 기본 기능         | 주의사항                        |
|---------|--------|-------------------|---------------------------------|
| GPIO2   | 3      | I2C1 SDA          | 기본 Pull-up HIGH               |
| GPIO3   | 5      | I2C1 SCL          | 기본 Pull-up HIGH               |
| GPIO14  | 8      | UART TXD          | 부팅 시 메시지 출력될 수 있음    |
| GPIO15  | 10     | UART RXD          | 외부 신호 영향 가능             |
| GPIO0   | 27     | ID_SD (EEPROM)    | HAT EEPROM 통신용               |
| GPIO1   | 28     | ID_SC (EEPROM)    | HAT EEPROM 통신용               |

> ✅ **Tip:** 안전하게 GPIO4, GPIO17, GPIO27, GPIO22 등을 사용하면 문제 발생 확률이 낮음


### 🔔 콜백 함수란?

- GPIO 핀에서 신호 변화가 생기면 **자동 호출**되는 함수
- 예) 스위치 누르면 LED 켜기

```python
def printcallback(channel):
    print("pushed")
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(ledPin, GPIO.LOW)
```
- channel 
    - 이벤트가 발생한 핀 번호가 자동으로 인자값으로 전달됨
- LED를 0.5초간 켰다 끄는 기능 수행

#### ✅ add_event_detect()
```python
GPIO.add_event_detect(swPin, GPIO.RISING, callback=printcallback, bouncetime=100)
```
## 2. 콜백제어 코드 💻
[전체 코드 보기 click](./source/day6/interrupt.py)
> **핵심 요약**
> **wPin** → 감지할 GPIO 핀 번호
> **GPIO.RISING** → LOW → HIGH로 변할 때 이벤트 발생
> **callback** → 이벤트 발생 시 호출할 함수
> **bouncetime** → 채터링 방지 시간 (ms)
>📝 Tip: bouncetime을 설정하지 않으면 스위치를 한 번 눌러도 여러 번 감지될 수 있습니다.


### 3. ✅ 오늘 겪은 문제와 해결 과정
### ⚠️ 문제 상황

 GPIO3 (핀 5)에 LED 연결했더니
 1. 아무 코드 안 돌려도 불이 들어옴 💡

 2. 프로그램 종료 후에도 LED가 꺼지지 않음 ❌
 
 3. 코드 오타 → AttributeError 발생 🔎

 4. RGB 모듈 핀 배치가 PCB와 다름:
    R 단자에 연결했는데 파란 불이 들어옴 🔵

### 💥 원인

1. GPIO3는 I2C SDA 핀 → 기본 Pull-up HIGH
    cleanup 후에도 HIGH로 돌아감
2. 오타는 `setup`이 정답
3. RGB 모듈은 제조사마다 핀 배치가 다를 수 있음

### ✅ 해결 과정

1. GPIO15로 핀 변경 → 정상 작동 확인 👍
2. 프로그램 종료 시 LED를 LOW로 출력 후 INPUT 모드로 변경 🔌
3. 코드 오타 수정
4. RGB 모듈 각 단자에 전류 흘려 색상 직접 확인 🎨

### 4. 추천 안전 GPIO 리스트 🛡️
| 🛡️ GPIO | 🔢 Pin No |
|---------|-----------|
| GPIO4   | 7         |
| GPIO17  | 11        |
| GPIO27  | 13        |
| GPIO22  | 15        |
| GPIO5   | 29        |
| GPIO6   | 31        |
| GPIO13  | 33        |
| GPIO19  | 35        |
| GPIO26  | 37        |
> ✅ Tip: GPIO3, GPIO2, UART 핀은 피해서 쓰는 것이 안전

<hr>

# 7일차
## 📚 핵심 개념 설명(flask, 라우팅, GET/POST)

### 🐍 Flask란?
> Flask는 파이썬으로 만든 '간단한 웹사이트'를 만들 수 있게 도와주는 도구(프레임워크)

- 웹 서버를 만들 때 꼭 필요한 기능(라우팅, 요청 처리, HTML 템플릿 연결 등)만 기본으로 포함되어 있음
- 복잡한 기능(회원가입, DB연결, 관리자 페이지 등)은 직접 추가해서 사용해야 함
- 처음 시작할 때 필요한 파일과 코드가 적어서 배우기 쉽고 가볍게 실행 가능
- 이런 이유로 Flask는 **'경량 구조(Micro Framework)'** 라고 불림

### 🔀 Routing (라우팅)
> 사용자가 어떤 주소(URL)로 접속했는지 보고, 그에 맞는 동작을 실행하도록 연결해주는 기능

> **핵심 포인트** 📍 주소와 기능을 이어주는 **'길 안내표'** 같은 역할을 함

- Flask에서는 **'@app.route()'** 를 사용해 특정 주소와 함수를 연결함
- 예시)
```python
@app.route('/') # index.html 보여줌 
def home():
    return render_template("index.html")
```
```python
 <form action='/data' method='post'> # 'data' 는 LED 제어 기능 실행
```

<pr>

### ※ Template Rendering (템플릿 렌더링)🧩
> HTML 파일(웹페이지 틀)에 값을 채워서 사용자에게 보여주는 기능

- Flask에서는 **'render_template("파일명.html")'** 을 사용
- 웹페이지 내용이 고정돼 있지 않고, 상황에 따라 바뀌도록 구성 가능
- 예시) 사용자 이름, 센서 값, 버튼 결과 등을 HTML에 출력
- 🧾 템플릿은 **빈 서식**, Flask는 **내용을 채워주는 역할**을 함.
<pr>

### 🌐 HTTP 요청 방식 (GET / POST)
> 웹 페이지가 서버에 정보를 요청하거나 전달할 때 사용하는 방식

- 대표적으로 GET과 POST 방식이 있음
<pr>

#### 📥 GET
> 서버에게 **"정보를 보여줘"** 라고 요청할 때 사용
- 요청(Request) 내용이 주소창(URL)에 그대로 보임
- 보안이 약하므로 검색, 조회 같은 단순 요청에 적합

#### 📤 POST
> 서버에서 **"정보를 보낼게"** 라고 요청할 때 사용
- 요청 내용이 주소창에 보이지 않아서 보안에 상대적으로 안전함 
- 회원가입, 로그인, 버튼 클릭 등 **사용자 입력을 처리할 때** 사용됨

#### 💬 추가 질문: GET 방식은 HTTPS를 쓰면 안전한가??
> HTTPs 를 사용하면 GET 요청 내용이 암호화 되서 **전송 중, 외부에서 엿보는 것(도청)은 방지** 가능

- 하지만! 요청 데이터를 **URL 에 포함해서 보내기** 때문에 누가 어떤요청과 어떤 정보를 보냈는지 흔적이 남음 
    - 브라우저 히스토리
    - 서버 로그
    - 즐겨찾기(북마크)

#### 🍪 쉬운 비유로 정리
| 방식 | 설명 | 특징 |
|------|------|------|
| **HTTP + GET** | 짝꿍에게 **복도 한복판에서 과자 이름을 외치며 던져줌** | → 다 들킴. 내용도, 주고받은 사실도 모두 노출됨 |
| **HTTPS + GET** | 복도에서 **속닥속닥 과자를 주지만 CCTV는 돌아가는 상태** | → 중간에서 훔쳐보긴 어렵지만, **기록은 남음** |
| **POST + HTTPS** | **가방에 몰래 과자를 넣고 복도 구석에서 전달** | → 내용도 숨김, **기록도 거의 안 남음** |

### ✅ 정리

| 요청 방식 | URL에 데이터 노출 | 전송 내용 암호화 | 기록에 남는가 | 적합한 용도 |
|------------|-------------------|------------------|----------------|--------------|
| GET (HTTP) | 있음 | 없음 | O | 단순 조회 외 비추 |
| GET (HTTPS) | 있음 | O | O | 검색, 페이지 이동 |
| POST (HTTPS) | 없음 | O | X | 로그인, 민감 정보 입력 등 |

> 📌 그렇기 때문에, 민감한 정보를 주고받을 때는 항상 `POST + HTTPS` 조합 사용을 권장함.

<pr>

### 💬 추가 질문: POST 방식이면 항상 안전한가요?
POST는 **요청 데이터를 URL이 아니라 HTTP 본문(Body)에 담아 전송**하기 때문에,  
GET보다 보안성이 높다고 알려져 있음.  
하지만 다음과 같은 경우에는 여전히 **데이터가 노출될 수 있음**:


### ⚠️ POST 방식에서도 데이터가 노출될 수 있는 상황

| 상황 | 설명 |
|------|------|
| ❌ HTTPS 없이 POST 사용 | 전송 내용이 **암호화되지 않음** → 중간에 데이터 탈취 가능 (예: 패킷 스니핑) |
| ❌ 서버 로그 기록 | 일부 서버 설정에서는 POST 요청의 **본문 내용을 로그에 남길 수 있음** |
| ❌ 악성 코드 또는 브라우저 확장 | 클라이언트 측(브라우저)에서 악성 코드가 동작 중이면 **전송 전 데이터 탈취 가능** |
| ❌ CORS 또는 오픈된 API | 외부 도메인에 POST 요청이 허용되면 **CSRF(Cross Site Request Forgery)** 공격 위험 존재 |


### ✅ 안전하게 POST 요청을 처리하는 방법

1. **HTTPS 필수 사용**  
   - 전송 내용 전체를 암호화함  
   - `http://`이 아닌 `https://` 주소 사용

2. **서버 로그 정책 설정**  
   - 민감한 데이터가 로그로 남지 않도록 서버 설정을 점검

3. **XSS / CSRF 보안 강화**  
   - 웹 폼에 CSRF 토큰 포함  
   - 입력 필드에 스크립트 삽입 방지

4. **입력값 검증 및 인코딩 처리**  
   - 클라이언트-서버 모두에서 입력값 유효성 검증


> 🔐 정리:  
> POST는 URL에 노출되지 않기 때문에 기본적으로는 안전하지만,  
> **HTTPS를 쓰지 않거나**, **서버와 브라우저 환경이 안전하지 않으면** 데이터가 유출될 수 있음.  
> **"POST + HTTPS + 보안 설정 강화" 조합이 필수적**임.

<hr>

## 1. Flask 웹 서버 실습 #1 - 간단한 라우팅
##### [결과]
    <img src="/img/app1.png" width="350">
- [코드](/source/day7/appTest.py.py)
> **핵심 포인트**
> - Flask는 @app.route() 통해 URL 라우팅을 설정한다
> - host:"0.0.0.0" 설정을 통해 다른 디바이스에서도 웹 서버 접근이 가능하다
> - HTML이 아닌 문자열만 리턴해도 웹 페이지로 동작한다

## 2. Flask 웹 서버 실습 #2 - 요청 파라미터 GET 방식 처리
- [결과]
<img src="/img/appTest2.png" width="350">

- [코드](/source/day7/appTest2.py)
>**핵심 포인트**
> *request.args.get('key', 'default')* 를 통해서 값을 쉽게 받을 수 있다
> 파라미터가 없을 경우 기본값을 지정할 수 있어서 예외처리가 용이
> ?key=value 형태로 브라우저 주소창에서 테스트 가능 

## 3. 📘 웹 서버 실습 #3 
- Python의 **Flask** 프레임워크를 사용한 간단한 예제
- 브라우저에 접속하면 "hello World" 출력

##### [결과]
- 🏠 루트 URL /
<img src="./img/app1.png" width="350">

- 이름 URL /name
<img src="/img/app1_age.png" width="350">

- 🎂 나이 URL /age
<img src="/img/app1_name.png" width="350">

- [코드](/source/day7/app1.py)

>**핵심 포인트**
> @app.route('/경로')를 통해 요청 URL에 따른 페이지 응답을 설정 할 수 있음
> h1 태그를 사용하여 HTML 형태로 텍스트 출력 가능
> debug=True 로 설정하면 코드 수정 시 서버 재시작 없이 바로 반영 가능

## 4. Flask + GPIO 웹 제어 - 웹에서 라즈베리파이 GPIO LED 제어
- Flask 웹 서버와 Raspberry Pi의 GPIO를 연동해서 웹 페이지에서 LED를 켜고 끄는 실습

### 구현 방식
##### - ✅ 방식 1: 고정 라우터(/led/on, /led/off)
- ``/led/on`` 또는 ``/led/off`` 주소에 접속하면 LED가 제어된다
##### - ✅ 방식 2: 동적 라우터(/led/<state>)
- 하나의 라우트로 on, off 둘 다 처리
- 방식 2 코드가 더 유연하고 확장성이 있다 

##### - ✅ 추가 기능: /led/clean
- GPIO 핀 설정을 모두 초기화하여 자원 해제
- 프로그램 종료 후 GPIO 상태를 깨끗하게 마무리할 때 사용 

##### 🧹 /led/clean 라우트를 실행해야 하는 이유
- 라즈베리파이에서 GPIO 핀은 설정 후에도 시스템에 남아있음
- 프로그램이 종료되도 계속 사용 중 상태로 유지됨
- ``/led/clean`` 라우트 통해 ``GPIO.cleanup()`` 을 실행하면 모든 핀 초기화
- **다음 실행 시 충돌, 오작동 방지**  

### ⚠️ 문제 발생 및 해결
- 문제: GPIO 18번으로 설정했을 때 LED가 켜지지 않음

- 원인: GPIO 18번은 기본적으로 PWM/오디오 기능이 할당된 핀으로, 단순 출력이 제한될 수 있음

- 해결: GPIO 15번으로 변경 후 정상 작동

> **TIPS** 단순 제어용 장치에는 일반 GPIO 핀(14, 15, 23 등)을 사용하는 것이 안정적임

### 📸 실행 화면
- [실행영상](https://github.com/user-attachments/assets/1df40ed8-f72d-45be-a964-4a077d59d49a)

<hr>

### 개인 실험 
####  하고자 하는 기능 정리
> ☑️ **/led/on 호출 시:**
부저에서 학교 종소리 음계 1번만 연주
LED 0 → 1 → 2번을 1.5초씩 켜고 차례로 넘어감
LED 순환을 무한히 반복 (while 루프)

> ☑️ **/led/off 호출 시:**
무한 LED 루프 종료
ledPins[2]만 1.5초 켰다가 꺼짐
끝

<hr>

## 8일차
## 🧪 Flask + GPIO POST 방식 제어 – 웹 버튼으로 LED 제어 실습
- HTML 폼의 버튼을 통해서 **POST 요청** 을 보냄
- Flask  서버에서 요청을 받아 Rasberry Pi의 GPIO 핀을 제어하는 웹 애플리케이션을 구현

### ⚙️ 시스템 구성도
```css
 HTML 버튼 클릭 ]
        ↓ POST
[ Flask 서버 (/data) ]
        ↓
[ RPi.GPIO ] → [ LED ON/OFF ]
```
 
### 🧾 구현 방식 요약
- 사용자가 웹에서 'on'/'off' 버튼 클릭시
- Flask가 **request.form**을 통해 값을 받고
- Raspberry Pi의 GPIO 핀에 HIGH/LOW 신호를 줌
- [파이썬 코드](/source/day8/ledapp.py)
- [html코드](/source/day8/templates/index.html)

### 🛠️ Troubleshooting – GPIO 15번 사용 시 LED가 작동하지 않는 문제
##### 🔍 문제 현상
- LED를 GPIO 15번 핀에 연결하고 웹에서 제어 시,
- "on" 버튼을 눌러도 LED가 켜지지 않음
- GPIO 18번으로 변경 시 정상 작동

##### 🎯 원인 분석
> GPIO 15번은 단순 출력용이 아니라, 특별한 용도로 예약된 핀이다.
- Raspberry Pi에서는 GPIO 15번이 기본적으로 *UART 통신의 RXD(수신) 핀으로 설정*되어 있음

    - **UART란**?
    👉 컴퓨터나 마이크로컨트롤러끼리 직렬로 통신할 수 있게 해주는 방식
        (예: 라즈베리파이와 아두이노, GPS 모듈, 블루투스 모듈 등)

    - **RXD (Receive Data)**:
    👉 외부 기기에서 데이터를 받아오는 용도

- 부팅 시 시스템 내부에서 **"외부 기기와 통신하기 위한 귀"**처럼 이미 사용 중이라, 
 단순한 LED 제어 신호를 보내도 반응이 없음

- 사용자가 전기 신호를 주려고 해도, 이미 다른 기능이 "선점"하고 있어서 무시됨

##### ✅ 해결 방법
- 단순 출력 목적이라면 GPIO 15번을 피하고, 일반 GPIO 핀을 사용하는 것이 가장 안전함
- 추천 핀: GPIO 17, 22, 23, 24 등 👉 특별한 기본 기능이 없음

##### 📦 그럼 언제 쓰냐?
| 사용 예시         | 설명                           |
| ------------- | ---------------------------- |
| 🛰️ GPS 모듈 연결 | GPS가 보내주는 데이터를 GPIO 15번으로 받음 |
| 📡 블루투스 통신    | HC-06 같은 블루투스 모듈에서 데이터 수신    |
| 🧠 MCU 연동     | 아두이노와 라즈베리파이 간 통신            |
| 🖥️ 시리얼 디버깅   | 콘솔 로그를 UART로 출력 받아 확인할 때     |

#### 🎥 실행화면
[동영상]()