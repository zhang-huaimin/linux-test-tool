"""
Connect with linux by ssh.
"""
from environment.connection.connect import Connect
from time import sleep
import paramiko


class Ssh(Connect):
    def __init__(self, conf):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=conf['hostname'], port=int(conf['port']), username=conf['username'], password=conf['password'])
        self.channel = self.ssh.invoke_shell()
        self.channel.setblocking = 0
        self.channel.settimeout = 1

    def recv(self, time=0.1):
        sleep(time)

        if self.channel.recv_ready():
            data = self.channel.recv(65535).decode('UTF-8')
        else:
            data = ''

        return data

    def send(self, cmd):
        self.channel.send(cmd)

    def close(self):
        self.ssh.close()
        self.channel.close()