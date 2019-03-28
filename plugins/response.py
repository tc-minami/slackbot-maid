from slackbot.bot import respond_to
from slackbot.bot import default_reply
from slackbot.bot import listen_to

import random

import sqlite3

class DB:
    def __init__(self):
        self.DB_NAME = "main.db"
        self.TABLE_NAME = "default_table"
        # self.isDBConnected = False
        self.connect2DB()
        self.createTableIfNotExist()

    def __del__(self):
        self.conn.close()


    def connect2DB(self):
        # DBに接続する
        self.conn = sqlite3.connect(self.DB_NAME)
        self.cursor = self.conn.cursor()

    def createTableIfNotExist(self):
        sql = "CREATE TABLE IF NOT EXISTS "
        sql += " " + self.TABLE_NAME + " "
        sql += ''' (id INTEGER PRIMARY KEY,
                    key TEXT,
                    value TEXT,
                    time TEXT)
                    '''
        self.conn.execute(sql)
        self.conn.commit()

    def createDateTimeStr(self, year, month, day, hour, min, sec):
        return str(year) + str(month) + str(day)\
        + str(hour) + str(min) + str(sec)

    def isDBConnected(self):
        return self.conn is not None and self.cursor is not None


db = DB()

@default_reply()
def error_func(message):
    message.reply("何か御用でしょうか？")
    if db.isDBConnected():
        message.reply("DBは接続済みですよ。")
    else:
        message.reply("DBはまだ接続されてませんよ。")

def __del__(self):
    message.reply("終了します。お疲れ様でした。")


#
# @listen_to("DB")
