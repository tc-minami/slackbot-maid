from slackbot.bot import respond_to
from slackbot.bot import default_reply
from slackbot.bot import listen_to

import random

@default_reply()
def error_func(message):
    message.reply("…？\n何か御用でしょうか？")

@respond_to("おみくじ")
def lottery(message):
    results = ["大吉", "中吉", "吉", "凶", "大凶"]
    percentage = [10, 25, 30, 25, 10]

    rnd = random.randint(1, sum(percentage))
    val = 0
    hit = 0

    for i in range(0, len(results) - 1):
        val += percentage[i - 1]
        if rnd <= val and hit == 0:
            hit = i

    message.reply("今日の貴方の運勢は【" + results[hit] + "】です！")


@respond_to("暇")
def scold(message):
    message.send("サボりは駄目ですよ？")
