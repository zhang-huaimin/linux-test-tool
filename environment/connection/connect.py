"""
Common API for connect with linux.
"""
from abc import ABC, abstractmethod
from common.re import is_match
import eventlet


class Connect(ABC):
    def __init__(self):
        pass

    def set_alias(self, alias: str):
        self.alias = alias
        return self.get_alias()

    def get_alias(self):
        return self.alias

    def ask(self, cmd: str, pass_flag, time=5, error_info=None, is_check=True, fail_flag=None):
        """Send cmd and recv message within fixed time(sec, min=0.1s) and check.
    
        if get pass_flag, then stop recv, return True.

        if is_check:
            if timeout, then test failed, print 'timeout' and error_info.
            if get fail_flag, then stop recv, test falied, and print error_info.

        if !is_check:
            if timeout, print 'timeout' and error_info, return False.
            if get fail_flag, then stop recv, and print error_info, return False.
        
        Return: 
            status: bool.
            data: str.
        """
        self.recv()
        self.send_with_line_break(cmd)
        status, data = self.recv_check(pass_flag, time, error_info, is_check, fail_flag)
        return status, data

    def recv_check(self, pass_flag, time, error_info=None, is_check=True, fail_flag=None):
        data = ''
        status = False
        with eventlet.Timeout(time, False):
            for t in range(time * 10):
                data += self.recv(0.1)
                is_pass = is_match(pass_flag, data)
                is_fail = is_match(fail_flag, data) if fail_flag else False
                status = True if is_pass and not is_fail else False
                if (is_pass or is_fail):
                    break

        if (not status and error_info):
            # TODO: log
            print(error_info)

        print("is_pass:{}, is_fail:{}\ndata: {}".format(is_pass, is_fail, data))

        if (is_check):
            assert status == True

        self.recv()

        return status, data
    
    def send_with_line_break(self, cmd: str):
        self.send(cmd + '\n')

    @abstractmethod
    def recv(self, time=0.1):
        """Recieve data from device within fixed time.
        
        Return: 
            data: str. The data should be decoded by UTF8.
        """

    @abstractmethod
    def send(self, cmd: str):
        """Send cmd to device without line break.
        """

    @abstractmethod
    def close(self):
        """Close current connect.
        """


def ConnectRepo():
    def __init__():
        pass


