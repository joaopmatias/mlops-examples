from datetime import datetime

from celery import Celery, group

app = Celery(
    'celery_example',
    backend='redis://localhost:6379',
    broker='redis://localhost:6379'
)


@app.task
def f(a, b):
    s = 0
    for i in range(a, b):
        s += i
    return s


if __name__ == "__main__":
    start = datetime.now()
    futures = []
    for i in range(10):
        futures.append(f.s(i * 100_000_000, (i + 1) * 100_000_000))
    promise = group(futures)()
    print(sum(promise.get()))
    end = datetime.now()
    print("Execution total time:", end - start)
