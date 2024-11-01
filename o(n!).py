# O(n!)

def permute(arr):
    if len(arr) == 0:
        return [[]]
    result = []
    for i in range(len(arr)):
        elem = arr[i]
        rest = arr[:i] + arr[i + 1:]
        for p in permute(rest):
            result.append([elem] + p)
    return result

# Factorial time complexity.
# Runtime grows extremely fast with input size, common in algorithms that generate all permutations of an input.
# Feasible only for very small inputs due to explosive growth.
