from datetime import datetime

from distributed import Client


def f(a, b):
	s = 0
	for i in range(a, b):
		s += i
	return s


if __name__ == "__main__":
	client = Client("localhost:8786")
	start = datetime.now()
	futures = []
	for i in range(10):
		futures.append(client.submit(f, i * 100_000_000, (i + 1) * 100_000_000))
	print(sum(client.gather(futures)))
	end = datetime.now()
	print("Execution total time:", end - start)
