def histogram(points, bins):
    """Efficiently computes a histogram.

    Assumes that both `points` and `bins` are sorted in ascending order to
    avoid looping through all bins for each point.

    """
    n = len(points)
    densities = []

    point_idx = 0

    for start, end in bins:
        count = 0

        # Because points and bins are sorted, each point is visited once total.
        while point_idx < n and points[point_idx] < end:
            count += 1
            point_idx += 1

        width = end - start
        densities.append(count / (n * width))

    return densities
