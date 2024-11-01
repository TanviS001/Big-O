# O(n log n)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        # Merging logic omitted for brevity
    return arr


# Log-linear time complexity.
# Common in efficient sorting algorithms like merge sort or heap sort.
# A balance between speed and complexity for larger datasets.
