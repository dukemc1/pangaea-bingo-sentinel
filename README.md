# pangaea-bingo-sentinel.py
Python3 script to monitor Harmony "pangaea" instance. Do take note that this only works if "BINGO" is enabled.


# Take note to replace the following in the script
* line 10: INSERT_TOKEN_HERE
Chat with "BotFather" in Telegram to obtain your own token

* line 50: INSERT_CHAT_ID_HERE
Replace this with your own telegram chat id or telegram channel id

* line 53: INSERT_CHAT_ID_HERE
Replace this with your own telegram chat id or telegram channel id

# Add the monitoring script to cron (crontab -e)
*/15 * * * * /SOME_PATH_TO/pangaea-bingo-sentinel.py
(do not forget to make the file executable, chmod +x pangaea-bingo-sentinel.py)
