def swap_sum(A, B):
    """
    Return indices (i, j) such that swapping A[i] and B[j] makes:
        sum(B_after) == sum(A_after) + 10
    If no such indices exist, return None.
    """
    sum_a = sum(A)
    sum_b = sum(B)

    # From algebra:
    # (sum_b - sum_a) + 2 * (A[i] - B[j]) = 10
    # so A[i] - B[j] must equal target_diff.
    numerator = 10 - (sum_b - sum_a)
    if numerator % 2 != 0:
        return None

    target_diff = numerator // 2

    i = 0
    j = 0

    while i < len(A) and j < len(B):
        current = A[i] - B[j]

        if current == target_diff:
            return (i, j)
        if current < target_diff:
            i += 1
        else:
            j += 1

    return None
