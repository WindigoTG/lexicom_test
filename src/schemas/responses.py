from pydantic import BaseModel


class NotFoundResponseSchema(BaseModel):
    error: str
