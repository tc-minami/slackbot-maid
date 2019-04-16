from slackbot.bot import respond_to
from slackbot.bot import default_reply
from slackbot.bot import listen_to
import random

from slacker import Slacker
import slackbot_settings

import re

# https://qiita.com/jnchito/items/893c887fbf19e17d3ff9

@listen_to("^(?:r|ランダム)[\s|　]+(.*)")
def randomSelector(message, content):
    selections = content.split()
    message.reply("私は「" + random.choice(selections) + "」を選択しますわ。")

@listen_to("^(?:rl|rlist|ランダムリスト)[\s|　]+([^\d\s　+].*)")
def randomSelector(message, content):
    selections = content.split()
    random.shuffle(selections)
    response = "ランダムリストを作成しておきましたよ。\n"
    for index, selection in enumerate(selections):
        response += str(index + 1) + " : " + selection + "\n"
    message.reply(response)

@listen_to("^(?:rl|rlist|ランダムリスト)[\s|　]+(\d+)[\s|　]+(.*)")
def selectRandom(message, maxCount, content):
    selections = content.split()

    response = "ランダムリストを作成しておきましたよ。\n"
    for index in range(int(maxCount)):
        response += str(index + 1) + " : " + str(random.choice(selections)) + "\n"

    message.reply(response)

@listen_to("^(?<!\d)(\d{1,3}-\d{1,4}-\d{4})(?!\d)")
def regExpSample(message, number):
    message.reply("電話番号は共有しちゃ駄目ですよ。\n共有された番号はこちらです : " + number)

    # re.sub("\d\d-\d\d\d\d-\d\d\d\d")

@listen_to("^rint[\s|　]*(\d+)[\s|　]*?-[\s|　]*?(\d+)")
def selectRandomInt(message, min, max):
    val = random.randrange(int(min), int(max))
    message.reply("ランダムに値を選択しました : val")

@listen_to("^rint[\s|　]*(\d+)[\s|　]+(\d)+[\s|　]*?-[\s|　]*?(\d+)")
def selectRandomInt(message, count, min, max):
    response = "ランダムに値を選択しましたよ。\n"

    message.reply(str(count) + " : " + str(min) + " : " + str(max))

    for index in range(int(count)):
        val = random.randrange(int(min), int(max))
        response += str(index + 1) + " : " + str(val) + "\n"

    message.reply(response)

# @respond_to("rl (.*)")
# @respond_to("rl　(.*)")
# @respond_to("ランダム (.*)")
# @respond_to("ランダム　(.*)")
