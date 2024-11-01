# O(2ⁿ)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Exponential time complexity.
# Runtime doubles with each additional input, typical in algorithms with recursive calls, like recursive Fibonacci.
# Generally impractical for large inputs.
