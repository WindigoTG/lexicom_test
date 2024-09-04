from pydantic import BaseModel, Field


class PhoneAddressSchema(BaseModel):
    phone: str = Field(pattern=r"^[7-8]\d{10}$")
    address: str
