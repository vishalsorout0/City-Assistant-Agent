from dotenv import load_dotenv
import os
import requests

from tavily import TavilyClient
from langchain.tools import tool
from langchain_mistralai import ChatMistralAI
from langchain.agents import create_agent

load_dotenv()


@tool
def get_weather(city: str) -> str:
    """Get current weather of a city."""

    api_key = os.getenv("OPENWEATHER_API_KEY")

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if str(data.get("cod")) != "200":
            return data.get("message", "Weather not found.")

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]

        return f"Weather in {city}: {desc}, {temp}°C"

    except Exception as e:
        return str(e)


tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@tool
def get_news(city: str) -> str:
    """Get the latest news about a city."""

    try:
        response = tavily.search(
            query=f"latest news in {city}",
            search_depth="basic",
            max_results=3,
        )

        results = response.get("results", [])

        if not results:
            return "No news found."

        news = []

        for item in results:
            news.append(
                f"Title: {item['title']}\n"
                f"Summary: {item['content']}\n"
                f"Source: {item['url']}"
            )

        return "\n\n".join(news)

    except Exception as e:
        return str(e)


llm = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0
)

agent = create_agent(
    llm,
    tools=[get_weather, get_news],
    system_prompt="You are a helpful city assistant."
)