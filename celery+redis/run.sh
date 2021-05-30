
docker-compose up -d --build

echo "**** Parallel jobs ****"

python celery_example.py

docker-compose down

echo "**** Serial jobs ****"

python what_example.py
