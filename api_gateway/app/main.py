from fastapi import FastAPI

from app.core.settings import settings
from app.api.routes import router as bad_words_router


def get_application() -> FastAPI:

    settings.configure_logging()

    application = FastAPI(**settings.fastapi_kwargs)

    application.include_router(bad_words_router, prefix=settings.api_prefix)
    return application


app = get_application()
