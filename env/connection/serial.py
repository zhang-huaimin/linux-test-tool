"""
Connect with linux by serial.
"""
from env.connection.connect import Connect
from time import sleep
import serial


class Serial(Connect):
    def __init__(self, conf):
        self.serial = serial.Serial(port=conf['port'], baudrate=conf['baudrate'], timeout=0)
        self.serial.flush()

    def recv(self, time=0.1):
        sleep(time)
        return self.serial.read(65535).decode('UTF-8')

    def send(self, cmd: str):
        self.serial.write(cmd.encode('UTF-8'))

    def close(self):
        self.close()