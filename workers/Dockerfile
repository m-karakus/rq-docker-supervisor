FROM python:3

# FROM python:3.8-slim-buster

RUN apt-get update \
    && apt-get install -y jq curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install rq \
    && pip install supervisor 

# Spawn workers according to config
# ENTRYPOINT ["/bin/bash", "-c", "supervisord -c /usr/src/workers/supervisord.conf -n"]

COPY . .
CMD [ "python3", "/usr/src/workers/app.py"]