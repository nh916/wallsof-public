python manage.py collectstatic --no-input
python manage.py migrate --no-input

python manage.py runserver 0.0.0.0:8000

# gunicorn wall.wsgi:application --bind 0.0.0.0:8000