FROM python:3.9-alpine3.13
LABEL maintainer="github.com/STRYKER316"

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /pyenv && \
    /pyenv/bin/pip install --upgrade pip && \
    /pyenv/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /pyenv/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-app-user

ENV PATH="/pyenv/bin:$PATH"

USER django-app-user
