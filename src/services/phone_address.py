from fastapi.responses import JSONResponse

from src.services.redis import cache
from src.schemas.phone_address import PhoneAddressSchema
from src.utils import response_factory


class PhoneAddressService:
    _not_found_message = "Address for this phone not found."

    @staticmethod
    async def add_address(phone_address: PhoneAddressSchema) -> JSONResponse:
        cache.set(phone_address.phone, phone_address.address)
        return response_factory.get_created_response(
            content=phone_address.model_dump()
        )

    @staticmethod
    async def get_address(phone: str) -> JSONResponse:
        address = cache.get(phone)

        if not address:
            return response_factory.get_not_found_response(
                message=PhoneAddressService._not_found_message
            )

        return response_factory.get_response(
            content=PhoneAddressSchema(
                phone=phone,
                address=address,
            ).model_dump()
        )

    @staticmethod
    async def update_address(
        phone_address: PhoneAddressSchema,
    ) -> JSONResponse:
        result = cache.set(phone_address.phone, phone_address.address, xx=True)

        if not result:
            return response_factory.get_not_found_response(
                message=PhoneAddressService._not_found_message
            )

        return response_factory.get_response(
            content=phone_address.model_dump()
        )
