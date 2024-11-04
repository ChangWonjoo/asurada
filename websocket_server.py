import asyncio
import websockets
import json
import time

print("obd_data start")
# test_0826.py의 시작 부분에 로그 남기기
with open("/home/asurada/Desktop/asurada/startup.log", "a") as log_file:
    log_file.write("Script started at: " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")


async def obd_data(websocket, path):
    while True:
        rpm = 3000 + int(time.time() % 100)
        speed = 60 + int(time.time() % 20)
        print(f"rpm: {rpm} // speed: {speed}")
        data = {
            "rpm": rpm,
            "speed": speed
        }

        await websocket.send(json.dumps(data))
        await asyncio.sleep(1)

start_server = websockets.serve(obd_data, "localhost", 8765)

loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
print("WebSocket server started")
loop.run_forever()
