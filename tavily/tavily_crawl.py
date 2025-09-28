# To install: pip install tavily-python
from tavily import TavilyClient
import json
import os
from dotenv import load_dotenv

load_dotenv()
TAVILY_KEY=os.getenv("TAVILY_KEY")

from tavily import TavilyClient

tavily_client = TavilyClient(api_key=TAVILY_KEY)
response = tavily_client.crawl("https://docs.tavily.com", instructions="Find all pages on the Python SDK")

print(response)

with open('tavily_crawl.json','w') as file:
    json.dump(response, file, indent=4)
