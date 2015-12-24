__author__ = 'ZHUKE'
import ConfigParser


class PropertiesUtil:
    config = ConfigParser.RawConfigParser()
    config.read("../conf/config.properties")

    def get(self, section, prop):
        return self.config.get(section, prop)
