import yaml


class YamlParser(object):
    def __init__(self, yaml_path):
        with open(yaml_path, "r") as file:
            self.conf = yaml.safe_load(file)