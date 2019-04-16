from slackbot.bot import respond_to
from slackbot.bot import default_reply
from slackbot.bot import listen_to

from .db import DB

__DB_NAME = "main.db"

# TABLE
__TABLE_DEF = "default_table"
__TABLE_FAMILY_TASKS = "table_family_tasks"
__TABLE_FAMILY_MISTAKES = "table_family_mistakes"
__TABLE_FAMILY_TODO = "table_family_todo"
__TABLE_FAMILY_CATEGORY = "table_house_category"

# TABLE CONSTANTS
__TABLE_STAT_HIDE = 0
__TABLE_STAT_SHOW = 1

db = DB()

@listen_to("テーブル確認")
def test(message):
    list = db.getTableList()
    result = ""
    for table in list:
        result += str(table) + "\n"

    message.reply("テーブル一覧を取得しました。\n" + result)

@listen_to("^[Dd][Bb][\s　]+[Ss]tart[\s　]*$")
def startDB(message):
    if db.isDBConnected(False):
        message.reply("DBはもう起動済みですよ。")
    else:
        db.connect(__DB_NAME)
        initDB(message)
        message.reply("DBを起動しましたわ。")

@listen_to("^[Dd][Bb][\s　]+[Ss]top[\s　]*$")
def stopDB(message):
    if db.isDBConnected(False):
        db.disconnect()
        message.reply("DBを停止しましたわ。")
    else:
        message.reply("DBはもう停止済みですよ。")

@listen_to("^[Dd][Bb][\s　]+[Ii]nit[\s　]*$")
def initDB(message):
    if not db.isDBConnected(False):
        showDBNotConnectedError()
        return

    createTableIfNotExist(message)
    message.reply("DBを初期化しました。")

@listen_to("^[Dd][Bb][\s　]+[Aa]dd[\s　]*(\w+)[\s　]*(\w+)$")
def addData2DB(message, key, value):
    if not db.isDBConnected(False):
        showDBNotConnectedError()
        return

    createTableIfNotExist(message)
    db.insert(__TABLE_DEF, key, value)
    message.reply("DBにデータを追加しました。")

@listen_to("^[Dd][Bb][\s　]+[Ss]how[\s　][Aa]ll[\s　]*$")
def showDBData(message):
    if not db.isDBConnected(False):
        showDBNotConnectedError()
        return

    message.reply("DBの中身を確認しますね。")
    result = "DBの中身はこちらです。\n";
    for row in db.selectAll(__TABLE_FAMILY_TASKS):
        result += str(row) + "\n"

    message.reply(result)

def showDBNotConnectedError(self):
    if not db.isDBConnected(False):
        message.reply("まずはDBを起動してくださいね。")

def createTableIfNotExist(message):
    # Defaut DB
    # defTableSQL = "create table if not exists " + __TABLE_DEF + " "
    # defTableSQL += ''' (id INTEGER PRIMARY KEY,
    #             key TEXT,
    #             value TEXT,
    #             time TEXT)
    #             '''
    # if not db.executeAndCommit(defTableSQL):
    #     message.reply("Table1の追加に失敗しました。")

    db.createTableIfNotExist(__TABLE_DEF)

    tasksTableSql = "create table if not exists " + __TABLE_FAMILY_TASKS + " "
    tasksTableSql += '''
                (id integer primary key,
                category text not null,
                content text not null,
                description,
                status integer not null,
                init_update text not null,
                last_update text not null)
                '''
    if not db.executeAndCommit(tasksTableSql):
        message.reply("Table2の追加に失敗しました。")

    message.reply("Tableの登録が完了しました。")
