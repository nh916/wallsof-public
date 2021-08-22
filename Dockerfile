FROM python:3.9-buster
WORKDIR /app

RUN apt update && apt upgrade -y


COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput
# RUN python manage.py migrate