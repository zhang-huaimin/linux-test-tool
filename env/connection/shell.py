"""
Connect with linux by shell directly.

Expecially for conection between ltt and ltt's server.
"""
import subprocess
from time import sleep
from queue import Queue
from env.connection.connect import Connect
from env.connection.keyboard import rev_key_escape

class Shell(Connect):
    def __init__(self):
        self._shell = _Shell()

    def recv(self, time=0.1) -> str:
        sleep(time)
        data = self._shell.read()
        return data

    def send(self, cmd):
        self._shell.write(cmd)

    def close(self):
        self._shell.close()


class _Shell(object):
    def __init__(self):
        self.in_buf = Queue()
        self.subproc = None

    def write(self, cmd):
        if cmd in rev_key_escape or '\n' in cmd:
            while not self.in_buf.empty():
                cmd = self.in_buf.get() + cmd

            self.subproc = subprocess.Popen(cmd, shell=True, \
                            stdin=subprocess.PIPE, \
                            stdout=subprocess.PIPE, \
                            stderr=subprocess.PIPE, \
                            encoding="UTF-8")
        else:
            self.in_buf.put(cmd)

    def read(self):
        stdout = ""

        # subproc not be None, and cmd was finished.
        if self.subproc and not self.subproc.poll():
            stdout = self.subproc.communicate()[0]

        self.close()

        return stdout

    def close(self):
        if self.subproc:
            self.subproc.kill()

        self.subproc = None
