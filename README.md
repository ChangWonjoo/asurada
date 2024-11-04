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
 using electron - setup devEnviroment.
 Node.js 설치
 
