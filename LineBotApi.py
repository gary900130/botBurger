from linebot import LineBotApi, WebhookHandler, exceptions
from linebot.models import TextSendMessage, events
from datetime import datetime
import netifaces
import os
import logging

# 讀取 LINE BOT API
CHANNEL_ACCESS_TOKEN = os.environ.get("lineBotToken")

# 設定日誌格式
logging.basicConfig(filename='example.log', level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%s')
logging.info('漢堡 啟動！')

# 取得IP位置
ip = netifaces.ifaddresses('enp0s8')[netifaces.AF_INET][0]['addr']
logging.info(f'找到你家地址了，在{ip}')

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
# 從日誌檔案中讀取最後兩行
with open('example.log', 'r') as log:
    last_two_lines = log.readlines()[-2:]

# 對每一行進行廣播
for line in last_two_lines:
    line_bot_api.broadcast(TextSendMessage(text=line.strip()))

# line_bot_api.broadcast(TextSendMessage(text="我是漢堡"))
