FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt-get update && apt-get -y install gcc

COPY ./requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000

COPY . .
WORKDIR .

CMD alembic upgrade head && \
    uvicorn app.main:app --host=0.0.0.0 --port=8000 --reload --workers=2


