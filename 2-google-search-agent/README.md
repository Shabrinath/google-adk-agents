Running the Google Search Agent
=====================================

This guide focuses on executing the `google_search_agent` via the ADK web interface, allowing for interaction in your browser. This agent leverages the `google_search` tool to provide real-time information.

Execution Steps
---------------

Follow these steps to get your Google Search agent running in a web interface:

1.  **Navigate to the `2-google-search-agent/google_search_agent` directory:** First, ensure you are in the correct directory within your cloned `google-adk-agents` repository.

    ```
    cd google-adk-agents/2-google-search-agent/google_search_agent

    ```

2.  **Prepare your environment file:** Copy the example environment file to create your own `.env` file. This file will store your API key securely.

    ```
    cp .env.example .env

    ```

3.  **Update your API key:** Open the newly created `.env` file in a text editor and replace `YOUR_API_KEY_HERE` with your actual **Google API Key**. This key is essential for authenticating with the `gemini-2.0-flash` model and enabling the `google_search` tool. You can obtain an API key from the [Google AI Studio website](https://aistudio.google.com/app/apikey "null").

    ```
    # .env file content
    GOOGLE_API_KEY=xxxxx # Replace with your key

    ```

    *Ensure you save the changes to the `.env` file.*

4.  **Launch the ADK web interface:** From the `2-google-search-agent/google_search_agent` directory, run the `adk web` command. This will start a local web server and launch the ADK interface for your agent.

    ```
    cd google-adk-agents/2-google-search-agent
    source adk/bin/activate #activate virtual environment if not activated already
    adk web

    ```

5.  **Interact in your browser:** After executing `adk web`, a browser window should automatically open (or you'll get a URL to open manually, typically `http://localhost:8000`). You can now interact with your **Google Search agent** directly within the web interface, asking it questions that might require real-time information.
