Running the RAG Agent with Vertex AI Search
=================================================

This guide provides instructions for setting up and executing the Retrieval Augmented Generation (RAG) agent via the Google Agent Development Kit (ADK) web interface. This agent specifically leverages a Vertex AI Search Data Store as its knowledge base to answer questions.

Table of Contents
-----------------

-   [Overview](#overview "null")

-   [Prerequisites](#prerequisites "null")

-   [Setting up Vertex AI Search Data Store](#setting-up-vertex-ai-search-data-store "null")

-   [Google Cloud Authentication and API Enables](#google-cloud-authentication-and-api-enables "null")

-   [Agent Configuration (.env and agent.py)](#agent-configuration-env-and-agentpy "null")

-   [Execution Steps](#execution-steps "null")

Overview
--------

The `agent.py` file defines an agent that acts as a "helpful assistant" capable of answering questions. Crucially, it is instructed to *only* use the `VertexAiSearchTool` to retrieve information from a specified knowledge base. If information isn't found, it will respond with "I'm sorry, I couldn't find that information in the knowledge base." This ensures the agent's responses are grounded in your provided data.

Prerequisites
-------------

Before proceeding, ensure you have:

-   **Google Cloud Project:** An active Google Cloud project with [billing enabled](https://cloud.google.com/billing/docs/how-to/enable-billing "null").

-   **Google Cloud SDK (gcloud CLI):** Installed and configured on your local machine. Follow the official installation guide [here](https://cloud.google.com/sdk/docs/install "null").

Setting up Vertex AI Search Data Store
--------------------------------------

The RAG agent requires a Vertex AI Search Data Store to function as its knowledge base. Follow these steps to create one:

1.  **Go to Vertex AI Search in Google Cloud Console:** Open your web browser and navigate to: <https://console.cloud.google.com/vertex-ai/search>

2.  **Create a new Data Store:**

    -   Click on the **"Create data store"** button.

    -   **Choose a Type:** Select **"Unstructured"**. This allows you to upload various document types.

    -   **Name your Data Store:** Provide a descriptive name, e.g., `my-rag-datastore` or `my-project-knowledge-base`.

    -   **Select a Region:** Choose a region that is geographically close to you or your users. Make a note of this region, as you'll need it for your `.env` configuration.

    -   **Upload your Content:** Upload PDFs, TXT files, Markdown files, or link websites that contain the information you want your agent to answer questions about.

    -   **Indexing:** After uploading, Vertex AI will begin indexing the content. This process can take a few minutes, depending on the amount of data. Ensure indexing is complete before trying to use the agent.

Google Cloud Authentication and API Enables
-------------------------------------------

Your local environment needs to be authenticated with Google Cloud, and specific APIs must be enabled for the ADK and Vertex AI Search to work correctly.

1.  **Authenticate Application Default Credentials:** This command authenticates your local Google Cloud SDK and sets up credentials that your applications (like the ADK agent) can use.

    ```
    gcloud auth application-default login

    ```

    Follow the prompts in your browser to complete the authentication.

2.  **Enable Required Google Cloud APIs:** Ensure that the Vertex AI Platform and Discovery Engine APIs are enabled in your Google Cloud project. These are essential for the `VertexAiSearchTool` to function.

    ```
    gcloud services enable aiplatform.googleapis.com discoveryengine.googleapis.com

    ```

    This command might take a moment to complete.

Agent Configuration (.env and agent.py)
---------------------------------------

You need to configure both your environment variables and the `agent.py` file to point to your specific Vertex AI Search Data Store.

1.  **Navigate to the `rag_agent` directory:** Open your terminal and change to the agent's directory:

    ```
    cd google-adk-agents/3-rag-agent/rag_agent

    ```

2.  **Prepare your environment file:** Copy the example environment file:

    ```
    cp .env.example .env

    ```

3.  **Update `.env` with API Key and Vertex AI Flag:** Open the newly created `.env` file in a text editor.

    -   **`GOOGLE_API_KEY`**: Replace `YOUR_API_KEY_HERE` with your actual Google API Key.

    -   **`GOOGLE_GENAI_USE_VERTEXAI=TRUE`**: This critical setting tells the ADK to route Gemini model calls through Vertex AI, which is required when using Vertex AI services.

    Your `.env` file should look similar to this:

    ```
    # .env file content
    GOOGLE_API_KEY=AIzaSyAs60xh1XjJzYPBEdgAHb_stB_oVqKWxTw # Replace with your key
    GOOGLE_GENAI_USE_VERTEXAI=TRUE

    ```

    *Ensure you save the changes to the `.env` file.*

4.  **Update `agent.py` with your Data Store ID:** Open the `agent.py` file in a text editor. Locate the `VertexAiSearchTool` definition within the `root_agent`'s `tools` list.

    You will see a line similar to this:

    ```
    # ...
    tools=[
        VertexAiSearchTool(
            data_store_id="projects/vertex-chatbot-433322/locations/us/collections/default_collection/dataStores/technova-datastore_1749516757306"
        )
    ],
    # ...

    ```

    **Replace the placeholder `data_store_id` value with the full resource path of the Data Store you created in the "Setting up Vertex AI Search Data Store" section.**

    The format for the `data_store_id` is always: `projects/<PROJECT-ID>/locations/<LOCATION>/collections/default_collection/dataStores/<DATASTORE-ID>`

    -   `<PROJECT-ID>`: Your Google Cloud Project ID.

    -   `<LOCATION>`: The region where you created your data store (e.g., `us-central1`, `us`).

    -   `<DATASTORE-ID>`: The specific ID of your data store. You can find this on the data store details page in the Vertex AI Search console.

    For example, if your project ID is `my-gcp-project`, your location is `us-central1`, and your data store ID is `my-rag-datastore`, the line would become:

    ```
    # ...
    tools=[
        VertexAiSearchTool(
            data_store_id="projects/my-gcp-project/locations/us-central1/collections/default_collection/dataStores/my-rag-datastore"
        )
    ],
    # ...

    ```

    *Save the changes to `agent.py`.*

Execution Steps
---------------

After completing all the setup and configuration steps, you are ready to run the RAG agent via the ADK web interface.

1.  **Ensure you are in the `rag_agent` directory:**

    ```
    cd google-adk-agents/3-rag-agent/

    ```

2.  **Launch the ADK web interface:** Execute the `adk web` command:

    ```
    adk web

    ```

3.  **Interact in your browser:** A browser window should automatically open (or you'll get a URL, typically `http://localhost:8000`). You can now interact with your **RAG agent**, asking it questions related to the content you uploaded to your Vertex AI Search Data Store.
