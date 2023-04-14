from env.connection.connect import Connect
from env.connection import ConnectFactory, shell_sample
from common.file_parser import YamlParser
from queue import Queue
from env.devices.bsps import BspFactory
from env.devices.bsp import Bsp
from logging import getLogger


class DeviceModel(object):
    def __init__(self, conf):
        self.conf = conf
        # TODO: cons should can be choosen by strategy.
        self.cons = []
        self.set_alias(conf['alias'])
        self.init_log()
        pass

    def set_alias(self, alias: str):
        self.alias = alias

    def add_con(self, con: Connect):
        self.con = con
        self.cons.append(con)

    def del_con(self, con: Connect):
        self.cons.remove(con)

    def init_log(self):
        self.log = getLogger(self.alias)


class Server(DeviceModel):
    # TODO: Device need talk with linux servers for resource.
    pass


class Device(DeviceModel):
    def __init__(self, conf):
        super().__init__(conf)
        self.set_i()
        self.servers = {}
        self.set_bsp()

    def set_i(self):
        """I am ltt's server.
        Can exec cmd which from ltt's testcases in ltt's server.
        """
        i_conf = self.conf.copy()
        i_conf['alias'] = '{}-i'.format(self.alias)
        self.i = Server(i_conf)
        self.i.add_con(ConnectFactory.create(shell_sample, self.i.log))

    def add_server(self):
        pass

    def set_bsp(self):
        self.bsp = BspFactory.create(self.conf['bsp'], self)


class DevicePool(object):
    def __init__(self, conf_file):
        self.pool = Queue()
        parser = DeviceYamlParser(conf_file)
        for conf in parser.yiled_dev_conf():
            device = Device(conf)
            device.add_con(ConnectFactory.create(conf['connect'], device.log))
            self.pool.put(device)
        pass

    def put(self, device: Device):
        self.pool.put(device)

    def get(self):
        return self.pool.get()


class DeviceYamlParser(YamlParser):
    def get_devs_conf(self):
        self.devs = self.conf['devices']
        # TODO. log devs
        return self.devs

    def yiled_dev_conf(self):
        for dev in self.get_devs_conf():
            yield dev['device']
