from fastapi import APIRouter, HTTPException
from structlog import get_logger

from pokemon.core.mongodb import get_client

logger = get_logger(__name__)

router = APIRouter()
