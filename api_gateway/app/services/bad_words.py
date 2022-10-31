from fastapi import HTTPException
from starlette import status
from sqlalchemy import insert
from aiohttp.client_exceptions import ClientConnectionError
from loguru import logger

from app.services.base import BaseService
from app.models.base import BadWordsRequest, BasWordsResponse
from app.services.aio_client import ServiceClient
from app.core.settings import settings
from app.db.tables import BadWords


class BadWordsService(BaseService):

    async def handle(self, bad_words_request: BadWordsRequest) -> list[BasWordsResponse]:
        request_data = bad_words_request.dict()
        client = ServiceClient(settings.bad_words_service_url)
        try:
            response = await client.get_data_from_service(request_data)
        except ClientConnectionError as exc:
            logger.info(f'Client Error {exc}')
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cannot connect to BadWords service",
            )

        await self.insert_to_db(request_data, response)
        return [BasWordsResponse.parse_obj(r) for r in response]

    async def insert_to_db(self, request_data: dict[str: list],
                           response_data: list[dict[str, bool]]) -> None:
        stmt = insert(BadWords).values(
            request=request_data,
            response=response_data
        )
        await self.session.execute(stmt)
