import requests
import wikipedia
from langchain.agents import initialize_agent, Tool, AgentType
from langchain_community.chat_models import ChatTongyi
import os
from dotenv import load_dotenv

load_dotenv()
qweather_api_key = os.getenv("qweather_api_key")
qweather_host = os.getenv("qweather_host")
qweather_location_url = os.getenv("qweather_location_url")

llm = ChatTongyi(model="qwen-turbo", api_key=os.getenv("qwen_api_key"))

def get_weather(city_name):
    try:
        location_url = qweather_host + qweather_location_url+ f"?location={city_name}&key={qweather_api_key}"
        loocation_resp= requests.get(location_url).json()
        print(loocation_resp)
    except Exception as e:
        return f"Error fetching weather data: {e}"