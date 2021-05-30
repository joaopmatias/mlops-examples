from datetime import datetime


def f(a, b):
	s = 0
	for i in range(a, b):
		s += i
	return s


if __name__ == "__main__":
	start = datetime.now()
	print(sum([f(i * 100_000_000, (i + 1) * 100_000_000) for i in range(10)]))
	end = datetime.now()
	print(end - start)
