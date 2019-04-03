from slackbot.bot import respond_to
from slackbot.bot import default_reply
from slackbot.bot import listen_to
import random
import sqlite3

from slacker import Slacker
import slackbot_settings

class DB:
    def __init__(self):
        self.DB_NAME = "main.db"
        self.TABLE_NAME = "default_table"
        # self.isDBConnected = False
        self.connect()
        self.createTableIfNotExist()

    def __del__(self):
        self.disconnect()

    def connect(self):
        # DBに接続する
        self.conn = sqlite3.connect(self.DB_NAME)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        if(self.conn is not None):
            self.conn.close()

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
slacker = Slacker(slackbot_settings.API_TOKEN)

@default_reply()
def defaultReply(message):
    message.reply("何か御用でしょうか？")
    if db.isDBConnected():
        message.reply("DBは接続済みですよ。")
    else:
        message.reply("DBはまだ接続されてませんよ。")

# https://blog.bitmeister.jp/?p=3948
# https://qiita.com/do_m_gatoru/items/d6dbb5e5dbca8d96a1cd
# https://qiita.com/Hironsan/items/0373339388f460cebb08
@listen_to("こんにちわ")
def hearQuestion(message):
    # slacker = Slacker(slackbot_settings.API_TOKEN)
    slacker.chat.post_message("dev", "こんにちわ〜")
    slacker.chat.post_message("dev", "瀟洒です。", as_user=True)
    slacker.chat.post_message("dev", message.body["text"])

@respond_to("オウム")
@respond_to("repeat")
def hearQuestion(message):
    # slacker = Slacker(slackbot_settings.API_TOKEN)
    message.reply(message.body["text"])
    slacker.chat.post_message("dev", message.body["text"])

@listen_to("貴方は(.*)ですか？")
@listen_to("あなたは(.*)ですか？")
@listen_to("君は(.*)ですか？")
@listen_to("きみは(.*)ですか？")
def respondYesIam(message, something):
    message.reply("はい、私は{0}です。".format(something))

@respond_to("DB")
def dbAction(message):
    message.reply("少々お待ちください。")
    message.react("+1")
