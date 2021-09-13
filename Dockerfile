FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update \
    && apt-get install -y jq curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install rq \
    && pip install supervisor 

COPY . .
CMD [ "python3", "app.py"]