FROM phusion/baseimage:0.11

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PYTHON_VERSION 3.8

RUN set -x \
  && apt-get update \
  && apt-get install -y python${PYTHON_VERSION} \
  && apt-get install -y python3-pip  \
  && apt-get clean

COPY etl-pipeline/etl-code/run_step.py .
COPY etl-pipeline/etl-code/requirements.txt .
COPY model-pipeline/utils ./utils/


RUN python3 -m pip install -r requirements.txt

