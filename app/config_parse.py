from configparser import ConfigParser


def parser():
    config = ConfigParser()
    config.read("config.ini")

    return config
