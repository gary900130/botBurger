from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI()
print(llm.predict("你好嗎？"))