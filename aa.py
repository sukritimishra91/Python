def generate_ints(n):
    for i in range(n):
        yield i
g = generate_ints(3)

type(g)


cities = ["San Jose", "Redwood City", "Sunnyvale"]
iterator_obj = iter(cities)

print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))


( i*i for i in range(10) )






