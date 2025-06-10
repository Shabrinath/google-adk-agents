# google-adk-agents
This repository showcases three distinct types of agents built with the ADK.

### 1\. Simple Greeting Agent 

This is a foundational example demonstrating the basic structure of an ADK agent. It's designed to be a helpful and funny assistant that initiates a conversation by asking for the user's name and then greeting them personally.

**Key Features:**

-   Basic agent definition with `name`, `model`, `description`, and `instruction`.

-   Direct interaction based on predefined instructions.

### 2\. Google Search Integration Agent 

Building upon the simple greeting agent, this example integrates the `google_search` tool, allowing the agent to access real-time information from the web. This expands the agent's knowledge beyond its pre-trained data, making it more dynamic and informative.

**Key Features:**

-   Utilization of the `google_search` tool from `google.adk.tools`.

-   Ability to perform web searches to answer user queries.

### 3\. RAG Agent with Vertex AI Search 

This advanced example demonstrates how to build a Retrieval Augmented Generation (RAG) agent that leverages a custom knowledge base hosted on Google Cloud's Vertex AI Search. This agent is specifically instructed to *only* use the provided knowledge base for answering questions, making it ideal for domain-specific applications where accuracy and controlled information retrieval are paramount.

**Key Features:**

-   Integration with `VertexAiSearchTool` for RAG capabilities.

-   Strict adherence to the provided `data_store_id` for information retrieval.

-   Demonstrates how to handle cases where information is not found in the knowledge base.

-   Emphasis on controlled information access, crucial for enterprise-grade AI applications.
