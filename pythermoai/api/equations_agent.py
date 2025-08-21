# import libs
import logging
import asyncio
import threading
from fastapi import HTTPException, APIRouter, Request
from fastapi.responses import JSONResponse
# local

# NOTE: logger
logger = logging.getLogger(__name__)
# set logging level
logger.setLevel(logging.INFO)

# SECTION: api router
config_router = APIRouter(prefix="/equations-agent")


# SECTION: routes
@config_router.post("/create")
async def create_equations_agent(request: Request):
    """
    Create and initialize the equations agent.
    """
    app = request.app
    if not hasattr(app.state, "agents"):
        app.state.agents = {}

    try:
        from pythermoai.agents import create_agent
        agent = await create_agent(
            model_provider="openai",  # default values
            model_name="gpt-3.5-turbo",
            agent_name="equations_agent",
            agent_prompt="You are a helpful assistant for solving equations.",
            memory_mode=True
        )
        app.state.agents["equations_agent"] = agent
        return JSONResponse(
            content={
                "message": "Equations agent created successfully.",
                "success": True
            },
            status_code=200
        )
    except Exception as e:
        logger.error(f"Error creating equations agent: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to create equations agent: {e}"
        )


@config_router.get("/config")
async def get_equations_agent_config(request: Request):
    """
    Get the configuration of the equations agent.
    """
    app = request.app
    if "equations_agent" not in app.state.agents:
        raise HTTPException(
            status_code=404, detail="Equations agent not found."
        )

    agent = app.state.agents["equations_agent"]
    config = {
        "model_provider": agent.model_provider,
        "model_name": agent.model_name,
        "agent_name": agent.agent_name,
        "agent_prompt": agent.agent_prompt,
        "memory_mode": agent.memory_mode
    }
    return JSONResponse(content=config)


@config_router.post("/config")
async def set_equations_agent_config(request: Request, config: dict):
    """
    Set the configuration of the equations agent.
    """
    app = request.app
    if "equations_agent" not in app.state.agents:
        raise HTTPException(
            status_code=404, detail="Equations agent not found."
        )

    try:
        from pythermoai.agents import create_agent
        agent = await create_agent(**config)
        app.state.agents["equations_agent"] = agent
        return JSONResponse(
            content={
                "message": "Equations agent configured successfully.",
                "success": True
            },
            status_code=200
        )
    except Exception as e:
        logger.error(f"Error configuring equations agent: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to configure equations agent: {e}"
        )
