
release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: python project-name/manage.py runserver 0.0.0.0:$PORT
web: gunicorn contactapi.wsgi
