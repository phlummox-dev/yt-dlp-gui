FROM python:3.13.3-bullseye

# general deps

RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
      sudo

COPY scripts/install-linux-deps.sh /tmp

RUN sh /tmp/install-linux-deps.sh

RUN mkdir /build

WORKDIR /build

COPY pyproject.toml /build

RUN uv sync --no-dev --no-install-project

