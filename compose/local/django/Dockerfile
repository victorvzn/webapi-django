FROM python:3.6

ENV PYTHONUNBUFFERED=1

RUN mkdir /src

WORKDIR /src

COPY ./requirements /requirements

RUN pip install -r /requirements/local.txt

COPY ./src /src/
