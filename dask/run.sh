
docker-compose up -d --build

echo "**** Parallel jobs ****"

python dask_example.py

docker-compose down

echo "**** Serial jobs ****"

python what_example.py
