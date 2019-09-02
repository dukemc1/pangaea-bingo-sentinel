#!/usr/bin/env python3

from datetime import datetime as dt
import time
import os
import json

import telegram
## chat with BotFather to get a token
bot = telegram.Bot(token='INSERT_TOKEN_HERE')

## VARIABLES
MESSAGE = ""


## get that timestamp
def gimme_tmstamp(logfile):
    with open(lfile) as fin:
        for line in fin:
            if "BINGO" in line:
                present = line
    jout = json.loads(present)
    return jout['time']


## timestamp = '''2019-08-24T17:54:13+08:00'''
def parse_tmstamp(tmstamp):
    fmt = "%Y-%m-%dT%H:%M:%SZ"
    strtmstamp = time.strptime(tmstamp.split('+')[0], fmt)
    return int(time.mktime(strtmstamp))


## isolate the log file
thome = os.environ.get('HOME')
tfiles = os.listdir(os.path.join(thome, 'latest'))
tfile = [ f for f in tfiles if (f.startswith('zerolog') and f.endswith('9000.log')) ]
lfile = os.path.join(thome, "latest", tfile[-1])


## gather data
logtime = gimme_tmstamp(lfile)
ltmstamp = parse_tmstamp(logtime)
ntmstamp = int(dt.now().timestamp())

# PROGRAM LOGIC
timediff = ntmstamp - ltmstamp

if timediff > 3600:
    MESSAGE += "ALERT! Last BINGO was more than 1 hour ago."
    bot.sendMessage(chat_id='INSERT_CHAT_ID_HERE', text=MESSAGE)
elif timediff > 900:
    MESSAGE += "WARNING! Last BINGO was more than 15 minutes ago."
    bot.sendMessage(chat_id='INSERT_CHAT_ID_HERE', text=MESSAGE)
else:
    pass
