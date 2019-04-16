import sqlite3
import logging
from datetime import datetime

class DB:

    logger = logging.getLogger(__name__)

    def __init__(self):
        self.conn = None
        self.cursor = None
        # self.isDBConnected = False
        # self.connect()
        # self.createTableIfNotExist()

    def __del__(self):
        self.disconnect()

    def connect(self, dbName):
        # DBに接続する
        self.conn = sqlite3.connect(dbName, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        if(self.conn is not None):
            self.conn.close()
        self.conn = None
        self.cursor = None

    def executeAndCommit(self, sql):
        if not self.isDBConnected(True):
            return False

        self.conn(sql)
        self.conn.commit()
        return True

    def createTableIfNotExist(self, tableName):
        sql = "CREATE TABLE IF NOT EXISTS "
        sql += " " + tableName + " "
        sql += ''' (id INTEGER PRIMARY KEY,
                    key TEXT,
                    value TEXT,
                    time TEXT)
                    '''
        self.conn(sql)
        self.conn.commit()

    def createCurrentDateTimeStr(self):
        return datetime.now().strftime("%Y/%m/%d_%H:%M:%S")

    def insert(self, tableName, key, value, timeStr = None):
        if timeStr is None:
            timeStr = self.createCurrentDateTimeStr()

        sql = "INSERT INTO " + tableName + " "
        sql += "(key, value, time) values (?, ?, ?)"
        data = (key, value, timeStr)
        self.cursor.execute(sql, data)
        self.conn.commit()

    def selectAll(self, tableName):
        return self.cursor.execute("SELECT * FROM " + tableName)

    def getTableList(self):
        result = []

        if not self.isDBConnected(True):
            return result

        self.cursor.execute("select * from sqlite_master where type=\"table\"")

        for table in self.cursor.fetchall():
            result.append(table)

        return result


    def isDBConnected(self, showErrorLogIfNotConnected = False):
        result = self.conn is not None and self.cursor is not None
        if not result:
            if showErrorLogIfNotConnected:
                self.logger.error("DB is not connected.")
        return result
