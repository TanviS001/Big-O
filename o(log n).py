# O(log n)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Logarithmic time complexity.
# The runtime grows slower as the input size increases, typical in divide-and-conquer algorithms like binary search.
# Efficient with larger inputs.
