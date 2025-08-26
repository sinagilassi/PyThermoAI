# PyThermoAI

[![PyPI Downloads](https://static.pepy.tech/badge/pythermoai/month)](https://pepy.tech/projects/pythermoai)
![PyPI Version](https://img.shields.io/pypi/v/pythermoai)
![Supported Python Versions](https://img.shields.io/pypi/pyversions/pythermoai.svg)
![License](https://img.shields.io/pypi/l/pythermoai)

## 🚀 Introduction

**PyThermoAI** is an intelligent Python package that revolutionizes thermodynamic data acquisition and processing by leveraging advanced AI agents and web search capabilities. This powerful tool seamlessly integrates thermodynamic data retrieval, equation solving, and database management into a unified platform.

![PyThermoAI Architecture](https://drive.google.com/uc?export=view&id=1osFnvr4dl0iLtnHhdhr_5EWLK0QGGabh)

### Key Features

- 🤖 **AI-Powered Data Agents**: Intelligent agents that automatically search and retrieve thermodynamic properties from authoritative sources (NIST, DIPPR, peer-reviewed literature)
- 💾 **Database Integration**: Direct connection with PyThermoDB for data storage and management, with automatic conversion of retrieved thermodynamic data into the valid PyThermoDB format

### Architecture Overview

PyThermoAI consists of several interconnected components:

- **Data Agent**: Searches and validates thermodynamic properties
- **Equations Agent**: Solves complex thermodynamic equations
- **MCP Manager**: Handles Model Context Protocol integrations allows using multiple MCP servers for enhanced functionality

## 📦 Installation

Install PyThermoAI using pip:

```bash
pip install pythermoai
```

### Requirements

- Python 3.13+
- API keys for LLM providers (OpenAI, Anthropic, Google, etc.)
- Tavily API key for enhanced web search capabilities

## 🛠️ Quick Start

### 1. Launch the Web Interface

```python
from pythermoai import thermo_chat

# mcp source configuration
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

# Launch with OpenAI GPT-4
thermo_chat(
    model_provider="openai",
    model_name="gpt-4o-mini",
    mcp_source=mcp_source,
)
```

### 2. Create an AI Agent

```python
import asyncio
from pythermoai.agents import create_agent
from pythermoai.memory import generate_thread

async def main():
    # Create a thermodynamic data agent
    agent = await create_agent(
        model_provider="openai",
        model_name="gpt-4o-mini",
        agent_name="data-agent",
        agent_prompt="You are a thermodynamic data expert...",
        mcp_source=mcp_source
    )

    # Generate conversation thread
    config = generate_thread()

    # Query for thermodynamic properties
    result = await agent.ainvoke({
        "messages": ["Find critical properties for methane"]
    }, config=config)

    print(result)

asyncio.run(main())
```

### 3. Create a FastAPI Service

```python
from pythermoai.api import create_api
import uvicorn

# Create API with integrated agents
app = create_api(
    model_provider="openai",
    model_name="gpt-4o-mini",
    mcp_source=mcp_source
)

# Run the server
uvicorn.run(app, host="127.0.0.1", port=8000)
```

## 📋 Examples

### Retrieve Thermodynamic Properties

```python
# Request critical properties for multiple compounds
query = """
Find the following properties for methane, ethane, and propane:
- Critical Temperature (K)
- Critical Pressure (MPa)
- Critical Volume (m³/mol)
- Molecular Weight (g/mol)
"""

# The agent will automatically search, validate, and format the data
# Output will be structured in YAML format for easy integration
```

### Convert Data to PyThermoDB Format

```python
query = """
These are thermodynamic data for Methane

Experimental data for CH4 (Methane)
22 02 02 11 45
Other names
Biogas; Fire damp; Marsh gas; Methane; Methyl hydride; R 50;
INChI	INChIKey	SMILES	IUPAC name
InChI=1S/CH4/h1H4	VNWKTOKETHGBQD-UHFFFAOYSA-N	C	Methane
State	Conformation
1A1	TD
Enthalpy of formation (Hfg), Entropy, Integrated heat capacity (0 K to 298.15 K) (HH), Heat Capacity (Cp)
Property	Value	Uncertainty	units	Reference	Comment
Hfg(298.15K) enthalpy of formation	-74.60	0.30	kJ mol-1	Gurvich
Hfg(0K) enthalpy of formation	-66.63	0.30	kJ mol-1	Gurvich
Entropy (298.15K) entropy	186.37	 	J K-1 mol-1	Gurvich
Integrated Heat Capacity (0 to 298.15K) integrated heat capacity	10.02	 	kJ mol-1	Gurvich
Heat Capacity (298.15K) heat capacity	35.69	 	J K-1 mol-1	Gurvich

Give me the yaml formatted data for PyThermoDB
"""

# Automated retrieval and validation from multiple sources
```

## 🔧 Advanced Configuration

### MCP Server Integration

```python
# Configure multiple MCP servers for enhanced functionality
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
    },
    "custom-mcp": {
        "command": "path/to/custom/mcp-server",
        "args": ["--option", "value"],
        "transport": "stdio",
        "env": {}
    }
}

```

### Custom Agent Prompts

```python
from pythermoai.agents import DATA_AGENT_PROMPT, EQUATIONS_AGENT_PROMPT

# Customize agent behavior with specialized prompts
custom_prompt = """
You are a specialized petrochemical data expert.
Focus on hydrocarbon properties and refinery applications.
Always include uncertainty estimates and data sources.
"""
```

## 📚 API Reference

### Core Functions

- `thermo_chat()`: Launch the complete web application
- `create_agent()`: Create specialized AI agents
- `create_api()`: Generate FastAPI application
- `generate_thread()`: Create conversation memory threads

### Supported Models

- **OpenAI**: GPT-4, GPT-4o, GPT-4o-mini
- **Anthropic**: Claude 3.5 Sonnet
- **Google**: Gemini Pro
- **X.AI**: Grok models

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request to improve the project.

## 📝 License

This project is licensed under the Apache License 2.0. You are free to use, modify, and distribute this software in your own applications or projects, provided that you comply with the terms of the Apache License. This includes providing proper attribution, including a copy of the license, and indicating any changes made to the original code. For more details, please refer to the [LICENSE](./LICENSE) file.

## ❓ FAQ

For any questions, contact me on [LinkedIn](https://www.linkedin.com/in/sina-gilassi/).

## 👨‍💻 Authors

- [@sinagilassi](https://www.github.com/sinagilassi)

---

⭐ **Star this repository** if you find it useful for your chemical engineering projects!

🐛 **Report issues** or 💡 **suggest new features** in the [Issues](https://github.com/sinagilassi/pythermoai/issues) section.