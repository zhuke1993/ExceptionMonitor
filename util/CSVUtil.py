__author__ = 'ZHUKE'

import MySQLdb
from DBUtil import DBUtil
import csv


class CSVUtil:
    def writeCSV(self):
        with open('eggs.csv', 'wb') as f:
            writer = csv.writer(f)
            dbUtil = DBUtil()
            conn = dbUtil.getConnection()
            cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            cur.execute("select * from agreementrequest")
            r = cur.fetchall()
            for i in r:
                writer = csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(i["oid"])

    if __name__ == '__main__':
        writeCSV(0)
