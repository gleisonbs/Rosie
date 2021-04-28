FROM python:3.9.2-slim

ENV FLASK_APP=app.py
WORKDIR /app

RUN apt-get clean \
  && apt-get -y update

RUN apt-get -y install nginx \
  && apt-get -y install python3-dev \
  && apt-get -y install build-essential

COPY requirements.txt .
RUN pip3 install -r requirements.txt --src /usr/local/src

COPY config config
COPY models models
COPY resources resources
COPY rosie rosie
COPY serializers serializers

COPY app.py .
COPY uwsgi.ini .
COPY nginx.conf /etc/nginx
COPY start.sh .

RUN flask db init
RUN flask db migrate -m "Initial migration."
RUN flask db upgrade
RUN chown -R www-data:www-data /app

RUN chmod +x ./start.sh
CMD ["./start.sh"]
