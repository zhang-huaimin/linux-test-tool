from env.connection.ssh import Ssh
from env.connection.serial import Serial
from env.connection.shell import Shell


shell_sample = {'type': 'shell'}


class ConnectFactory(object):
    @classmethod
    def create(self, con_conf, log):
        con_type = con_conf['type'].lower()
        con = None

        if con_type == 'ssh':
            con = Ssh(con_conf)
        elif con_type == 'serial':
            con = Serial(con_conf)
        elif con_type == 'shell':
            con = Shell()

        con.set_log(log)

        return con
