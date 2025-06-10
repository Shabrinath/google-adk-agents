from google.adk.agents import Agent
from google.adk.tools.vertex_ai_search_tool import VertexAiSearchTool


root_agent = Agent(
    name="rag_agent",
    model="gemini-2.0-flash",
    description="Agent that can answer questions using Vertex AI Search.",
    instruction="""
    You are a helpful assistant. You must only answer questions using the `vertex_ai_search_tool`.
    If the tool does not return results or the information is not found in the data store, reply with "I don't know" or "No relevant information found."
    Never answer from your own knowledge.
    """
    tools=[VertexAiSearchTool(data_store_id="projects/<PROJECT-ID>/locations/<LOCATION>/collections/default_collection/dataStores/<DATASTORE-ID>")],
)

