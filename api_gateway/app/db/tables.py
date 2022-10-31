import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.functions import func

Base = declarative_base()


class BadWords(Base):
    __tablename__ = "badlisted_words"

    id = sa.Column(sa.Integer, primary_key=True)
    request = sa.Column(sa.JSON)
    response = sa.Column(sa.JSON)
    created_at = sa.Column(sa.DateTime(timezone=True), server_default=func.now())
