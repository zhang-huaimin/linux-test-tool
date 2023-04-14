"""
Common API for connect with linux.
"""
from abc import ABC, abstractmethod
from common.re import is_match
import eventlet
from env.connection.keyboard import key_escape
from logging import Logger


class Connect(ABC):
    def __init__(self):
        pass

    def set_log(self, log: Logger):
        self.log = log

    def set_alias(self, alias: str) -> str:
        self.alias = alias
        return self.get_alias()

    def get_alias(self) -> str:
        return self.alias

    def ask(
        self,
        cmd: str,
        pass_flag,
        time=5,
        error_info=None,
        is_check=True,
        fail_flag=None,
    ):
        """Send cmd and recv message within fixed time(sec, min=0.1s) and check.

        if get pass_flag, then stop recv, return True.

        if is_check:
            if timeout, then test failed, print 'timeout' and error_info.
            if get fail_flag, then stop recv, test falied, and print error_info.
        else:
            if timeout, print 'timeout' and error_info, return False.
            if get fail_flag, then stop recv, and print error_info, return False.

        Return:
            status: bool.
            data: str.
        """
        self.recv()
        self.send_LF(cmd)
        status, data = self.recv_check(pass_flag, time, error_info, is_check, fail_flag)
        return status, data

    def recv_check(
        self, pass_flag, time, error_info=None, is_check=True, fail_flag=None
    ):
        data = ''
        status = False
        with eventlet.Timeout(time, False):
            for t in range(time * 10):
                data += self.recv(0.1)
                is_pass = is_match(pass_flag, data)
                is_fail = is_match(fail_flag, data) if fail_flag else False
                status = True if is_pass and not is_fail else False
                if is_pass or is_fail:
                    break

        if not status and error_info:
            # TODO: log
            print(error_info)

        self.log.info("status: {}, data: {}".format(status, data))

        if is_check:
            assert status == True

        self.recv()

        return status, data

    def send_LF(self, cmd=''):
        """Send cmd with LF"""
        self.send(cmd + '\n')

    def send_key(self, key: str):
        """Always you want to simulated keyboard, Expecially ctrl + c.
        Input: key. Find it in map key_escape.
        """
        self.send(key_escape[key])

    def ctrl_c(self):
        self.send_key('ctrl_c')

    @abstractmethod
    def recv(self, time=0.1) -> str:
        """Recieve data from device within fixed time.

        Return:
            data: str. The data should be decoded by UTF8.
        """

    @abstractmethod
    def send(self, cmd: str):
        """Send cmd to device without line break."""

    @abstractmethod
    def close(self):
        """Close current connect."""
