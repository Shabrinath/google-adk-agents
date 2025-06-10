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

Getting Your Google API Token and Environment Setup
---------------------------------------------------

To interact with Google's AI models and services, you'll need to authenticate.

1.  **Create a `.env` file:** In the root of your project directory, create a file named `.env` and add the following:

    ```
    GOOGLE_API_KEY=Axxxxxxxxxxxxxxxxxxxxw
    GOOGLE_GENAI_USE_VERTEXAI=FALSE  

    ```

    -   **`GOOGLE_API_KEY`**: Replace `Axxxxxxxxxxxxxxxxxxxxxxw` with your actual Google Cloud API key if you're using the Gemini API directly. You can obtain one from the [Google AI Studio](https://aistudio.google.com/app/apikey "null").

    -   **`GOOGLE_GENAI_USE_VERTEXAI`**: This tells the ADK to route Gemini model calls through Vertex AI, which is necessary when using Vertex AI services like Vertex AI Search. This should be TRUE when using RAG.

2.  **Google Cloud CLI Authentication (Essential for RAG Agent with Vertex AI Search):** For the RAG agent using Vertex AI Search, you need to authenticate your local environment with Google Cloud.

    -   **Install the Google Cloud CLI:** Follow the official instructions [here](https://cloud.google.com/sdk/docs/install "null").

    -   **Authenticate your application default credentials:**

        ```
        gcloud auth application-default login

        ```

        This command opens a browser window to complete the authentication process.

    -   **Enable necessary Google Cloud APIs:** Ensure the AI Platform and Discovery Engine APIs are enabled in your Google Cloud project.

        ```
        gcloud services enable aiplatform.googleapis.com discoveryengine.googleapis.com

        ```

    -   **Update `data_store_id` (if using your own data store):** In `agent.py`, update the `data_store_id` if you are not using the provided one:

        ```
        # ...
        tools=[
            VertexAiSearchTool(
                data_store_id="projects/YOUR_PROJECT_ID/locations/YOUR_LOCATION/collections/YOUR_COLLECTION_ID/dataStores/YOUR_DATASTORE_ID"
            )
        ],
        # ...

        ```

        For example, if your data store is in `us-central1` and named `my-new-datastore`, it might look like: `projects/vertex-chatbot-433322/locations/us-central1/collections/default_collection/dataStores/technova-datastore_1749516757306`
