from env.connection.connect import Connect
from env.connection import ConnectFactory, shell_sample
from common.file_parser import YamlParser
from queue import Queue


class DeviceModel(object):
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


class Server(DeviceModel):
    # TODO: Device need talk with linux servers for resource.
    pass


class Device(DeviceModel):
    def __init__(self):
        super().__init__()
        self.set_i()
        self.servers = {}

    def set_i(self):
        """I am ltt's server.
        Can exec cmd which from ltt's testcases in ltt's server.
        """
        self.i = Server()
        self.i.add_con(ConnectFactory().create(shell_sample))

    def add_server():
        pass


class DevicePool(object):
    def __init__(self, conf_file):
        self.pool = Queue()
        parser = DeviceYamlParser(conf_file)
        for conf in parser.yiled_dev_conf():
            device = Device()
            device.add_con(ConnectFactory().create(conf))
            device.set_alias(conf['alias'])
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