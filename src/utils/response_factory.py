from typing import Dict

from fastapi import status
from fastapi.responses import JSONResponse


def get_response(content: Dict, status_code: int = status.HTTP_200_OK):
    return JSONResponse(content=content, status_code=status_code)


def get_created_response(content: Dict):
    return get_response(content, status_code=status.HTTP_201_CREATED)


def get_not_found_response(message: str):
    return get_response(
        {"error": message},
        status_code=status.HTTP_404_NOT_FOUND,
    )
