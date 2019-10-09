import configparser


def parse_config_file(ns):
    config = configparser.ConfigParser()
    config.read(ns.config)
    return config