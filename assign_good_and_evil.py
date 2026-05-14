"""Homework 06 - Programming Problem 1.

Determine whether an undirected rivalry graph is bipartite and, if so,
return one valid good/evil labeling.
"""

from collections import deque


def assign_good_and_evil(graph):
    """Return a valid good/evil labeling, or None if impossible.

    Parameters
    ----------
    graph : dsc40graph.UndirectedGraph
        Rivalry graph where nodes are schools and edges are rivalries.

    Returns
    -------
    dict or None
        A dictionary mapping each node to 'good' or 'evil' if a valid labeling
        exists. Returns None if any edge would force two adjacent nodes to have
        the same label.
    """
    labels = {}

    for start in graph.nodes:
        if start in labels:
            continue

        labels[start] = "good"
        queue = deque([start])

        while queue:
            current = queue.popleft()
            current_label = labels[current]
            opposite_label = "evil" if current_label == "good" else "good"

            for neighbor in graph.neighbors(current):
                if neighbor not in labels:
                    labels[neighbor] = opposite_label
                    queue.append(neighbor)
                elif labels[neighbor] == current_label:
                    return None

    return labels
