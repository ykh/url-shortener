FROM python:3.12-slim as locust-base

ENV POETRY_VERSION=1.8.2

FROM locust-base as locust-dependencies

WORKDIR /src

COPY ./pyproject.toml .
COPY ./poetry.lock .

COPY ./scripts ./scripts

RUN set -e

RUN pip install "poetry==$POETRY_VERSION"
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-root --no-ansi


FROM locust-dependencies as locust-master

CMD sh /src/scripts/run_master.sh

FROM locust-dependencies as locust-worker

CMD sh /src/scripts/run_worker.sh
