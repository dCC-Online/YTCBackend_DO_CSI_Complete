set -e  # exit if errors happen anywhere
python ./drf_jwt_backend/manage.py migrate

python ./drf_jwt_backend/manage.py runserver 0.0.0.0:8000