from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="google_search_agent",
    model="gemini-2.0-flash",
    description="google search agent",
    instruction="""
    You are a helpful funny assistant that greets the user. 
    You can search for real-time information using the google_search tool.
    """,
    tools=[google_search],
)

