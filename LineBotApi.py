from linebot import LineBotApi, WebhookHandler, exceptions
from linebot.models import TextSendMessage, events
from dotenv import load_dotenv
import os

load_dotenv()

CHANNEL_ACCESS_TOKEN = os.getenv("lineBotToken")

try:
    line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
    line_bot_api.broadcast(TextSendMessage(text="新年快樂"))
except exceptions.LineBotApiError as e:
    print(f"LineBotApiError: {e.status_code} {e.error.message}")
except Exception as e:
    print(f"Exception: {e}")
