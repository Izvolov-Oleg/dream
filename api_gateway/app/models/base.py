from pydantic import BaseModel


class BadWordsRequest(BaseModel):
    sentences: list[str]


class BasWordsResponse(BaseModel):
    bad_words: bool
