#!/bin/bash

# LOGFILE="/home/asurada/Desktop/asurada/start_log.txt"
LOGFILE="/home/asurada/Desktop/asurada/startup.log"

echo "Starting OBD service..." >> $LOGFILE
date >> $LOGFILE

sudo hciconfig hci0 up >> $LOGFILE 2>&1
# 기존 바인딩 해제
sudo rfcomm release 0 >> $LOGFILE 2>&1  
# 관련 프로세스 종료
# sudo lsof /dev/rfcomm0 | awk 'NR>1 {print $2}' | xargs sudo kill -9 >> $LOGFILE 2>&1
# 모듈 강제 제거 및 재로드
# sudo rmmod -f rfcomm >> $LOGFILE 2>&1
# sudo modprobe rfcomm >> $LOGFILE 2>&1
# RFCOMM 장치 바인딩
sudo rfcomm bind 0 00:1D:A5:03:C2:34 >> $LOGFILE 2>&1
# RFCOMM 장치 확인
# if ls /dev | grep -q rfcomm; then
#   echo "RFCOMM device created successfully" >> $LOGFILE
# else
#   echo "Failed to create RFCOMM device" >> $LOGFILE
#   exit 1
# fi
# RFCOMM 장치가 연결을 기다리는 상태로 설정
sudo rfcomm listen 0 1 & >> $LOGFILE 2>&1

sleep 5 >> $LOGFILE 2>&1

echo "Running Python script..." >> $LOGFILE
sudo /usr/bin/python3 /home/asurada/Desktop/asurada/test_0826.py >> $LOGFILE 2>&1



# echo "Starting OBD service..."
# date

# # Bluetooth 초기화 및 설정
# sudo rfcomm release 0  # 혹은 해당하는 RFCOMM 번호
# sudo hciconfig hci0 up
# sudo rmmod rfcomm
# sudo modprobe rfcomm
# sudo rfcomm bind 0 00:1D:A5:03:C2:34
# sudo rfcomm listen 0 1 &

# # Python 스크립트 실행
# # 기본 시스템 Python을 사용하여 스크립트를 실행합니다.
# # python3 /home/asurada/Desktop/asurada/websocket_server.py
# /usr/bin/python3 /home/asurada/Desktop/asurada/test_0826.py