from env.devices.bsp import Bsp
from env.devices.bsps.qemu import Qemu


class BspFactory(object):
    @classmethod
    def create(self, bsp_type, dev):
        bsp_type = bsp_type.lower()
        if bsp_type == 'qemu':
            return Qemu(dev)
        return None