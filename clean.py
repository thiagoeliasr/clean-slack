# -*- coding: utf-8 -*-

from slack_cleaner2 import *
import os
import sys

SLACK_TOKEN = os.getenv('SLACK_TOKEN') # set this variable in your os/console environment

if not SLACK_TOKEN:
    print('The env virable SLACK_TOKEN is not set.')
    exit()

if len(sys.argv) < 2:
    print('You need to specify which channels to delete messages')
    print('Eg: clean.py bot-.* erros-.* .*-errors .*-bot')
    exit()

s = SlackCleaner(SLACK_TOKEN)

i = 0
for param in sys.argv:
    if i != 0:
        for msg in s.msgs(filter(match(param), s.conversations)):
            msg.delete(replies=True, files=True)
    i = i + 1
