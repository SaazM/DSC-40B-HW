def learn_theta(data, colors):
    """Return theta with all blue <= theta and all red > theta. O(n) time."""
    max_blue = float('-inf')
    min_red = float('inf')

    for value, color in zip(data, colors):
        if color == 'blue':
            if value > max_blue:
                max_blue = value
        elif color == 'red':
            if value < min_red:
                min_red = value

    return (max_blue + min_red) / 2


def compute_ell(data, colors, theta):
    """Return L(theta): misclassified red (<= theta) plus blue (> theta)."""
    loss = 0.0
    for value, color in zip(data, colors):
        if color == 'red' and value <= theta:
            loss += 1
        elif color == 'blue' and value > theta:
            loss += 1
    return float(loss)


def minimize_ell(data, colors):
    """Return theta minimizing L(theta). O(n^2) time; smallest point is blue."""
    best_theta = data[0]
    best_loss = compute_ell(data, colors, best_theta)

    for theta in data:
        loss = compute_ell(data, colors, theta)
        if loss < best_loss:
            best_loss = loss
            best_theta = theta

    return float(best_theta)


def minimize_ell_sorted(data, colors):
    """Return theta minimizing L(theta) when data is sorted. O(n) time."""
    n = len(data)
    total_blue = sum(1 for c in colors if c == 'blue')

    red_leq_theta = 0
    blue_gt_theta = total_blue

    best_theta = data[0]
    best_loss = red_leq_theta + blue_gt_theta

    for alpha in range(1, n + 1):
        idx = alpha - 1
        if colors[idx] == 'red':
            red_leq_theta += 1
        else:
            blue_gt_theta -= 1

        loss = red_leq_theta + blue_gt_theta
        if loss < best_loss:
            best_loss = loss
            best_theta = data[idx]

    return float(best_theta)
