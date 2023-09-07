FROM python:3.11-slim-bullseye

ENV PYTHONPATH /app/src/
ENV PATH /app/src/:$PATH
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.6

ARG UID=1000
ARG GID=1000
ENV UID=${UID}
ENV GID=${GID}

RUN groupadd --gid $GID node && useradd --uid $UID --gid node --shell /bin/bash --create-home node

# change workdir
WORKDIR /app

# install poetry
RUN pip3 install --no-cache-dir "poetry==$POETRY_VERSION"
RUN poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock /app/

RUN poetry install --without dev

COPY . /app

EXPOSE 9000
ENTRYPOINT []

USER node
CMD ["gunicorn", "-b", "0.0.0.0:9000", "-k", "uvicorn.workers.UvicornWorker", "-w", "4", "--log-level", "warning", "--reuse-port", "pokemon.asgi:app"]
