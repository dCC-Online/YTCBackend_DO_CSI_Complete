set -e  # exit if errors happen anywhere

# Setup environment variables for Super User (will extract to be hidden later)
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=password1561
export DJANGO_SUPERUSER_EMAIL=nomail@email.com

# The next steps must be executed in the order they are listed here.

python ./drf_jwt_backend/manage.py migrate

python ./drf_jwt_backend/manage.py createsuperuser --noinput

python ./drf_jwt_backend/manage.py runserver 0.0.0.0:8000