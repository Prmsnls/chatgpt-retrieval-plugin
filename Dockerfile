
FROM python:3.10.6-slim

# Allow statements and log messages to immediately appear in the Cloud Run logs
ENV PYTHONUNBUFFERED 1
ENV wd=/home/app/

# Create and change to the app directory.
WORKDIR ${wd}

# Copy application dependency manifests to the container image.
# Copying this separately prevents re-running pip install on every code change.
COPY ./requirements.txt .

# Install dependencies.
RUN pip install -r requirements.txt

COPY . .


CMD  uvicorn main:app --port 8000 --host 0.0.0.0 --reload --limit-concurrency 100


