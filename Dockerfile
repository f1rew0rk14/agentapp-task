FROM python:3.9-slim

RUN apt update

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p networks_connector
COPY networks_connector /networks_connector
COPY run.py /
COPY .env /
WORKDIR /

CMD python3 run.py