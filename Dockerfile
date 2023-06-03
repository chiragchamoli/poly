FROM python:3.9.13-slim

EXPOSE 8000
WORKDIR /polly


RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat && \
    apt-get -y install libpq-dev gcc && \
    pip install psycopg2 && \
    pip install scikit-learn && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY requirements.txt ./
RUN pip install -r requirements.txt
ADD . /polly

ENTRYPOINT ./entrypoint.sh
