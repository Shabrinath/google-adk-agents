# google-adk-agents
This repository showcases three distinct types of agents built with the ADK.

## 🧠 What is ADK?

**Google’s Agent Development Kit (ADK)** is a lightweight framework for building multi-modal, tool-using AI agents that run in your local environment — similar to how ChatGPT agents work.

With ADK, you can:
- Build custom AI assistants
- Extend them with external tools (APIs, search, databases)
- Run them locally via a web UI

### 1\. Simple Greeting Agent 

This is a foundational example demonstrating the basic structure of an ADK agent. It's designed to be a helpful and funny assistant that initiates a conversation by asking for the user's name and then greeting them personally.

**Key Features:**

-   Basic agent definition with `name`, `model`, `description`, and `instruction`.

-   Direct interaction based on predefined instructions.
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/5dbe3125-d503-4576-ac56-22bd0484243d" />

### 2\. Google Search Integration Agent 

Building upon the simple greeting agent, this example integrates the `google_search` tool, allowing the agent to access real-time information from the web. This expands the agent's knowledge beyond its pre-trained data, making it more dynamic and informative.

**Key Features:**

-   Utilization of the `google_search` tool from `google.adk.tools`.

-   Ability to perform web searches to answer user queries.
<img width="1435" alt="image" src="https://github.com/user-attachments/assets/3ba8c3cf-8f02-4197-8c61-defb781127e9" />

### 3\. RAG Agent with Vertex AI Search 

This advanced example demonstrates how to build a Retrieval Augmented Generation (RAG) agent that leverages a custom knowledge base hosted on Google Cloud's Vertex AI Search. This agent is specifically instructed to *only* use the provided knowledge base for answering questions, making it ideal for domain-specific applications where accuracy and controlled information retrieval are paramount.

**Key Features:**

-   Integration with `VertexAiSearchTool` for RAG capabilities.

-   Strict adherence to the provided `data_store_id` for information retrieval.

-   Demonstrates how to handle cases where information is not found in the knowledge base.

-   Emphasis on controlled information access, crucial for enterprise-grade AI applications.

Installation
------------

To get started with these examples, you'll need to set up your Python environment and install the Google ADK.

1.  **Clone the repository:**

    ```
    git clone https://github.com/shabrinath/google-adk-agents.git
    cd google-adk-agents

    ```

2.  **Create and activate a virtual environment:** It's highly recommended to use a virtual environment to manage dependencies.

    ```
    python -m venv .venv
    source .venv/bin/activate  # On Linux/macOS
    # .venv\Scripts\activate   # On Windows

    ```

3.  **Install the Google ADK:** The ADK is typically installed via pip.

    ```
    pip install google-adk

    ```

    *Note: The ADK often includes necessary Google Cloud client libraries. If you encounter issues, you might need to manually install `google-cloud-aiplatform` or other relevant libraries for specific tools.*

