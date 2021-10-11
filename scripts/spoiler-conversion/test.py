def g():
	a = [1,2,3,4]
	for n in a:
		yield n
	
g = g()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))