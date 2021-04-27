FROM ubuntu:20.04

RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential

WORKDIR /app

ENV FLASK_APP=app.py

COPY config config
COPY models models
COPY resources resources
COPY rosie rosie
COPY serializers serializers

COPY requirements.txt .
COPY app.py .
COPY uwsgi.ini .

RUN pip3 install -r requirements.txt

RUN flask db init
RUN flask db migrate -m "Initial migration."
RUN flask db upgrade
RUN chown -R www-data:www-data /app

CMD ["uwsgi", "--ini", "uwsgi.ini"]
