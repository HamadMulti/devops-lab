FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY pipmanager/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY pipmanager/* .

RUN pip install --no-cache-dir .

ENV PYTHONUNBUFFERED=1

CMD ["pipmanager", "--help"]
