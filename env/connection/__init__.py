from env.connection.connect import Connect
from env.connection.ssh import Ssh
from env.connection.serial import Serial
from env.connection.shell import Shell


shell_sample = {
    'connect': {'method': 'shell'}
}

class ConnectFactory(object):
    def create(self, conf):
        connect_conf = conf['connect']
        con = None

        if connect_conf['method'] == 'ssh':
            con = Ssh(connect_conf)
        elif connect_conf['method'] == 'serial':
            con = Serial(connect_conf)
        elif connect_conf['method'] == 'shell':
            con = Shell()

        return con