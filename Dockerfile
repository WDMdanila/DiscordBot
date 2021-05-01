FROM python:3.9.4-buster

RUN apt-get update && apt-get install ffmpeg -y

WORKDIR /bot
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /bot
CMD python3 -m discord_bot