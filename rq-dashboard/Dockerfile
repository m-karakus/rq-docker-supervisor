FROM python:3.8-slim-buster

# Install Python dependencies
RUN pip install rq-dashboard \
    && pip install --upgrade --force-reinstall click==7.1.2

ENTRYPOINT ["/bin/bash", "-c", "rq-dashboard -H redis"]