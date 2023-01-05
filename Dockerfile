# syntax=docker/dockerfile:1
FROM ubuntu:22.04
FROM python:3.10-slim-buster

# install app dependencies
RUN apt-get update && apt-get install -y  python3-pip


# install app
COPY app.py /
COPY requirements.txt /
COPY bestModelUSELogistic.pkl /
COPY dicoPassageTagToList.pickle /
COPY function.py /
COPY labels.pkl /
COPY StopWord.pickle /
COPY templates/* templates/

# install app dependencies
RUN pip install --no-cache-dir -r requirements.txt

# final configuration
ENV FLASK_APP=app
EXPOSE 5000
CMD flask run --host 0.0.0.0 --port 5000
