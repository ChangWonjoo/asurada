#!/bin/bash

LOGFILE="/home/asurada/Desktop/asurada/start_log.txt"

echo "Starting OBD service..." >> $LOGFILE
date >> $LOGFILE

sudo hciconfig hci0 up >> $LOGFILE 2>&1
sudo rmmod rfcomm >> $LOGFILE 2>&1
sudo modprobe rfcomm >> $LOGFILE 2>&1
sudo rfcomm bind 0 00:1D:A5:03:C2:34 >> $LOGFILE 2>&1
ls /dev | grep rfcomm >> $LOGFILE 2>&1
sudo rfcomm listen 0 1 & >> $LOGFILE 2>&1
sleep 15 >> $LOGFILE 2>&1

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