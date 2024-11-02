# websocket_server.py
import asyncio
import websockets
import json
import time

async def obd_data(websocket, path):
    while True:
        # 예시로 RPM과 속도를 임의로 생성
        rpm = 3000 + int(time.time() % 100)  # 예시로 생성된 RPM 데이터
        speed = 60 + int(time.time() % 20)   # 예시로 생성된 속도 데이터

        data = {
            "rpm": rpm,
            "speed": speed
        }

        await websocket.send(json.dumps(data))
        await asyncio.sleep(1)  # 1초마다 데이터 전송

start_server = websockets.serve(obd_data, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
