# import libs
import uvicorn
import asyncio
import os
import logging
# python dot env
from dotenv import load_dotenv
# local
from pythermoai.api import create_api

# NOTE: logger
logger = logging.getLogger(__name__)

# SECTION: load environment variables
load_dotenv()

# langchain
env_val = os.getenv('LANGCHAIN_API_KEY')
if env_val is not None:
    os.environ['LANGCHAIN_API_KEY'] = env_val
env_val = os.getenv('LANGCHAIN_TRACING_V2')
if env_val is not None:
    os.environ['LANGCHAIN_TRACING_V2'] = env_val

# open ai
env_val = os.getenv('OPENAI_API_KEY')
if env_val is not None:
    os.environ['OPENAI_API_KEY'] = env_val
# tavily
env_val = os.getenv('TAVILY_API_KEY')
if env_val is not None:
    os.environ['TAVILY_API_KEY'] = env_val

# SECTION: inputs
# NOTE: model provider
model_provider = "openai"
# NOTE: model name
model_name = "gpt-4o-mini"

# NOTE: mcp source
# tavily remote mcp
mcp_source = {
    "tavily-remote": {
        "command": "npx",
        "args": [
            "-y",
            "mcp-remote",
            f"https://mcp.tavily.com/mcp/?tavilyApiKey={os.getenv('TAVILY_API_KEY')}"
        ],
        "transport": "stdio",
        "env": {}
    }
}

mcp_source = None

# NOTE: agent prompt
agent_prompt = """You are a helpful assistant that can perform various tasks using tools provided by the EOS Models and Flash Calculations MCP servers.
You can use tools to perform calculations, retrieve data, and assist with various tasks.
Based on the results from the tools, you will provide a final answer to the user.
"""


# SECTION: Run the FastAPI application
if __name__ == "__main__":
    app_instance = asyncio.run(create_api(
        model_provider=model_provider,
        model_name=model_name,
        agent_name="Data-Agent",
        agent_prompt=agent_prompt,
        mcp_source=mcp_source,
        memory_mode=True
    ))
    # Run the FastAPI app with Uvicorn
    uvicorn.run(
        app_instance,
        host="127.0.0.1",
        port=8001,
        log_level="info"
    )
