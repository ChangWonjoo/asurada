import obd
import time
import asyncio
import websockets
import json

# make conn with OBD
def connOBD():
    print("OBD device searching...")
    
    connection = obd.OBD()
    if connection.is_connected():
        print("OBD connected successfully.")
        return connection
    else:
        print("Failed to connect.")
        return None
    
#def connOBD2222():
#    print("OBD device searching...")
#    max_retries = 10
#    retries = 0
#    connection = None
#
#    while retries < max_retries:
#        connection = obd.OBD()
#        if connection.is_connected():
#            print("OBD connected successfully.")
#            return connection
#        else:
#            print(f"Connection failed. Retrying in 5 seconds... ({retries+1}/{max_retries})")
#            retries += 1
#            time.sleep(5)
#
#    print("Failed to connect to OBD device after 5 attempts.")
#    return None

# Function to query OBD data
async def query_obd_data(websocket, path, connection):
    retries = 0

    if connection.is_connected():
        print("------------obd is connected-------------")
        while True:
            try:
                rpm = connection.query(obd.commands.RPM)
                speed = connection.query(obd.commands.SPEED)

                print(f"rpm: {rpm} //// speed: {speed}")
                rpmNumber = rpm.value.magnitude if rpm.value is not None else 0
                speedNumber = speed.value.magnitude if speed.value is not None else 0
                print(type(rpmNumber))
                
                
                print(f"rpmvalue: {rpmNumber} //// speedvalue: {speedNumber}")
                data = {
                    "rpm": rpmNumber,
                    "speed": speedNumber
                }
                await websocket.send(json.dumps(data))

                await asyncio.sleep(0.1)

            except KeyboardInterrupt:
                break

    else:
        print("obd connect failed")

# conn OBD
obd_connection = None

# WebSocket server setup
obd_connection = connOBD()

#while obd_connection == None:
#    print("obd conn while start")
#    obd_connection = connOBD()
    
print("obd conn while end")
start_server = websockets.serve(lambda ws, path: query_obd_data(ws, path, obd_connection), "localhost", 8765)

# Start the WebSocket server
loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
print("WebSocket server started")
loop.run_forever()


# -----------------------------------0826.py origin -----------
# import obd
# import time

# #obd.logger.setLevel(obd.logging.DEBUG) # enables all debug information
# print("obd device searching....")

# # 直接シリアルポートを指定
# connection = obd.OBD() # auto-connects to USB or RF port
# # connection = obd.OBD("/dev/ttyUSB0")

# if connection.is_connected():
#     print (connection.is_connected())
#     print("------------obd is connected-------------")

#     while(True):
#         try:
#             rpm = connection.query(obd.commands.RPM) # select an OBD command (sensor) & send the command, and parse the response
#             speed = connection.query(obd.commands.SPEED)

#             print(f"rpm:{rpm.value} || speed:{speed.value}") # returns unit-bearing values thanks to Pint
#             #print(f"rpm:{rpm.value.magnitude} || speed:{speed.value.magnitude}") # returns unit-bearing values thanks to Pint

#             time.sleep(0.1)

#         except KeyboardInterrupt:
#             pass


# else :
#     # 利用できるシリアルポートから選択する
#     ports = obd.scan_serial()      # ['/dev/ttyUSB0', '/dev/ttyUSB1']
#     connection = obd.OBD(ports[0]) 
#     print("obd connect failed & try again")

#     if connection.is_connected():
#         print("obd is connected in seconde trial")

#     else :
#         print("obd connect failed")
#         connection.close()


# --------------------------test for websocket--------------
# import asyncio
# import websockets
# import json
# import time

# print("obd_data start")

# async def obd_data(websocket, path):
#     while True:
#         rpm = 3000 + int(time.time() % 100)
#         speed = 60 + int(time.time() % 20)
#         print(f"rpm: {rpm} // speed: {speed}")
#         data = {
#             "rpm": rpm,
#             "speed": speed
#         }

#         await websocket.send(json.dumps(data))
#         await asyncio.sleep(1)

# start_server = websockets.serve(obd_data, "localhost", 8765)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(start_server)
# print("WebSocket server started")
# loop.run_forever()
