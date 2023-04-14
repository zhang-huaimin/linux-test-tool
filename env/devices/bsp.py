"""Abstract device type, which called by Bsp in this project.

Bsp's defines should be write into bsps/, such as qemu.
"""


class Bsp(object):
    def __init__(self, device):
        self.dev = device

    def burn_img(self):
        pass

    def reboot(self):
        pass

    def ifconfig(self):
        pass
