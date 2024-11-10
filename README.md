# asurada
WagonR to Asurada since 2023-05-20


# 230520 
Setup Venv to Ubuntu 22.04.2 with VMWare / asurada21  
<Setup Git>   
sudo apt install git  
git --version  
(change directory to wnat to make local repository)  
git clone [GITHUB's repository adress]  
git pull  

*git commit -am [commit Tile]  
*git --amend >> commit title change

<Setup python>  
sudo apt-get install python3  
sudo apt-get install python3-pip


# 230826
Raspi - OBD2 connection success.
Getting RPM & SPEED values & Printing values are success. 

# 231214
using Teamviewer - for making remote DEV enviroment.
 >> sign up VNC and connection test. >> need to pay for using fee >> using teamviewer & smartphone's hotspot >>success.


# 0702
- index.html 작성 및 자동 켜짐
>> 
    vim ~/.config/lxsession/LXDE-pi/autostart

# 0703
- WEBsocket을 활용해서 python 파일 데이터를 html로 전송.
>>  
    pip install websockets

- systemd 활용해서 부팅 시에 블루투스 연결 및 파이썬 실행
>>  
    sudo vim /etc/systemd/system/myobd.service
    sudo systemctl daemon-reload
    sudo systemctl enable myobd.service
    sudo systemctl start myobd.service

- .sh파일을 생성한 뒤, sh파일을 service에서 자동실행하게하여 python자동실행
>>
    start.sh 파일 생성 및 파이썬 실행 명령 추가
    sudo chmod +x /home/asurada/Desktop/asurada/start.sh 권한 수정
    myobd.service에 sh파일 실행 명령어 추가
    sudo journalctl -u myobd.service --since "2024-07-05 00:00:00" >> 로그 보기


>> 웹소켓이 부팅시에는 실행이 되지 않아서, rc.local로 시도
sudo vim /etc/rc.local
sudo chmod +x /etc/rc.local // 실행권한이 부여되어있어야함

>> 시스템 전체 범위로 웹소켓 다시 설치
sudo pip3 install websockets
# Python 스크립트 실행
# /home/asurada/Desktop/aa.sh &
# /usr/bin/python3 /home/asurada/Desktop/asurada/websocket_server.py &
 /usr/bin/python3 /home/asurada/Desktop/asurada/test_0826.py &


 # 241102 restart development.
 using electron - setup devEnviroment. >> 일단 보류
 Node.js 설치

# 241104 >> 자동실행 후 RPM 표시까지 성공.
rc.local >> python test_0826.py 를 start.sh 로 진행하도록 변경
** sh 파일 실행을 위해서는 sh <<파일절대디렉토리>> 로 작성 필요
start.sh >> 오류 처리 코드가 없고, 아직 rfcomm 다루는 법에 대해 모르는게 많아서 최소 코드로 변경
index.html >> css 95vh로 변경하여 스크롤 나오는 현상 없앰.

# 241111 >> 현재 기어 표시를 SPEED/RPM 비율로 단순하게 변경
실제 측정한 속도/회전수 비율을 적용하여 계산하도록 변경














 ** bluetooth 관련 명령어
 1. Bluetooth 서비스 상태 확인
sudo systemctl status bluetooth

2. Bluetooth 장치 상태 확인
sudo hciconfig hci0 up
hciconfig hci0

3. Bluetooth 페어링 상태 확인
sudo bluetoothctl 
>>  power on
    agent on
    default-agent
    scan on
    pair <OBD_MAC_ADDRESS>
    trust <OBD_MAC_ADDRESS>
    connect <OBD_MAC_ADDRESS>

4. RFCOMM 장치 바인딩 확인
sudo rfcomm bind 0 <OBD_MAC_ADDRESS>
ls /dev | grep rfcomm  # rfcomm0 가 있는지 확인

5. 블루투스 설정 파일 확인
sudo vim /etc/bluetooth/main.conf
설정 파일에서 AutoEnable=true가 설정되어 있는지 확인합니다.

6. 블루투스 모듈 재로드
sudo modprobe -r btusb
sudo modprobe btusb

7. 시스템 로그 확인
sudo journalctl -u bluetooth


** 웹소켓 에러 대처
sudo lsof -i :8765  #8765번 포트 사용중 확인
sudo kill -9 1234  #PID 1234 kill


 
