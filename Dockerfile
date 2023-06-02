FROM python:3.7.11-slim

EXPOSE 8000
WORKDIR /sc-worker


RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY requirements.txt ./
RUN pip install -r requirements.txt

ADD . /sc-worker

ENTRYPOINT ./entrypoint.sh
