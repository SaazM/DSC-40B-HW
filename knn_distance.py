import random


def knn_distance(arr, q, k):
    """
    Return:
      1) the distance from q to its k-th closest point in arr
      2) that k-th closest point itself

    k is 1-indexed.
    This function may modify arr.
    """
    for i, value in enumerate(arr):
        arr[i] = (abs(value - q), value)

    target = k - 1
    left = 0
    right = len(arr) - 1

    while left <= right:
        pivot_idx = random.randint(left, right)
        arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
        pivot_dist = arr[right][0]

        store = left
        for j in range(left, right):
            if arr[j][0] < pivot_dist:
                arr[store], arr[j] = arr[j], arr[store]
                store += 1

        arr[store], arr[right] = arr[right], arr[store]

        if store == target:
            distance, point = arr[store]
            return distance, point
        if store < target:
            left = store + 1
        else:
            right = store - 1

    # Unreachable for valid inputs where 1 <= k <= len(arr).
    raise ValueError("Invalid input for k")
