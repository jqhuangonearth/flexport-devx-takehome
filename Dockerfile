# syntax=docker/dockerfile:1

FROM python:3.9

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

CMD flask --app src/rock_paper_scissors/app.py run -h 0.0.0.0 -p 5000