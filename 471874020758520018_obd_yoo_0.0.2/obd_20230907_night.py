import obd
import json
import threading
from multiprocessing import Queue
import sys
import time
import datetime

data_queue = Queue()

class main:
	def __init__(self):
		with open('./command_list.json', 'r', encoding = 'utf-8') as f:
			self.system_data = json.load(f)
		self.cmd_rpm = self.system_data["rpm"]
		self.time_delay = self.system_data["time_delay"]

		if self.system_data["type"] != "Async":
			self.conn1 = obd.OBD()
			self.RPM = obd.commands[self.cmd_rpm]
			self.response = self.conn1.query(self.RPM)
		else:
			self.conn1 = obd.Async()

	def get_now(self):
		now = datetime.datetime.now()
		now = now - datetime.timedelta(microseconds = now.microsecond)
		now = now.strftime("%y/%m/%d %H:%M:%S")
		return now

################### Async #####################
	def get_value_async(self, v):
		print(v.value)
		print("step1")

	def get_param_async(self):
		rpm = self.system_data["rpm"]
		cmd1 = obd.commands[rpm]

		self.conn1.watch(cmd1, callback = self.get_value_async)
		self.conn1.start()
		res1 = self.conn1.query(cmd1) # rpm
		print(res1.value)
		return res1

################### OBD #####################
	def get_RPM_obd(self):
		while True:
			try:
				#self.response = self.conn1.query(self.RPM)
				data_queue.put(self.response.value)
				print("data_queue putting")
				time.sleep(self.time_delay)
			except KeyboardInterrupt:
				print("exit")
				sys.exit(0)

	def queue_get(self):
		while True:
			datetime_now = self.get_now()
			if data_queue.qsize() > 0:
				queue_res = data_queue.get()
				print(datetime_now + " queue_res : ", queue_res)

if __name__ == "__main__":
	start = main()
	t1 = threading.Thread(target = start.get_RPM_obd)
	t1.daemon = True
	t1.start()
	try:
		start.queue_get()
	except KeyboardInterrupt:
		sys.exit(0)
	#start.get_param_async()

