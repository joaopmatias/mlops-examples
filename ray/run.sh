docker build . -t ray-example
docker run --rm ray-example python /app/what_example.py
docker run --shm-size=2gb --rm ray-example python /app/ray_example.py
