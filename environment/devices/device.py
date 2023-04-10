from environment.connection.connect import Connect
from environment.connection import ConnectFactory
from common.file_parser import YamlParser
from queue import Queue


class Device(object):
    def __init__(self):
        self.cons = []
        pass

    def set_alias(self, alias: str):
        self.alias = alias

    def add_con(self, con: Connect):
        self.con = con
        self.cons.append(con)

    def del_con(self, con: Connect):
        self.cons.remove(con)


class DevicePool(object):
    def __init__(self, conf_file):
        self.pool = Queue()
        parser = DeviceYamlParser(conf_file)
        for conf in parser.yiled_dev_conf():

            device = Device()

            device.add_con(ConnectFactory().create(conf))

            device.set_alias(conf['alias'])

            self.pool.put(device)

    def put(self, device: Device):
        self.pool.put(device)
    
    def get(self):
        return self.pool.get()


class DeviceYamlParser(YamlParser):
    def get_devs_conf(self):
        self.devs = self.conf['devices']
        # TODO. 记录devs到日志中
        return self.devs

    def yiled_dev_conf(self):
        for dev in self.get_devs_conf():
            yield dev['device']