FROM python:3.9-buster
WORKDIR /app

# container maintenance
RUN apt update && apt upgrade -y

# starting django
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput
#RUN python manage.py migrate