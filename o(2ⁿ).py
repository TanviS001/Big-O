# O(2ⁿ)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Quadratic time complexity.
# Runtime increases significantly as input size grows; occurs in algorithms with nested loops.
# Suitable for smaller inputs but inefficient for larger datasets.
