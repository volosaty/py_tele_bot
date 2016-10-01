# -*- coding: utf-8 -*-

import telebot
from telebot import types
import re
import paramiko
import cmd
import sys
import subprocess
from subprocess import call

#pass bot security token as command line argument
token = str(sys.argv[1])

bot = telebot.TeleBot(token)

proc = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)
output = proc.stdout.read()

proc = subprocess.Popen(["free", "-g"], stdout=subprocess.PIPE)
output1 = proc.stdout.read()

proc = subprocess.Popen(["uptime"], stdout=subprocess.PIPE)
output2 = proc.stdout.read()

proc = subprocess.Popen(["cat", "list_txt"], stdout=subprocess.PIPE)
output4 = proc.stdout.read()

proc = subprocess.Popen(["./news.sh"], stdout=subprocess.PIPE)
output5 = proc.stdout.read()



# Handles all text messages that contains the commands '/start' or '/help'.
@bot.message_handler(commands=['fuck'])
def servers_list(message):
    bot.reply_to(message, text=output4)
    pass

@bot.message_handler(commands=['free'])
def server_free(message):
    bot.reply_to(message, text=output1)
    pass

@bot.message_handler(commands=['news'])
def server_free(message):
    bot.reply_to(message, text=output5)
    pass


if __name__ == '__main__':
    bot.polling(none_stop=True)
