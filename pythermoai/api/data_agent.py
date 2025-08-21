# import libs
import logging
from fastapi import HTTPException, APIRouter, Request
from fastapi.responses import JSONResponse
# local
from ..agents import create_agent, DATA_AGENT_NAME, DATA_AGENT_PROMPT

# NOTE: logger
logger = logging.getLogger(__name__)
# set logging level
logger.setLevel(logging.INFO)

# SECTION: api router
config_router = APIRouter(prefix="/data-agent")


# SECTION: routes
@config_router.post("/create")
async def create_data_agent(request: Request):
    """
    Create and initialize the data agent.
    """
    app = request.app
    if not hasattr(app.state, "agents"):
        app.state.agents = {}

    # SECTION: extract data from app state
    model_provider, model_name, memory_mode = (
        app.state.model_provider,
        app.state.model_name,
        app.state.memory_mode
    )

    try:
        # create the agent
        agent = await create_agent(
            model_provider=model_provider,  # default values
            model_name=model_name,
            agent_name="data_agent",
            agent_prompt="You are a helpful assistant for data-related tasks.",
            memory_mode=memory_mode
        )
        app.state.agents["data_agent"] = agent
        return JSONResponse(
            content={
                "message": "Data agent created successfully.",
                "success": True
            },
            status_code=200
        )
    except Exception as e:
        logger.error(f"Error creating data agent: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to create data agent: {e}"
        )


@config_router.get("/config")
async def get_data_agent_config(request: Request):
    """
    Get the configuration of the data agent.
    """
    app = request.app
    if "data_agent" not in app.state.agents:
        raise HTTPException(status_code=404, detail="Data agent not found.")

    agent = app.state.agents["data_agent"]
    config = {
        "model_provider": agent.model_provider,
        "model_name": agent.model_name,
        "agent_name": agent.agent_name,
        "agent_prompt": agent.agent_prompt,
        "memory_mode": agent.memory_mode
    }
    return JSONResponse(content=config)


@config_router.post("/config")
async def set_data_agent_config(request: Request, config: dict):
    """
    Set the configuration of the data agent.
    """
    app = request.app
    if "data_agent" not in app.state.agents:
        raise HTTPException(status_code=404, detail="Data agent not found.")

    try:
        from pythermoai.agents import create_agent
        agent = await create_agent(**config)
        app.state.agents["data_agent"] = agent
        return JSONResponse(
            content={
                "message": "Data agent configured successfully.",
                "success": True
            },
            status_code=200
        )
    except Exception as e:
        logger.error(f"Error configuring data agent: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to configure data agent: {e}"
        )
