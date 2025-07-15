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
> [▶️ 시연 영상 보기]<img src="/img">
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