from datetime import datetime

import ray


@ray.remote
def f(a, b):
	s = 0
	for i in range(a, b):
		s += i
	return s


if __name__ == "__main__":
	ray.init()
	start = datetime.now()
	futures = []
	for i in range(10):
		futures.append(f.remote(i * 100_000_000, (i + 1) * 100_000_000))
	print(sum(ray.get(futures)))
	end = datetime.now()
	print("Execution total time:", end - start)
