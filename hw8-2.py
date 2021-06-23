def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def binomial(n, r):
    if n < 0 or r < 0:
        print("Invalid numbers given")
    return factorial(n) / (factorial(r) * factorial(n - r))

print(binomial(5, 0))
print(binomial(5, 3))
