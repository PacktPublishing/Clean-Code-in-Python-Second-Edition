FROM python:3.9-slim-buster

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python-dev \
        gcc \
        musl-dev \
        make \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
ADD . /app

RUN pip install /app/libs/web /app/libs/storage
RUN pip install /app

EXPOSE 8080
CMD ["/usr/local/bin/status-service"]
