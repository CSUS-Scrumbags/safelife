web: gunicorn safelife_project.wsgi:application --log-file - --log-level debug
web: python safelife/safelife/safelife_project/manage.py runserver 0.0.0.0:$PORT --noreload
python manage.py collectstatic --noinput
