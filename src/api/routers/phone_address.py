from fastapi import status
from fastapi import APIRouter, Query

from src.services.phone_address import PhoneAddressService
from src.schemas.phone_address import PhoneAddressSchema
from src.schemas.responses import NotFoundResponseSchema

router = APIRouter()


@router.get(
    "/check_data",
    response_model=PhoneAddressSchema,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": NotFoundResponseSchema}
    },
    status_code=status.HTTP_200_OK,
    summary="Get address data by phone number",
)
async def get_address(phone: str = Query(regex=r"^[7-8]\d{10}$")):
    """
    Get address data by phone number.

    Path params:
    - **phone**: The phone number for which you want to obtain
        an associated address.
    """
    result = await PhoneAddressService.get_address(phone)
    return result


@router.post(
    "/write_data",
    response_model=PhoneAddressSchema,
    status_code=status.HTTP_201_CREATED,
    summary="Store an address data associated with a phone number."
)
async def add_address(phone_address: PhoneAddressSchema):
    """
    Store an address data associated with a phone number.

    Body params:
    - **phone**: The phone number for which you want to store
        associated address.
    - **address**: The address you want to store.
    """
    result = await PhoneAddressService.add_address(phone_address)
    return result


@router.put(
    "/write_data",
    response_model=PhoneAddressSchema,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": NotFoundResponseSchema}
    },
    status_code=status.HTTP_200_OK,
    summary="Update the address data associated with a phone number."
)
async def update_address(phone_address: PhoneAddressSchema):
    """
        Update the address data associated with a phone number.

        Body params:
        - **phone**: The phone number for which you want to update
            associated address.
        - **address**: The address you want to store.
        """
    result = await PhoneAddressService.update_address(phone_address)
    return result
