from linebot import LineBotApi, WebhookHandler, exceptions
from linebot.models import TextSendMessage, events
from dotenv import load_dotenv
# from langchain import OpenAI
from flask import Flask, request
from openai import OpenAI
import json
import os

load_dotenv()


app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
  body = request.get_data(as_text=True)
  json_data = json.loads(body)
  print(json_data)
  CHANNEL_ACCESS_TOKEN = os.environ.get("lineBotToken")
  OpenAI.api_key = os.environ.get("OPENAI_API_KEY")
  line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
  LINESECRET = os.environ.get("lineSecret")
  handler = WebhookHandler(LINESECRET)

  signature = request.headers['X-Line-Signature']
  handler.handle(body, signature)
  tk = json_data['events'][0]['replyToken']          # 取得 reply token
  msg = json_data['events'][0]['message']['text']    # 取得使用者發送的訊息
  """
  llm = OpenAI(model="gpt-3.5-turbo"	, max_tokens=50)

  replyMsg = llm(msg)
  """
  client = OpenAI()
  chat_completion = client.chat.completions.create(
    messages=[
      {
        "role": "user",
        "content": msg,
      }
    ],
    model="gpt-3.5-turbo",
  )
  text_message = TextSendMessage(text=chat_completion.choices[0].message.content)
  line_bot_api.reply_message(tk,text_message)       # 回傳訊息


if __name__ == "__main__":
  app.run()