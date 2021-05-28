# -*- coding: utf-8 -*-

from slack_cleaner2 import *
import os
import sys

class CleanSlack:

    SLACK_TOKEN = None
    MAX_TRIES = 50
    retries = 0
    slack_obj = None

    def __init__(self):
        self.SLACK_TOKEN = os.getenv('SLACK_TOKEN') # set this variable in your os/console environment
        if not self.SLACK_TOKEN:
            print('The env virable SLACK_TOKEN is not set.')
            exit()

        if len(sys.argv) < 2:
            print('You need to specify which channels to delete messages')
            print('Eg: clean.py bot-.* errors-.* .*-errors .*-bot')
            exit()

        self.slack_obj = SlackCleaner(self.SLACK_TOKEN)
        self.execute()

    def delete_messages(self):
        success = False
        try:
            i = 0
            for param in sys.argv:
                if i != 0:
                    for msg in self.slack_obj.msgs(filter(match(param), self.slack_obj.conversations)):
                        msg.delete(replies=True, files=True)
                i = i + 1
            success = True
        except:
            self.retries += 1
            success = False

        return success

    def execute(self):
        success = False
        while not success and self.retries < self.MAX_TRIES:
            print ("\n>> Starting ...\n")
            success = self.delete_messages()

        if self.retries == self.MAX_TRIES:
            print("\n\n>> Reached the max tries number of {}".format(self.MAX_TRIES))
        else:
            print("\n\n>> Finished. No more messages to delete")

try:
    CleanSlack()
except KeyboardInterrupt:
    print("\n\n>> Canceled by the user.")