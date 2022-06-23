FROM python:3.7-alpine as base

ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt ./

RUN apk add --update --no-cache --virtual .build-deps \
    build-base \
    postgresql-dev \
    libffi-dev \
    python3-dev \
    libffi-dev \
    jpeg-dev \
    zlib-dev \
    binutils \
    musl-dev \
    libpq \
    && pip install --no-cache-dir -r requirements.txt


FROM python:3.7-alpine

RUN apk add --update --no-cache \
    libpq \
    binutils \
    libc-dev \
    libjpeg-turbo

COPY --from=base /usr/local/lib/python3.7/site-packages/ /usr/local/lib/python3.7/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/

WORKDIR /code

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /code:$PYTHONPATH

EXPOSE 8000

COPY ./src /code/src
COPY ./static /code/static
COPY ./.env /code/.env

COPY ./entrypoint.sh /code
ENTRYPOINT ["./entrypoint.sh"]
