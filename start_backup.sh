sudo hciconfig hci0 up
sudo rmmod rfcomm
sudo modprobe rfcomm
sudo rfcomm bind 0 00:1D:A5:03:C2:34
ls /dev | grep rfcomm
sudo rfcomm listen 0 1 &
sleep 15
sudo python home/asurada/Desktop/asurada/test_0826.py