import sys

try:
	assert len(sys.argv) <= 2, "more than one argument provided"
	if (len(sys.argv) > 1):
		try:
			n = int(sys.argv[1])
		except ValueError:
			raise AssertionError("argument is not an integer")
		print("I'm odd") if (int(sys.argv[1]) % 2) else print("I'm even")

except AssertionError as e:
	print(f"{AssertionError.__name__}{":"}" ,  e)