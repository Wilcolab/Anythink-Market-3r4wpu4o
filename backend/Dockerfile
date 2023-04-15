FROM python:3.10.6-slim-buster


ARG WORKDIR=/usr/src/backend
WORKDIR ${WORKDIR}

ENV \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PYTHONDONTWRITEBYTECODE=1 \
  # pip:
  PIP_NO_CACHE_DIR=1 \
  PIP_DISABLE_PIP_VERSION_CHECK=1 \
  PIP_DEFAULT_TIMEOUT=100 \
  # poetry:
  POETRY_VERSION=1.4.2 \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local'

RUN apt-get update && apt-get upgrade -y \
  && apt-get install --no-install-recommends -y \
    bash \
    brotli \
    build-essential \
    curl \
    gettext \
    git \
    libpq-dev \
    wait-for-it \
#   # Installing `tini` utility:
#   # https://github.com/krallin/tini
#   # Get architecture to download appropriate tini release:
#   # See https://github.com/wemake-services/wemake-django-template/issues/1725
#   && dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \
#   && curl -o /usr/local/bin/tini -sSLO "https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-${dpkgArch}" \
#   && chmod +x /usr/local/bin/tini && tini --version \
  # Installing `poetry` package manager:
  # https://github.com/python-poetry/poetry
  && curl -sSL 'https://install.python-poetry.org' | python - \
  && poetry --version \
  # Cleaning cache:
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Pre-install poetry packages

COPY backend/ ${WORKDIR}
RUN poetry install
# RUN wait-for-it postgres-python:5432 -q -t 60
RUN poetry run alembic upgrade head
RUN poetry run gunicorn app.main:app --worker-class=uvicorn.workers.UvicornWorker --bind=0.0.0.0:3000 --workers=5
