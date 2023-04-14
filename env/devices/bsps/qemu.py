from env.devices.bsp import Bsp


class Qemu(Bsp):
    def burn_img(self):
        self.dev.log.info("it's qemu")

    def reboot(self):
        pass