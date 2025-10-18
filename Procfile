web: gunicorn sitebus.wsgi:application
release: python manage.py migrate && python manage.py collectstatic --noinput && python manage.py createsu
