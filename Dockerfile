FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r pipmanager/requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]