from slackbot.bot import respond_to
from slackbot.bot import default_reply
from slackbot.bot import listen_to
import random

from slacker import Slacker
import slackbot_settings

@respond_to("r (.*)")
@respond_to("r　(.*)")
@respond_to("ランダム (.*)")
@respond_to("ランダム　(.*)")
def randomSelector(message, content):
    selections = content.split()
    message.reply("私は「" + random.choice(selections) + "」を選択しますわ。")

@listen_to("/r (.*)")
@listen_to("/r　(.*)")
@listen_to("/rand (.*)")
@listen_to("/rand　(.*)")
def randomSelector(message, content):
    selections = content.split()
    message.reply("私は「" + random.choice(selections) + "」を選択しますわ。")
