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
config_router = APIRouter(prefix="equations-agent")

# SECTION: routes
