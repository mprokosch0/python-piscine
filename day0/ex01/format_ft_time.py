import time as tm

a = tm.time()
split = tm.asctime(tm.localtime()).split()
print("Seconds since January 1, 1970:", f"{int(a):,}", "or", f"{int(a):e}", "in scientific notation")
print(split[1], split[2], split[4])