# To install: pip install tavily-python
from tavily import TavilyClient
import json
import os
from dotenv import loadenv

loadenv()
TAVILY_KEY=os.getenv("TAVILY_KEY")

client = TavilyClient(TAVILY_KEY)
response = client.search(
    query="latest uppdates with nvidia",
    # search_depth="advanced"
)
print(response)
with open('tavily_search.json','w') as file:
    json.dump(response, file, indent=4)