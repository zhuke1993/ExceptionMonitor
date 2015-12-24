__author__ = 'ZHUKE'
import MySQLdb
from PropertiesUtil import PropertiesUtil


class DBUtil:
    def getConnection(self):
        return MySQLdb.connect(PropertiesUtil().get("db", "host"),
                               PropertiesUtil().get("db", "user"),
                               PropertiesUtil().get("db", "passwd"),
                               PropertiesUtil().get("db", "db"))
