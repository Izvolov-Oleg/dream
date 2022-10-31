from fastapi import APIRouter, Depends

from app.services.bad_words import BadWordsService
from app.models.base import (
    BadWordsRequest,
    BasWordsResponse,
)

router = APIRouter()


@router.post('/badlisted_words', response_model=list[BasWordsResponse])
async def bad_listed(
        bad_words_request: BadWordsRequest,
        service: BadWordsService = Depends()
):
    return await service.handle(bad_words_request)
