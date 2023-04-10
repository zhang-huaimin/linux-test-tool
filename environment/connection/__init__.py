from environment.connection.connect import Connect
from environment.connection.ssh import Ssh


class ConnectFactory(object):
    def create(self, conf):
        connect_conf = conf['connect']
        if connect_conf['method'] == 'ssh':
            ssh = Ssh(connect_conf)

            return Ssh(connect_conf)


class ConnectRepo(object):
    def __init__(self):
        self.repo = {}
    
    def add(self, alias:str, con: Connect):
        self.repo[alias] = con
    
    def delete(self, alias):
        self.repo[alias].clear()
        self.repo.pop(alias, 'Can not find/del alias: {}'.format(alias))
    
    def update(self, alias, con:Connect):
        self.repo[alias].clear()
        self.repo[alias] = con
    
    def search(self, alias):
        return self.repo[alias]

    def ls(self):
        return self.repo
