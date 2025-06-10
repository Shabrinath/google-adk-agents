Running the Basic Greeting Agent
======================================

This guide focuses on executing the `greeting_agent` via the ADK web interface, allowing for interaction in your browser.

Execution Steps
---------------

Follow these steps to get your basic greeting agent running in a web interface:

1.  **Navigate to the `1-basic-agent` directory:** First, ensure you are in the correct directory. If you just cloned the `google-adk-agents` repository, you'll need to change directories.

    ```
    cd google-adk-agents/1-basic-agent

    ```

2.  **Prepare your environment file:** Copy the example environment file to create your own `.env` file. This file will store your API key securely.

    ```
    cp .env.example .env

    ```

3.  **Update your API key:** Open the newly created `.env` file in a text editor and replace `YOUR_API_KEY_HERE` with your actual **Google API Key**. You can obtain an API key from the [Google AI Studio website](https://aistudio.google.com/app/apikey "null").

    ```
    # .env file content
    GOOGLE_API_KEY=xxxxx # Replace with your key

    ```

    *Ensure you save the changes to the `.env` file.*

4.  **Launch the ADK web interface:** From the `1-basic-agent` directory, run the `adk web` command. This will start a local web server and launch the ADK interface for your agent.

    ```
    cd google-adk-agents/1-basic-agent
    source adk/bin/activate 
    adk web

    ```

5.  **Interact in your browser:** After executing `adk web`, a browser window should automatically open (or you'll get a URL to open manually, typically `http://localhost:8000`). You can now interact with your **greeting agent** directly within the web interface.
