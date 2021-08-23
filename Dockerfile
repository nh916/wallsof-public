FROM python:3.9-buster

WORKDIR /app

RUN apt update && apt upgrade -y
RUN pip install -U pip


COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

COPY ./django-enterypoint.sh /app/

ENTRYPOINT [ "sh", "django-enterypoint.sh" ]