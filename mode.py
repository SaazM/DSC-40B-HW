def mode(numbers):
    counts = {}
    best_value = None
    best_count = 0

    for x in numbers:
        counts[x] = counts.get(x, 0) + 1
        if counts[x] > best_count:
            best_count = counts[x]
            best_value = x

    return best_value
